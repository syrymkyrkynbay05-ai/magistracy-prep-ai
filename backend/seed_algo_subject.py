"""
Seed Algorithm (Алгоритмдер) questions.
Based on "Алгоритмдер.md" specification (C++).

Topics:
1. Programming Basics (C++, loops, conditions, struct)
2. Abstract Data Types (Stack, Queue, Lists, Trees)
3. Graph Algorithms (Dijkstra, Prim, Kruskal)
4. Algorithm Complexity (Big O)

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
# ALGORITHM QUESTIONS
# ============================================================================

ALGO_QUESTIONS = [
    # --- 1. Programming Basics (C++) ---
    {
        "text": "Төмендегі кодтың нәтижесі қандай?\n```cpp\nint x = 10;\nwhile (x > 5) {\n    x -= 2;\n}\ncout << x;```",
        "options": ["6", "5", "4", "3"],
        "correct_indices": [2],  # 10 -> 8 -> 6 -> 4 (loops stops)
        "topic": "algo_basics",
        "difficulty": "A",
    },
    {
        "text": "switch-case құрылымында 'break' операторы не үшін қажет?",
        "options": [
            "Циклды тоқтату үшін",
            "Келесі case-ке өтіп кетпеу үшін (fall-through болдырмау)",
            "Бағдарламаны аяқтау үшін",
            "Айнымалыны жою үшін",
        ],
        "correct_indices": [1],
        "topic": "algo_basics",
        "difficulty": "B",
    },
    {
        "text": "C++ тілінде 'struct' дегеніміз не?",
        "options": [
            "Тек бір типті деректер массиві",
            "Цикл түрі",
            "Әртүрлі типтегі деректерді біріктіретін құрылым",
            "Функция",
        ],
        "correct_indices": [2],
        "topic": "algo_basics",
        "difficulty": "A",
    },
    {
        "text": "`do-while` циклінің `while` циклінен айырмашылығы:",
        "options": [
            "Ешқандай айырмашылығы жоқ",
            "`do-while` кем дегенде бір рет орындалады",
            "`while` кем дегенде бір рет орындалады",
            "`do-while` тек сандармен жұмыс істейді",
        ],
        "correct_indices": [1],
        "topic": "algo_basics",
        "difficulty": "A",
    },
    {
        "text": "Қабаттасқан циклдерде (nested loops) ішкі цикл сыртқы циклдің әр итерациясында неше рет орындалады?",
        "options": [
            "Тек бір рет",
            "Толығымен (аяқталғанша)",
            "Орындалмайды",
            "Кездейсоқ рет",
        ],
        "correct_indices": [1],
        "topic": "algo_basics",
        "difficulty": "B",
    },
    # --- 2. Abstract Data Types (ADS) ---
    {
        "text": "LIFO (Last In, First Out) принципін қолданатын деректер құрылымы:",
        "options": ["Кезек (Queue)", "Стек (Stack)", "Ағаш (Tree)", "Массив (Array)"],
        "correct_indices": [1],
        "topic": "algo_ads",
        "difficulty": "A",
    },
    {
        "text": "Кезекте (Queue) бірінші келген элемент қашан шығады?",
        "options": ["Ең соңында", "Ортасында", "Бірінші (FIFO)", "Кездейсоқ"],
        "correct_indices": [2],
        "topic": "algo_ads",
        "difficulty": "A",
    },
    {
        "text": "Екібағытты тізімнің (Doubly Linked List) бірбағытты тізімнен айырмашылығы:",
        "options": [
            "Тек алға жүре алады",
            "Әр түйін алдыңғы және келесі элементке сілтеме жасайды",
            "Жадыны аз қолданады",
            "Тізім шеңбер тәрізді",
        ],
        "correct_indices": [1],
        "topic": "algo_ads",
        "difficulty": "B",
    },
    {
        "text": "Бинарлық іздеу ағашында (BST) сол жақ түйіннің мәні ата-аналық түйін мәнінен:",
        "options": [
            "Үлкен болуы керек",
            "Кіші болуы керек",
            "Тең болуы керек",
            "Екі есе үлкен болуы керек",
        ],
        "correct_indices": [1],
        "topic": "algo_ads",
        "difficulty": "B",
    },
    {
        "text": "Ағаштың биіктігі (height) қалай анықталады?",
        "options": [
            "Түйіндердің жалпы саны",
            "Тамырдан ең алыс жапыраққа дейінгі қабырғалар саны",
            "Ең үлкен мән",
            "Ең кіші мән",
        ],
        "correct_indices": [1],
        "topic": "algo_ads",
        "difficulty": "C",
    },
    # --- 3. Graph Algorithms ---
    {
        "text": "Теріс салмағы жоқ графта ең қысқа жолды табу алгоритмі:",
        "options": ["Беллман-Форд (Bellman-Ford)", "Дейкстра (Dijkstra)", "DFS", "BFS"],
        "correct_indices": [1],
        "topic": "algo_graphs",
        "difficulty": "B",
    },
    {
        "text": "Теріс салмақты қабырғалары бар графта ең қысқа жолды табатын алгоритм:",
        "options": ["Дейкстра", "Беллман-Форд", "Прим", "Крускал"],
        "correct_indices": [1],
        "topic": "algo_graphs",
        "difficulty": "C",
    },
    {
        "text": "Минималды тірек ағашын (Minimum Spanning Tree) құруға арналған алгоритмдер:",
        "options": [
            "Дейкстра және Флойд-Уоршелл",
            "Прим және Крускал",
            "BSF және DFS",
            "Sort және Merge",
        ],
        "correct_indices": [1],
        "topic": "algo_graphs",
        "difficulty": "B",
    },
    {
        "text": "Флойд-Уоршелл алгоритмі не үшін қолданылады?",
        "options": [
            "Тек екі төбе арасындағы жолды табу",
            "Барлық төбелер жұбы арасындағы ең қысқа жолды табу",
            "Графты сұрыптау",
            "Цикл бар-жоғын тексеру",
        ],
        "correct_indices": [1],
        "topic": "algo_graphs",
        "difficulty": "C",
    },
    # --- 4. Complexity (Big O) ---
    {
        "text": "Алгоритмнің ең жақсы уақытша тиімділігі тұрақты уақыт болса, ол қалай жазылады?",
        "options": ["O(n)", "O(log n)", "O(1)", "O(n^2)"],
        "correct_indices": [2],
        "topic": "algo_complexity",
        "difficulty": "A",
    },
    {
        "text": "Егер массивті бір рет толық аралап шықсақ, күрделілік қандай болады?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
        "correct_indices": [2],
        "topic": "algo_complexity",
        "difficulty": "A",
    },
    {
        "text": "Қабаттасқан екі цикл (nested loops) болса, күрделілік шамамен:",
        "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"],
        "correct_indices": [2],
        "topic": "algo_complexity",
        "difficulty": "B",
    },
    {
        "text": "Бинарлық іздеу (Binary Search) алгоритмінің күрделілігі:",
        "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"],
        "correct_indices": [1],
        "topic": "algo_complexity",
        "difficulty": "B",
    },
    {
        "text": "Тиімді сұрыптау алгоритмдерінің (мысалы, Merge Sort) орташа күрделілігі:",
        "options": ["O(n)", "O(n^2)", "O(n log n)", "O(n!)"],
        "correct_indices": [2],
        "topic": "algo_complexity",
        "difficulty": "C",
    },
    {
        "text": "О(2^n) қандай күрделілік түріне жатады?",
        "options": ["Сызықтық", "Квадраттық", "Экспоненциалдық", "Логарифмдік"],
        "correct_indices": [2],
        "topic": "algo_complexity",
        "difficulty": "C",
    },
]


def seed_algo_questions():
    """Add Algorithm questions to database."""
    db = SessionLocal()

    try:
        # Ensure ALGO subject exists
        # In types.ts it is SubjectId.ALGO ('algo')
        algo_subject = (
            db.query(DBSubject).filter(DBSubject.id == SubjectId.ALGO.value).first()
        )
        if not algo_subject:
            print("Creating ALGO Subject...")
            algo_subject = DBSubject(
                id=SubjectId.ALGO.value, name="Алгоритмдер (Algorithms)"
            )
            db.add(algo_subject)
            db.commit()

        all_questions = ALGO_QUESTIONS
        added = 0

        print(f"Adding {len(all_questions)} Algorithm questions...")

        for q_data in all_questions:
            q_id = str(uuid.uuid4())

            db_question = DBQuestion(
                id=q_id,
                subject_id=SubjectId.ALGO.value,
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

        print(f"\n[OK] Successfully added {added} Algorithm questions!")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    print("=" * 60)
    print("[ALGO] Algorithm Questions Seeder")
    print("=" * 60)
    seed_algo_questions()
