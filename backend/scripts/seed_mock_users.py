import os
import sys
from datetime import datetime, timedelta, timezone
import json

backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from database import SessionLocal
from auth import DBUser, get_password_hash
from models import DBTestResult

MOCK_USERS_DATA = [
    {"full_name": "Азамат Серікұлы", "email": "azamat@mail.ru", "is_admin": True, "test_count": 12, "avg_score": 88},
    {"full_name": "Аяулым Мақсатқызы", "email": "ayaulym@gmail.com", "is_admin": False, "test_count": 8, "avg_score": 82},
    {"full_name": "Нұрсұлтан Болатұлы", "email": "nursik.b@mail.ru", "is_admin": False, "test_count": 15, "avg_score": 91},
    {"full_name": "Дильназ Арманқызы", "email": "dilnaz.a@yahoo.com", "is_admin": False, "test_count": 5, "avg_score": 68},
    {"full_name": "Бауыржан Талғатұлы", "email": "bauka_t@gmail.com", "is_admin": False, "test_count": 22, "avg_score": 94},
    {"full_name": "Мәдина Қайратқызы", "email": "madina.q@mail.ru", "is_admin": False, "test_count": 3, "avg_score": 80},
    {"full_name": "Ерасыл Нұрланұлы", "email": "era_nurlan@gmail.com", "is_admin": False, "test_count": 18, "avg_score": 85},
    {"full_name": "Жансая Ермекқызы", "email": "zhansaya.e@mail.ru", "is_admin": False, "test_count": 9, "avg_score": 79},
    {"full_name": "Әлібек Ғалымұлы", "email": "alibek_g@gmail.com", "is_admin": False, "test_count": 11, "avg_score": 84},
    {"full_name": "Арайлым Маратқызы", "email": "arai_m@mail.ru", "is_admin": False, "test_count": 14, "avg_score": 87},
    {"full_name": "Руслан Омаров", "email": "ruslan.o@gmail.com", "is_admin": False, "test_count": 6, "avg_score": 76},
    {"full_name": "Ақбота Сәкенқызы", "email": "akbota.s@mail.ru", "is_admin": False, "test_count": 20, "avg_score": 90},
    {"full_name": "Дәурен Серіков", "email": "dauren.s@gmail.com", "is_admin": False, "test_count": 4, "avg_score": 70},
    {"full_name": "Гүлназ Жұмабек", "email": "gulnaz.z@mail.ru", "is_admin": False, "test_count": 16, "avg_score": 93},
    {"full_name": "Абылай Ханұлы", "email": "abylai.h@yahoo.com", "is_admin": False, "test_count": 2, "avg_score": 75}
]

def seed_mock_data():
    db = SessionLocal()
    try:
        # We don't want to clear all users, but we can add or skip if exists
        hashed_pwd = get_password_hash("password123")
        
        for idx, udata in enumerate(MOCK_USERS_DATA):
            # Check if user exists
            existing_user = db.query(DBUser).filter(DBUser.email == udata["email"]).first()
            if not existing_user:
                new_user = DBUser(
                    email=udata["email"],
                    full_name=udata["full_name"],
                    hashed_password=hashed_pwd,
                    is_active=True,
                    is_admin=udata["is_admin"],
                    created_at=datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(days=20-idx)
                )
                db.add(new_user)
                db.commit()
                db.refresh(new_user)
                user_id = new_user.id
            else:
                user_id = existing_user.id

            # Add mock test results
            # Clean up old test results for this user if we want just exactly their mock count
            # (optional, but let's just insert some)
            count_tests = db.query(DBTestResult).filter(DBTestResult.user_id == user_id).count()
            if count_tests < udata["test_count"]:
                needed = udata["test_count"] - count_tests
                for i in range(needed):
                    score = int(udata["avg_score"] + (i % 5) - 2) # small variation
                    score = min(max(score, 0), 100) # clamp
                    
                    sub_scores = {
                        "Ағылшын Тілі": {"score": int(score * 0.5), "max": 50},
                        "Оқу Сауаттылығы": {"score": int(score * 0.3), "max": 30},
                        "Информатика": {"score": int(score * 0.3), "max": 30},
                        "Деректер Қоры": {"score": int(score * 0.2), "max": 20}
                    }
                    
                    test_res = DBTestResult(
                        user_id=user_id,
                        total_score=score,
                        max_score=100,
                        subject_scores=json.dumps(sub_scores, ensure_ascii=False),
                        correct_count=int(score * 1.3),
                        total_questions=130,
                        created_at=datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(days=i)
                    )
                    db.add(test_res)
                db.commit()

        print("Mock users and test results inserted successfully.")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_mock_data()
