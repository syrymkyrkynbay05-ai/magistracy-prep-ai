"""
Seed Database (Дерекқорлар) questions.
Based on "Дерекқорлар.md" specification.

Topics:
1. ER-Modeling (Entity, Relationship)
2. Relational Model & Normalization (1NF, 2NF, 3NF, BCNF)
3. SQL (Select, Join, Aggregate)
4. DBMS Architecture & Integrity (ACID)

Total: ~25 questions.
"""

import os
import sys
import uuid

backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from database import SessionLocal
from models import DBSubject, DBQuestion, DBOption, SubjectId, QuestionType

# ============================================================================
# DATABASE QUESTIONS
# ============================================================================

DB_QUESTIONS = [
    # --- 1. ER-Modeling ---
    {
        "text": "ER-диаграммасындағы 'E' әрпі нені білдіреді?",
        "options": [
            "Element (Элемент)",
            "Entity (Субъект/Нысан)",
            "Error (Қате)",
            "Engine (Қозғалтқыш)",
        ],
        "correct_indices": [1],
        "topic": "db_er_model",
        "difficulty": "A",
    },
    {
        "text": "ER-модельдегі 'Бір мұғалім — көп студент' байланысы қалай белгіленеді?",
        "options": ["1:1", "1:M", "M:N", "M:1"],
        "correct_indices": [1],
        "topic": "db_er_model",
        "difficulty": "A",
    },
    {
        "text": "Объектіні бірегей анықтайтын атрибут қалай аталады?",
        "options": [
            "Жай атрибут",
            "Күрделі атрибут",
            "Кілттік атрибут",
            "Туынды атрибут",
        ],
        "correct_indices": [2],
        "topic": "db_er_model",
        "difficulty": "B",
    },
    # --- 2. Relational Model & Normalization ---
    {
        "text": "Реляциялық деректер моделінде кесте қалай аталады?",
        "options": ["Атрибут", "Домен", "Қатынас (Relation)", "Кортеж"],
        "correct_indices": [2],
        "topic": "db_normalization",
        "difficulty": "A",
    },
    {
        "text": "Нормализацияның негізгі мақсаты не?",
        "options": [
            "Деректердің көлемін ұлғайту",
            "Артық деректерді (redundancy) азайту және құрылымды дұрыс ұйымдастыру",
            "Сұраныстарды баяулату",
            "Барлық деректерді бір кестеге жинау",
        ],
        "correct_indices": [1],
        "topic": "db_normalization",
        "difficulty": "B",
    },
    {
        "text": "X → Y жазуы нені білдіреді?",
        "options": [
            "X және Y тең",
            "Y мәні X-ке функционалды тәуелді",
            "X мәні Y-ке функционалды тәуелді",
            "X пен Y байланыспаған",
        ],
        "correct_indices": [1],
        "topic": "db_normalization",
        "difficulty": "B",
    },
    {
        "text": "Қай нормальді форма транзитивті тәуелділікті жоюды талап етеді?",
        "options": ["1NF", "2NF", "3NF", "BCNF"],
        "correct_indices": [2],
        "topic": "db_normalization",
        "difficulty": "C",
    },
    {
        "text": "Денормализация не үшін қолданылады?",
        "options": [
            "Деректер қауіпсіздігі үшін",
            "Өнімділікті арттыру үшін (оқу жылдамдығын)",
            "Дискіде орын үнемдеу үшін",
            "Кодты қысқарту үшін",
        ],
        "correct_indices": [1],
        "topic": "db_normalization",
        "difficulty": "C",
    },
    # --- 3. SQL ---
    {
        "text": "Келесі сұраныс не істейді?\nSELECT * FROM Students ORDER BY GPA DESC LIMIT 3;",
        "options": [
            "Барлық студенттерді көрсетеді",
            "GPA ең төмен 3 студентті көрсетеді",
            "GPA ең жоғары 3 студентті көрсетеді",
            "Кездейсоқ 3 студентті көрсетеді",
        ],
        "correct_indices": [2],
        "topic": "db_sql",
        "difficulty": "B",
    },
    {
        "text": "Екі кестенің тек ортақ мәндерін қайтаратын JOIN түрі:",
        "options": ["LEFT JOIN", "RIGHT JOIN", "INNER JOIN", "FULL OUTER JOIN"],
        "correct_indices": [2],
        "topic": "db_sql",
        "difficulty": "B",
    },
    {
        "text": "SQL-де қай оператор бірегей (қайталанбайтын) мәндерді алу үшін қолданылады?",
        "options": ["UNIQUE", "DISTINCT", "DIFFERENT", "SINGLE"],
        "correct_indices": [1],
        "topic": "db_sql",
        "difficulty": "A",
    },
    {
        "text": "Топтастырылған деректерге шарт қою үшін қай оператор қолданылады?",
        "options": ["WHERE", "HAVING", "ORDER BY", "GROUP BY"],
        "correct_indices": [1],
        "topic": "db_sql",
        "difficulty": "C",
    },
    {
        "text": "SELECT COUNT(*) FROM Users; сұранысының нәтижесі:",
        "options": [
            "Пайдаланушылардың тізімі",
            "Пайдаланушылар саны",
            "Ең үлкен ID",
            "Бос мәндер",
        ],
        "correct_indices": [1],
        "topic": "db_sql",
        "difficulty": "A",
    },
    # --- 4. DBMS Architecture & Integrity ---
    {
        "text": "ACID қасиеттеріндегі 'A' (Atomicity) нені білдіреді?",
        "options": [
            "Транзакция бөліктерге бөлінеді",
            "Транзакция толық орындалады немесе мүлдем орындалмайды",
            "Транзакция әрқашан сәтті аяқталады",
            "Автоматты түрде сақтау",
        ],
        "correct_indices": [1],
        "topic": "db_theory",
        "difficulty": "B",
    },
    {
        "text": "ACID қасиеттеріндегі 'I' (Isolation) нені білдіреді?",
        "options": [
            "Транзакциялар бір-біріне әсер етпейді",
            "Интернет байланысы қажет емес",
            "Деректер құпия сақталады",
            "Интеграция",
        ],
        "correct_indices": [0],
        "topic": "db_theory",
        "difficulty": "B",
    },
    {
        "text": "UI, бизнес логика және дерекқор бөлек орналасқан архитектура:",
        "options": [
            "Файл-сервер",
            "Клиент-сервер (2 деңгейлі)",
            "3 деңгейлі архитектура",
            "Монолитті",
        ],
        "correct_indices": [2],
        "topic": "db_theory",
        "difficulty": "B",
    },
    {
        "text": "Foreign Key арқылы кестелер арасындағы байланыстың дұрыстығын қамтамасыз ететін тұтастық түрі:",
        "options": [
            "Домендік тұтастық",
            "Сілтемелік тұтастық (Referential Integrity)",
            "Семантикалық тұтастық",
            "Физикалық тұтастық",
        ],
        "correct_indices": [1],
        "topic": "db_theory",
        "difficulty": "C",
    },
    {
        "text": "Транзакция нәтижелерінің жүйе істен шыққанда да сақталуы ACID-тың қай қасиеті?",
        "options": ["Atomicity", "Consistency", "Isolation", "Durability"],
        "correct_indices": [3],
        "topic": "db_theory",
        "difficulty": "C",
    },
    {
        "text": "SQL тілінде жаңа кесте құру командасы:",
        "options": ["ADD TABLE", "NEW TABLE", "CREATE TABLE", "MAKE TABLE"],
        "correct_indices": [2],
        "topic": "db_sql",
        "difficulty": "A",
    },
    {
        "text": "Primary Key өрісі қандай қасиеттерге ие?",
        "options": [
            "Қайталанатын мәндер болуы мүмкін",
            "NULL мәнін қабылдайды",
            "Бірегей және NULL емес",
            "Кез келген мәнді қабылдайды",
        ],
        "correct_indices": [2],
        "topic": "db_theory",
        "difficulty": "B",
    },
    {
        "text": "Деректер қорындағы 'View' (Көрініс) дегеніміз не?",
        "options": [
            "Нақты деректер сақталған физикалық кесте",
            "Сұраныс нәтижесінде құрылған виртуалды кесте",
            "Графикалық интерфейс",
            "Деректердің резервтік көшірмесі",
        ],
        "correct_indices": [1],
        "topic": "db_sql",
        "difficulty": "C",
    },
    {
        "text": "Кестеден деректерді өшіру командасы (құрылымын сақтай отырып):",
        "options": ["DROP", "DELETE", "REMOVE", "CLEAR"],
        "correct_indices": [1],
        "topic": "db_sql",
        "difficulty": "A",
        "hint": "DROP кестені толық өшіреді, DELETE тек деректерді өшіреді.",
    },
    {
        "text": "1:1 байланысының мысалы:",
        "options": [
            "Студент - Пән",
            "Адам - Паспорт (бір елде)",
            "Мұғалім - Сынип",
            "Автор - Кітап",
        ],
        "correct_indices": [1],
        "topic": "db_er_model",
        "difficulty": "A",
    },
]


