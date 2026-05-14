import os
import sys
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.auth import DBUser

def make_admin(email):
    db: Session = SessionLocal()
    try:
        user = db.query(DBUser).filter(DBUser.email == email).first()
        if user:
            user.is_admin = True
            db.commit()
            print(f"SUCCESS: {email} is now an admin!")
        else:
            print(f"ERROR: User with email {email} not found.")
    except Exception as e:
        print(f"DATABASE ERROR: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    email = "syrymkyrkynbay05@gmail.com"
    make_admin(email)
