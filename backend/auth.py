"""
Authentication module — JWT tokens, password hashing, OTP email, user management.
"""

import os
import random
import secrets
import hashlib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from database import Base, get_db
from dotenv import load_dotenv

load_dotenv()

# --------------- Configuration ---------------
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "magistracy-ai-super-secret-key-2026")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24 hours

# SMTP Config
SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")

# OTP Config
OTP_EXPIRES_SECONDS = int(os.getenv("OTP_EXPIRES_SECONDS", "300"))


# --------------- Password Hashing (stdlib, no freeze) ---------------
_HASH_ITERATIONS = 100_000


def get_password_hash(password: str) -> str:
    salt = secrets.token_hex(16)
    h = hashlib.pbkdf2_hmac(
        "sha256", password.encode(), salt.encode(), _HASH_ITERATIONS
    )
    return f"{salt}${h.hex()}"


def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        salt, stored_hash = hashed_password.split("$", 1)
        h = hashlib.pbkdf2_hmac(
            "sha256", plain_password.encode(), salt.encode(), _HASH_ITERATIONS
        )
        return h.hex() == stored_hash
    except (ValueError, AttributeError):
        return False


# --------------- JWT Token ---------------
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# --------------- OTP Generation ---------------
def generate_otp() -> str:
    """Generate a 6-digit OTP code."""
    return str(random.randint(100000, 999999))


# --------------- Email Sending ---------------
def send_otp_email(to_email: str, otp_code: str, user_name: str = "") -> bool:
    """Send OTP code to user's email via Gmail SMTP."""
    if not SMTP_USER or not SMTP_PASS:
        print(f"[DEV MODE] OTP for {to_email}: {otp_code}")
        return True

    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"🔐 MagistracyAI — Қалпына келтіру коды: {otp_code}"
        msg["From"] = f"MagistracyAI <{SMTP_USER}>"
        msg["To"] = to_email

        html_body = f"""
        <div style="font-family: 'Segoe UI', Arial, sans-serif; max-width: 480px; margin: 0 auto; padding: 30px; background: #0a0c10; border-radius: 20px; border: 1px solid #1e293b;">
            <div style="text-align: center; margin-bottom: 24px;">
                <h1 style="color: #f8fafc; font-size: 24px; margin: 0;">🎓 MagistracyAI</h1>
                <p style="color: #64748b; font-size: 13px; margin-top: 4px;">Магистратураға дайындық платформасы</p>
            </div>
            <div style="background: #111827; border-radius: 16px; padding: 24px; text-align: center; border: 1px solid #1e293b;">
                <p style="color: #94a3b8; font-size: 14px; margin: 0 0 16px;">
                    {('Сәлем, ' + user_name + '! ' if user_name else '')}Парольді қалпына келтіру коды:
                </p>
                <div style="background: linear-gradient(135deg, #3b82f6, #6366f1); border-radius: 12px; padding: 16px; display: inline-block;">
                    <span style="color: white; font-size: 32px; font-weight: 900; letter-spacing: 8px; font-family: monospace;">{otp_code}</span>
                </div>
                <p style="color: #64748b; font-size: 12px; margin-top: 16px;">
                    Код {OTP_EXPIRES_SECONDS // 60} минут ішінде жарамды.
                </p>
            </div>
            <p style="color: #475569; font-size: 11px; text-align: center; margin-top: 20px;">
                Егер сіз бұл сұрауды жасамаған болсаңыз, хабарламаны елемеңіз.
            </p>
        </div>
        """

        msg.attach(MIMEText(html_body, "html", "utf-8"))

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, to_email, msg.as_string())

        print(f"[EMAIL] OTP sent to {to_email}")
        return True
    except Exception as e:
        print(f"[EMAIL ERROR] {e}")
        return False


# --------------- SQLAlchemy User Model ---------------
class DBUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    full_name = Column(String(255), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(
        DateTime, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None)
    )
    # OTP fields
    otp_code = Column(String(6), nullable=True)
    otp_expires_at = Column(DateTime, nullable=True)


# --------------- Pydantic Schemas ---------------
class UserRegister(BaseModel):
    email: str
    full_name: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: "UserProfile"


class UserProfile(BaseModel):
    id: int
    email: str
    full_name: str
    is_active: bool

    class Config:
        from_attributes = True


class ForgotPasswordRequest(BaseModel):
    email: str


class VerifyOtpRequest(BaseModel):
    email: str
    otp_code: str


class ResetPasswordRequest(BaseModel):
    email: str
    otp_code: str
    new_password: str


class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str


class MessageResponse(BaseModel):
    message: str


class HistoryItem(BaseModel):
    id: int
    total_score: int
    max_score: int
    subject_scores: str  # JSON string
    correct_count: int
    total_questions: int
    created_at: datetime

    class Config:
        from_attributes = True


# --------------- Dependency: Get Current User ---------------
def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> DBUser:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Токен жарамсыз немесе мерзімі аяқталған",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(DBUser).filter(DBUser.id == int(user_id)).first()
    if user is None or not user.is_active:
        raise credentials_exception
    return user
