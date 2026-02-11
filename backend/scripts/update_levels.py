"""
Сұрақтарға language_level (A1/A2/B1/B2) және difficulty (A/B/C) мәндерін қосу скрипті.
Спецификация бойынша:
- Listening: A1 (8), A2 (4), B1 (2), B2 (2)
- Grammar: A1 (15), A2 (6), B1 (6), B2 (5)
- Reading: A1 (15), A2 (9), B1 (6), B2 (3), C (3)
"""

import os
import sys

backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from sqlalchemy import func
from database import SessionLocal
from models import DBQuestion, SubjectId


def update_question_levels():
    """Update language_level and difficulty for English questions"""
    db = SessionLocal()

    try:
        # Get all English questions grouped by topic
        listening_qs = (
            db.query(DBQuestion)
            .filter(
                DBQuestion.subject_id == SubjectId.ENGLISH.value,
                DBQuestion.topic.ilike("%listening%"),
            )
            .all()
        )

        grammar_qs = (
            db.query(DBQuestion)
            .filter(
                DBQuestion.subject_id == SubjectId.ENGLISH.value,
                DBQuestion.topic.ilike("%grammar%"),
            )
            .all()
        )

        reading_qs = (
            db.query(DBQuestion)
            .filter(
                DBQuestion.subject_id == SubjectId.ENGLISH.value,
                DBQuestion.topic.ilike("%reading%"),
            )
            .all()
        )

        updated = 0

        # Update Listening questions (A1:8, A2:4, B1:2, B2:2)
        print(f"Updating {len(listening_qs)} listening questions...")
        for i, q in enumerate(listening_qs):
            if i < 8:
                q.language_level = "A1"
                q.difficulty = "A"  # Easy
            elif i < 12:
                q.language_level = "A2"
                q.difficulty = "B"  # Medium
            elif i < 14:
                q.language_level = "B1"
                q.difficulty = "B"
            else:
                q.language_level = "B2"
                q.difficulty = "C"  # Hard
            updated += 1

        # Update Grammar questions (A1:15, A2:6, B1:6, B2:5)
        print(f"Updating {len(grammar_qs)} grammar questions...")
        for i, q in enumerate(grammar_qs):
            if i < 15:
                q.language_level = "A1"
                q.difficulty = "A" if i < 5 else ("B" if i < 10 else "C")
            elif i < 21:
                q.language_level = "A2"
                q.difficulty = "A" if i < 17 else ("B" if i < 19 else "C")
            elif i < 27:
                q.language_level = "B1"
                q.difficulty = "A" if i < 23 else ("B" if i < 25 else "C")
            else:
                q.language_level = "B2"
                q.difficulty = "A" if i < 29 else ("B" if i < 31 else "C")
            updated += 1

        # Update Reading questions (A1:15, A2:9, B1:6, B2:3, C:3)
        print(f"Updating {len(reading_qs)} reading questions...")
        for i, q in enumerate(reading_qs):
            if i < 15:
                q.language_level = "A1"
                q.difficulty = "A" if i < 5 else ("B" if i < 10 else "C")
            elif i < 24:
                q.language_level = "A2"
                q.difficulty = "A" if i < 18 else ("B" if i < 21 else "C")
            elif i < 30:
                q.language_level = "B1"
                q.difficulty = "A" if i < 26 else ("B" if i < 28 else "C")
            elif i < 33:
                q.language_level = "B2"
                q.difficulty = "B"
            else:
                q.language_level = "C"
                q.difficulty = "C"
            updated += 1

        db.commit()

        print(f"\n{'='*50}")
        print(f"Successfully updated {updated} questions!")
        print("=" * 50)

        # Stats
        for level in ["A1", "A2", "B1", "B2", "C"]:
            count = (
                db.query(DBQuestion)
                .filter(
                    DBQuestion.subject_id == SubjectId.ENGLISH.value,
                    DBQuestion.language_level == level,
                )
                .count()
            )
            print(f"  {level}: {count} questions")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    print("=" * 50)
    print("Updating Question Language Levels")
    print("=" * 50)
    update_question_levels()
