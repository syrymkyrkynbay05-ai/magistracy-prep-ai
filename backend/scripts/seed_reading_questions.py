# Seed script for new reading comprehension questions
# Based on specification topics

from database import SessionLocal
from models import DBQuestion, DBOption, DBSubject
from english_reading_questions import READING_TEXTS
import uuid


def seed_reading_questions():
    """Seed reading questions into the database."""
    db = SessionLocal()

    try:
        # Get or create English subject
        english_subject = db.query(DBSubject).filter_by(id="english").first()
        if not english_subject:
            english_subject = DBSubject(
                id="english", name="Ағылшын тілі", question_count=50
            )
            db.add(english_subject)
            db.commit()

        # Delete old reading questions to avoid duplicates
        old_reading = (
            db.query(DBQuestion)
            .filter(
                DBQuestion.subject_id == "english", DBQuestion.topic.ilike("%reading%")
            )
            .all()
        )

        if old_reading:
            print(f"Deleting {len(old_reading)} old reading questions...")
            for q in old_reading:
                db.delete(q)
            db.commit()

        questions_added = 0

        for text_data in READING_TEXTS:
            passage = text_data["passage"]
            level = text_data["level"]

            for q_data in text_data["questions"]:
                # Generate unique ID
                q_id = str(uuid.uuid4())

                # Pre-generate option IDs to know correct one
                correct_idx = q_data["correct"]
                option_ids = [str(uuid.uuid4()) for _ in q_data["options"]]
                correct_option_id = option_ids[correct_idx]

                # Create question FIRST (foreign key requirement)
                question = DBQuestion(
                    id=q_id,
                    subject_id="english",
                    topic="reading",
                    text=q_data["text"],
                    type="SINGLE",  # Required field
                    reading_passage=passage,
                    correct_option_ids=correct_option_id,
                    difficulty=q_data["difficulty"],
                    language_level=level.split("-")[0],
                    hint=None,
                )
                db.add(question)
                db.flush()  # Flush to satisfy FK constraint

                # Create options AFTER question
                for idx, option_text in enumerate(q_data["options"]):
                    option = DBOption(
                        id=option_ids[idx], question_id=q_id, text=option_text
                    )
                    db.add(option)

                questions_added += 1

        db.commit()
        print(f"✅ Successfully added {questions_added} reading questions!")
        print(f"   ({len(READING_TEXTS)} texts × 8 questions each)")

        # Verify
        total = (
            db.query(DBQuestion)
            .filter(DBQuestion.subject_id == "english", DBQuestion.topic == "reading")
            .count()
        )
        print(f"   Total reading questions in DB: {total}")

    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_reading_questions()
