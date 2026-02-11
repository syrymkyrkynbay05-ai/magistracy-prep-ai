"""
Seed listening questions for monologue audio files.
Based on KT test specification - 8 questions per audio text.
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
# MONOLOGUE 1: Great Leaders (monologue_leaders.wav)
# ============================================================================
LISTENING_LEADERS = [
    {
        "text": "According to the monologue, most great leaders:",
        "options": [
            "Are born with leadership skills",
            "Learn to be great over time",
            "Become CEOs immediately",
            "Don't need any training",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "Great leaders stay ___ when things get difficult.",
        "options": ["Angry", "Calm", "Excited", "Sad"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "The speaker mentions that confident leaders are NOT:",
        "options": ["Helpful", "Strong", "Arrogant", "Comfortable"],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "A soccer coach who isn't excited about sports:",
        "options": [
            "Gets great results",
            "Hardly ever gets great results",
            "Wins championships",
            "Trains harder",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "Good communication for leaders means:",
        "options": [
            "Only speaking clearly",
            "Communicating ideas and listening carefully",
            "Writing emails",
            "Giving orders",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "Akio Morita's first product was:",
        "options": ["A television", "A radio", "A rice cooker", "A phone"],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "What happened with Morita's first product?",
        "options": [
            "It was very successful",
            "It burnt the rice",
            "It was too expensive",
            "It broke easily",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "C",
    },
    {
        "text": "The main message of the monologue is:",
        "options": [
            "Leadership cannot be learned",
            "Only CEOs are leaders",
            "Leadership qualities can be developed",
            "Failure means giving up",
        ],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "B2",
        "difficulty": "C",
    },
]


# ============================================================================
# MONOLOGUE 2: Film Review (monologue_films.wav)
# ============================================================================
LISTENING_FILMS = [
    {
        "text": "The film 'Jungle Fever' is:",
        "options": ["A documentary", "A cartoon", "A drama", "A horror film"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "The documentary that 'Jungle Fever' is based on was about:",
        "options": [
            "Lions in Africa",
            "Tigers in India",
            "Bears in Russia",
            "Pandas in China",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "Steve Willis was known as an ___ hero.",
        "options": ["Comedy", "Action", "Horror", "Drama"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "In the film 'Call', Steve Willis plays a:",
        "options": ["Police officer", "Chef", "Doctor", "Teacher"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "The comedy 'Swim' is about a man who:",
        "options": [
            "Is a professional swimmer",
            "Learns to swim as an adult",
            "Teaches swimming",
            "Wins a competition",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "How old is the main character in 'Swim'?",
        "options": ["10 years old", "20 years old", "30 years old", "40 years old"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "'Mountain Dreams' is about:",
        "options": [
            "Mountain animals",
            "Climbers on Everest",
            "Mountain villages",
            "Skiing",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "C",
    },
    {
        "text": "The reviewer's attitude toward 'Jungle Fever' is:",
        "options": ["Negative", "Neutral", "Positive", "Unclear"],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "B2",
        "difficulty": "C",
    },
]


# ============================================================================
# MONOLOGUE 3: University Life (monologue_university.wav)
# ============================================================================
LISTENING_UNIVERSITY = [
    {
        "text": "Cambridge University was founded in:",
        "options": ["1109", "1209", "1309", "1409"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "How many students does Cambridge have?",
        "options": ["Over 13,000", "Over 23,000", "Over 33,000", "Over 43,000"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "Cambridge has how many colleges?",
        "options": ["21", "31", "41", "51"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "Supervisions at Cambridge involve:",
        "options": [
            "Large lecture halls",
            "Small group sessions with 1-2 students",
            "Online learning only",
            "Self-study",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "The University Library receives:",
        "options": [
            "Only academic books",
            "Every book published in UK",
            "Only old books",
            "Foreign books only",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "C",
    },
    {
        "text": "The boat race is against which university?",
        "options": ["Harvard", "Yale", "Oxford", "London"],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "The boat race is held on:",
        "options": ["River Cambridge", "River Thames", "River Severn", "River Avon"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "C",
    },
    {
        "text": "The main purpose of this monologue is:",
        "options": [
            "To criticize Cambridge",
            "To introduce Cambridge to visitors",
            "To compare universities",
            "To discuss exams",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B2",
        "difficulty": "C",
    },
]


# ============================================================================
# MONOLOGUE 4: Kazakhstan Culture (monologue_kazakhstan.wav)
# ============================================================================
LISTENING_KAZAKHSTAN = [
    {
        "text": "Kazakhstan is the ___ largest country in the world.",
        "options": ["5th", "7th", "9th", "11th"],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "A traditional Kazakh dwelling is called:",
        "options": ["Tent", "Kiiz uy (yurt)", "House", "Cabin"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "Kumys is made from:",
        "options": ["Cow's milk", "Goat's milk", "Mare's milk", "Sheep's milk"],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "'Beshbarmak' means:",
        "options": ["Five fingers", "Five stars", "Five plates", "Five tastes"],
        "correct_indices": [0],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "The dombra has how many strings?",
        "options": ["One", "Two", "Three", "Four"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "Nauryz is celebrated on:",
        "options": ["March 1st", "March 15th", "March 22nd", "March 31st"],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "Traditional songs called 'kuis' tell stories about:",
        "options": [
            "Only wars",
            "Nature, love, and history",
            "Only cooking",
            "Only politics",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "C",
    },
    {
        "text": "The nomadic heritage influences:",
        "options": [
            "Nothing today",
            "Modern Kazakh culture",
            "Only language",
            "Only music",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B2",
        "difficulty": "C",
    },
]


# ============================================================================
# MONOLOGUE 5: Technology (monologue_technology.wav)
# ============================================================================
LISTENING_TECHNOLOGY = [
    {
        "text": "Your smartphone has more computing power than:",
        "options": [
            "A modern laptop",
            "Computers that sent astronauts to the moon",
            "A supercomputer",
            "A gaming PC",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "AI can now do all EXCEPT:",
        "options": ["Diagnose diseases", "Drive cars", "Create art", "Feel emotions"],
        "correct_indices": [3],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "In healthcare, AI helps doctors to:",
        "options": [
            "Replace all operations",
            "Detect cancer earlier",
            "Eliminate all diseases",
            "Work less",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "C",
    },
    {
        "text": "A concern about technology mentioned is:",
        "options": [
            "It's too fast",
            "Privacy concerns",
            "It's too colorful",
            "It's too quiet",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "Social media can create:",
        "options": [
            "More friends",
            "Echo chambers",
            "New languages",
            "Physical products",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B2",
        "difficulty": "C",
    },
    {
        "text": "Renewable energy technology is helping address:",
        "options": ["Education", "Climate change", "Entertainment", "Sports"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "Quantum computing can solve problems that are:",
        "options": [
            "Easy",
            "Impossible for traditional computers",
            "Already solved",
            "Not important",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "C",
    },
    {
        "text": "The speaker's overall view of technology is:",
        "options": [
            "Completely negative",
            "Completely positive",
            "Balanced - benefits with mindfulness",
            "Indifferent",
        ],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "B2",
        "difficulty": "C",
    },
]


# ============================================================================
# MONOLOGUE 6: Health (monologue_health.wav)
# ============================================================================
LISTENING_HEALTH = [
    {
        "text": "Adults should sleep ___ hours per night.",
        "options": ["5-6", "7-9", "10-12", "4-5"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "To improve sleep, you should avoid ___ before bed.",
        "options": ["Water", "Food", "Screens", "Books"],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "A 30-minute walk can reduce the risk of:",
        "options": [
            "Only heart disease",
            "Heart disease, diabetes, and depression",
            "Nothing",
            "Accidents",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "The speaker says the best exercise is:",
        "options": [
            "Running marathons",
            "Lifting weights",
            "The one you will actually do",
            "Swimming only",
        ],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "Diet should include plenty of:",
        "options": [
            "Processed foods",
            "Sugary drinks",
            "Fruits, vegetables, whole grains",
            "Fast food",
        ],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "Stress management can include:",
        "options": [
            "Working more",
            "Deep breathing and meditation",
            "Watching more TV",
            "Sleeping less",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "Social relationships are linked to:",
        "options": [
            "More stress",
            "Happiness and longevity",
            "Financial success",
            "Career advancement",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "C",
    },
    {
        "text": "Regular health check-ups help to:",
        "options": [
            "Spend more money",
            "Catch problems early",
            "Avoid doctors",
            "Create more problems",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B2",
        "difficulty": "C",
    },
]


def seed_monologue_questions():
    """Add monologue listening questions to database."""
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

        all_questions = (
            LISTENING_LEADERS
            + LISTENING_FILMS
            + LISTENING_UNIVERSITY
            + LISTENING_KAZAKHSTAN
            + LISTENING_TECHNOLOGY
            + LISTENING_HEALTH
        )

        added = 0

        print(f"Adding {len(all_questions)} monologue listening questions...")

        for q_data in all_questions:
            q_id = str(uuid.uuid4())

            db_question = DBQuestion(
                id=q_id,
                subject_id=SubjectId.ENGLISH.value,
                text=q_data["text"],
                type=QuestionType.SINGLE,
                topic=q_data["topic"],
                difficulty=q_data.get("difficulty", "B"),
                language_level=q_data.get("language_level", "A2"),
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

        print(f"\n{'='*60}")
        print(f"[OK] Successfully added {added} questions!")
        print("=" * 60)
        print("\nBreakdown:")
        print(f"  - Leaders Monologue: {len(LISTENING_LEADERS)}")
        print(f"  - Films Review: {len(LISTENING_FILMS)}")
        print(f"  - University Life: {len(LISTENING_UNIVERSITY)}")
        print(f"  - Kazakhstan Culture: {len(LISTENING_KAZAKHSTAN)}")
        print(f"  - Technology: {len(LISTENING_TECHNOLOGY)}")
        print(f"  - Health: {len(LISTENING_HEALTH)}")

        # Show totals
        total_listening = (
            db.query(DBQuestion)
            .filter(
                DBQuestion.subject_id == SubjectId.ENGLISH.value,
                DBQuestion.topic.ilike("%listening%"),
            )
            .count()
        )

        print(f"\nTOTAL Listening Questions: {total_listening}")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    print("=" * 60)
    print("[AUDIO] Monologue Listening Questions Seeder")
    print("=" * 60)
    seed_monologue_questions()
