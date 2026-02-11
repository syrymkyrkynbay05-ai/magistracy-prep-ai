"""
Auth API routes — register, login, profile, OTP password reset via email.
"""

from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from auth import (
    DBUser,
    UserRegister,
    UserLogin,
    TokenResponse,
    UserProfile,
    ForgotPasswordRequest,
    VerifyOtpRequest,
    ResetPasswordRequest,
    ChangePasswordRequest,
    MessageResponse,
    HistoryItem,
    get_password_hash,
    verify_password,
    create_access_token,
    generate_otp,
    send_otp_email,
    get_current_user,
    OTP_EXPIRES_SECONDS,
)
from models import DBTestResult

router = APIRouter(prefix="/auth", tags=["Authentication"])


# ==================== REGISTER ====================
@router.post("/register", response_model=TokenResponse, status_code=201)
def register(data: UserRegister, db: Session = Depends(get_db)):
    """Жаңа пайдаланушы тіркеу."""
    if len(data.password) < 6:
        raise HTTPException(400, detail="Құпия сөз кемінде 6 таңбадан тұруы керек")
    if not data.email or "@" not in data.email:
        raise HTTPException(400, detail="Жарамсыз email мекенжайы")
    if not data.full_name.strip():
        raise HTTPException(400, detail="Аты-жөніңізді жазыңыз")

    existing = (
        db.query(DBUser).filter(DBUser.email == data.email.lower().strip()).first()
    )
    if existing:
        raise HTTPException(status_code=409, detail="Бұл email бұрыннан тіркелген")

    user = DBUser(
        email=data.email.lower().strip(),
        full_name=data.full_name.strip(),
        hashed_password=get_password_hash(data.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token({"sub": str(user.id)})
    return TokenResponse(access_token=token, user=UserProfile.model_validate(user))


# ==================== LOGIN ====================
@router.post("/login", response_model=TokenResponse)
def login(data: UserLogin, db: Session = Depends(get_db)):
    """Пайдаланушы кіру."""
    user = db.query(DBUser).filter(DBUser.email == data.email.lower().strip()).first()

    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Email немесе құпия сөз қате")

    if not user.is_active:
        raise HTTPException(status_code=403, detail="Аккаунт бұғатталған")

    token = create_access_token({"sub": str(user.id)})
    return TokenResponse(access_token=token, user=UserProfile.model_validate(user))


# ==================== GET PROFILE ====================
@router.get("/me", response_model=UserProfile)
def get_profile(current_user: DBUser = Depends(get_current_user)):
    """Ағымдағы пайдаланушы профилін алу (токен қажет)."""
    return UserProfile.model_validate(current_user)


# ==================== FORGOT PASSWORD (Send OTP) ====================
@router.post("/forgot-password", response_model=MessageResponse)
def forgot_password(data: ForgotPasswordRequest, db: Session = Depends(get_db)):
    """Парольді қалпына келтіру — email-ге OTP код жіберу."""
    user = db.query(DBUser).filter(DBUser.email == data.email.lower().strip()).first()

    if not user:
        # Қауіпсіздік: email бар-жоғын айтпаймыз
        return MessageResponse(message="Егер бұл email тіркелген болса, код жіберілді")

    # Generate OTP
    otp = generate_otp()
    user.otp_code = otp
    user.otp_expires_at = (
        datetime.now(timezone.utc) + timedelta(seconds=OTP_EXPIRES_SECONDS)
    ).replace(tzinfo=None)
    db.commit()

    # Send email
    sent = send_otp_email(user.email, otp, user.full_name)
    if not sent:
        raise HTTPException(500, detail="Email жіберу кезінде қате орын алды")

    return MessageResponse(message="Қалпына келтіру коды email-ге жіберілді")


# ==================== VERIFY OTP ====================
@router.post("/verify-otp", response_model=MessageResponse)
def verify_otp(data: VerifyOtpRequest, db: Session = Depends(get_db)):
    """OTP кодын тексеру."""
    user = db.query(DBUser).filter(DBUser.email == data.email.lower().strip()).first()

    if not user or not user.otp_code:
        raise HTTPException(400, detail="Код жарамсыз")

    if user.otp_code != data.otp_code:
        raise HTTPException(400, detail="Код қате")

    if (
        user.otp_expires_at
        and datetime.now(timezone.utc).replace(tzinfo=None) > user.otp_expires_at
    ):
        raise HTTPException(400, detail="Кодтың мерзімі аяқталған")

    return MessageResponse(message="Код дұрыс")


# ==================== RESET PASSWORD (with OTP) ====================
@router.post("/reset-password", response_model=MessageResponse)
def reset_password(data: ResetPasswordRequest, db: Session = Depends(get_db)):
    """Жаңа пароль орнату (OTP код арқылы)."""
    if len(data.new_password) < 6:
        raise HTTPException(400, detail="Құпия сөз кемінде 6 таңбадан тұруы керек")

    user = db.query(DBUser).filter(DBUser.email == data.email.lower().strip()).first()

    if not user or not user.otp_code:
        raise HTTPException(400, detail="Код жарамсыз")

    if user.otp_code != data.otp_code:
        raise HTTPException(400, detail="Код қате")

    if (
        user.otp_expires_at
        and datetime.now(timezone.utc).replace(tzinfo=None) > user.otp_expires_at
    ):
        raise HTTPException(400, detail="Кодтың мерзімі аяқталған")

    # Update password & clear OTP
    user.hashed_password = get_password_hash(data.new_password)
    user.otp_code = None
    user.otp_expires_at = None
    db.commit()

    return MessageResponse(message="Құпия сөз сәтті жаңартылды")


# ==================== CHANGE PASSWORD (authenticated) ====================
@router.post("/change-password", response_model=MessageResponse)
def change_password(
    data: ChangePasswordRequest,
    current_user: DBUser = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Парольді ауыстыру (ескісін біліп тұрғанда)."""
    if not verify_password(data.old_password, current_user.hashed_password):
        raise HTTPException(400, detail="Ескі құпия сөз қате")

    if len(data.new_password) < 6:
        raise HTTPException(400, detail="Жаңа құпия сөз кемінде 6 таңбадан тұруы керек")

    current_user.hashed_password = get_password_hash(data.new_password)
    db.commit()

    return MessageResponse(message="Құпия сөз сәтті жаңартылды")


# ==================== TEST HISTORY ====================
@router.get("/history", response_model=list[HistoryItem])
def get_test_history(
    current_user: DBUser = Depends(get_current_user), db: Session = Depends(get_db)
):
    """Пайдаланушының тест нәтижелерінің тарихын алу."""
    history = (
        db.query(DBTestResult)
        .filter(DBTestResult.user_id == current_user.id)
        .order_by(DBTestResult.created_at.desc())
        .all()
    )
    return history


@router.delete("/history/{result_id}", response_model=MessageResponse)
def delete_test_result(
    result_id: int,
    current_user: DBUser = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Тест нәтижесін тарихтан өшіру."""
    result = (
        db.query(DBTestResult)
        .filter(DBTestResult.id == result_id, DBTestResult.user_id == current_user.id)
        .first()
    )

    if not result:
        raise HTTPException(404, detail="Нәтиже табылмады")

    db.delete(result)
    db.commit()

    return MessageResponse(message="Нәтиже өшірілді")
