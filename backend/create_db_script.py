import pymysql
import os
from dotenv import load_dotenv

load_dotenv()


def create_db():
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "")
    host = os.getenv("DB_HOST", "localhost")
    port = int(os.getenv("DB_PORT", "3306"))
    db_name = os.getenv("DB_NAME", "magistracy_prep")

    try:
        connection = pymysql.connect(host=host, user=user, password=password, port=port)
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        connection.close()
        print(f"✅ Database '{db_name}' created or already exists.")
    except Exception as e:
        print(f"❌ Error creating database: {e}")
        print("Please check your MySQL credentials in backend/.env")


if __name__ == "__main__":
    create_db()
