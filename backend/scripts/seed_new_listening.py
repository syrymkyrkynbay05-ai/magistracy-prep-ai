"""
Seed NEW listening questions from 10 audio texts for English test.
Based on KT test specification - 8 questions per audio text = 80 questions.
Audio files located in: public/english/
"""

import os
import sys
import uuid

backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from database import SessionLocal
from models import DBSubject, DBQuestion, DBOption, SubjectId, QuestionType
from english_listening_questions import LISTENING_QUESTIONS


def seed_new_listening_questions():
    """Add new listening questions from 10 audio texts to database."""
    db = SessionLocal()

    try:
        # Ensure English subject exists
        english_subject = (
            db.query(DBSubject).filter(DBSubject.id == SubjectId.ENGLISH.value).first()
        )
        if not english_subject:
            english_subject = DBSubject(id=SubjectId.ENGLISH.value, name="English")
            db.add(english_subject)
            db.commit()

        added = 0
        text_stats = {}

        print(
            f"Adding listening questions from {len(LISTENING_QUESTIONS)} audio texts..."
        )
        print("=" * 60)

        for text_data in LISTENING_QUESTIONS:
            audio_file = text_data["audio_file"]
            text_id = text_data["text_id"]
            level = text_data["level"]
            questions = text_data["questions"]

            text_stats[audio_file] = 0

            for q_data in questions:
                q_id = str(uuid.uuid4())

                # Create question with audio reference in reading_passage
                db_question = DBQuestion(
                    id=q_id,
                    subject_id=SubjectId.ENGLISH.value,
                    text=q_data["text"],
                    type=QuestionType.SINGLE,
                    topic="listening",
                    difficulty=q_data.get("difficulty", "B"),
                    language_level=level,
                    reading_passage=f"AUDIO:/english/{audio_file}",  # Reference to audio file
                )
                db.add(db_question)

                correct_ids = []
                for idx, opt_text in enumerate(q_data["options"]):
                    opt_id = str(uuid.uuid4())
                    db_option = DBOption(id=opt_id, question_id=q_id, text=opt_text)
                    db.add(db_option)

                    if idx == q_data["correct"]:
                        correct_ids.append(opt_id)

                db_question.correct_option_ids = ",".join(correct_ids)
                added += 1
                text_stats[audio_file] += 1

        db.commit()

        print(f"\n[SUCCESS] Added {added} listening questions!")
        print("=" * 60)
        print("\nBreakdown by audio file:")
        for audio, count in text_stats.items():
            print(f"  - {audio}: {count} questions")

        # Show difficulty distribution
        a_count = sum(
            1
            for t in LISTENING_QUESTIONS
            for q in t["questions"]
            if q.get("difficulty") == "A"
        )
        b_count = sum(
            1
            for t in LISTENING_QUESTIONS
            for q in t["questions"]
            if q.get("difficulty") == "B"
        )
        c_count = sum(
            1
            for t in LISTENING_QUESTIONS
            for q in t["questions"]
            if q.get("difficulty") == "C"
        )

        print(f"\nDifficulty distribution:")
        print(f"  A (easy): {a_count}")
        print(f"  B (medium): {b_count}")
        print(f"  C (hard): {c_count}")

        # Show total listening questions in database
        total_listening = (
            db.query(DBQuestion)
            .filter(
                DBQuestion.subject_id == SubjectId.ENGLISH.value,
                DBQuestion.topic.ilike("%listening%"),
            )
            .count()
        )
        print(f"\nTOTAL Listening Questions in DB: {total_listening}")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    print("=" * 60)
    print("[AUDIO] New Listening Questions Seeder")
    print("10 audio texts x 8 questions = 80 questions")
    print("=" * 60)
    seed_new_listening_questions()