def seed_db_questions():
    """Add Database questions to database."""
    db = SessionLocal()

    try:
        # Ensure DB subject exists
        # In types.ts it is SubjectId.DB ('db')
        db_subject = (
            db.query(DBSubject).filter(DBSubject.id == SubjectId.DB.value).first()
        )
        if not db_subject:
            print("Creating DB Subject...")
            db_subject = DBSubject(
                id=SubjectId.DB.value, name="Мағлұматтар қоры (Databases)"
            )
            db.add(db_subject)
            db.commit()

        all_questions = DB_QUESTIONS
        added = 0

        print(f"Adding {len(all_questions)} Database questions...")

        for q_data in all_questions:
            q_id = str(uuid.uuid4())

            db_question = DBQuestion(
                id=q_id,
                subject_id=SubjectId.DB.value,
                text=q_data["text"],
                type=QuestionType.SINGLE,
                topic=q_data["topic"],
                difficulty=q_data.get("difficulty", "medium"),
                language_level=None,
            )
            db.add(db_question)

            correct_ids = []
            for idx, opt_text in enumerate(q_data["options"]):
                opt_id = str(uuid.uuid4())
                db_option = DBOption(id=opt_id, question_id=q_id, text=opt_text)
                db.add(db_option)

                if idx in q_data["correct_indices"]:
                    correct_ids.append(opt_id)

            db_question.correct_option_ids = ",".join(correct_ids)
            added += 1

        db.commit()

        print(f"\n[OK] Successfully added {added} Database questions!")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    print("=" * 60)
    print("[DB] Database Questions Seeder")
    print("=" * 60)
    seed_db_questions()
