"""
Спецификация бойынша қосымша English сұрақтары.
Тақырыптар:
1. Noun (singular/plural, countable/uncountable, possessive)
2. Numeral (cardinal, ordinal, fractional)
3. Adverb (formation, place)
4. Mood (indicative, imperative, subjunctive)
5. Lexicology (synonyms, antonyms, collocations)
6. Reading: Қазақстан, ағылшын тілді елдер, ғылым
"""

import os
import sys
import uuid

backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from sqlalchemy.orm import Session
from database import SessionLocal
from models import DBSubject, DBQuestion, DBOption, SubjectId, QuestionType


# New Reading Passages based on specification topics
READING_KAZAKHSTAN = """KAZAKHSTAN: A LAND OF OPPORTUNITIES

Kazakhstan is the largest landlocked country in the world and the ninth largest country overall. Located in Central Asia, it borders Russia to the north, China to the east, and several other Central Asian nations to the south.

The country has experienced remarkable economic growth since gaining independence in 1991. Rich in natural resources, Kazakhstan has become one of the world's leading producers of uranium, chromium, and petroleum. The capital city, Astana (now Nur-Sultan), was moved from Almaty in 1997 and has been transformed into a modern metropolis with stunning architecture.

Kazakhstan is home to diverse ethnic groups and cultures, with Kazakhs making up the majority of the population. The country has successfully maintained peaceful relations among its various ethnic communities. Russian and Kazakh are both widely spoken, and English is increasingly important for business and education.

The education system has undergone significant reforms, with many students choosing to study abroad or at international universities within Kazakhstan. The Bolashak scholarship program has sent thousands of students to study in top universities worldwide, contributing to the country's human capital development."""

READING_BRITAIN = """UNITED KINGDOM: TRADITION MEETS MODERNITY

The United Kingdom, comprising England, Scotland, Wales, and Northern Ireland, is a constitutional monarchy with a rich history spanning over a thousand years. Despite its relatively small size, the UK has had an enormous influence on world culture, politics, and economics.

The British education system is renowned worldwide. Universities like Oxford and Cambridge have been centers of learning for centuries, while newer institutions continue to attract students from around the globe. The UK's higher education system emphasizes independent thinking and research skills.

British culture is a fascinating blend of tradition and modernity. From the changing of the guard at Buckingham Palace to cutting-edge theater in London's West End, the country offers diverse experiences. The pub culture, afternoon tea, and love of sports like football and cricket remain central to British life.

The UK has been a leader in science and innovation. British scientists have made groundbreaking discoveries in physics, medicine, and technology. From Isaac Newton to Stephen Hawking, British thinkers have shaped our understanding of the universe."""

READING_SCIENCE = """THE DIGITAL REVOLUTION IN EDUCATION

Technology is transforming how we learn and teach. Online learning platforms, virtual classrooms, and educational apps have made education more accessible than ever before. Students can now access world-class courses from anywhere with an internet connection.

Artificial intelligence is beginning to personalize learning experiences. AI tutors can adapt to individual student needs, providing customized exercises and feedback. This technology helps identify learning gaps and suggests targeted improvements, making education more efficient and effective.

However, the digital revolution also presents challenges. The digital divide means that not everyone has equal access to technology and high-speed internet. There are concerns about screen time, online safety, and the loss of face-to-face interaction in education. Teachers must learn new skills to effectively integrate technology into their teaching.

Despite these challenges, experts believe that technology will continue to play an increasingly important role in education. The most successful approaches will likely combine the best of traditional teaching methods with innovative digital tools, creating hybrid learning environments that prepare students for the modern workforce."""


# Noun questions (A1-B1)
NOUN_QUESTIONS = [
    {
        "text": "Choose the correct plural form: child → ___",
        "options": ["childs", "childes", "children", "childern"],
        "correct_indices": [2],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "Which noun is uncountable?",
        "options": ["apple", "information", "book", "student"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "Choose the correct possessive form: The ___ toys are on the floor.",
        "options": ["childrens", "children's", "childrens'", "children"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "Which is the correct plural? tooth → ___",
        "options": ["tooths", "teeth", "toothes", "teeths"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "___ is a very important subject.",
        "options": [
            "The mathematics",
            "Mathematics",
            "A mathematics",
            "Some mathematics",
        ],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "Choose the correct form: I need ___ for my research.",
        "options": [
            "an information",
            "informations",
            "some information",
            "the informations",
        ],
        "correct_indices": [2],
        "topic": "grammar",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "The ___ meeting is scheduled for Monday.",
        "options": ["managers", "managers'", "manager's", "manager"],
        "correct_indices": [2],
        "topic": "grammar",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "Which sentence is correct?",
        "options": [
            "The news are good today.",
            "The news is good today.",
            "The new are good today.",
            "The news be good today.",
        ],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "B1",
        "difficulty": "C",
    },
]

# Numeral questions (A1-A2)
NUMERAL_QUESTIONS = [
    {
        "text": "Choose the correct ordinal number: 21 → ___",
        "options": ["twenty-first", "twenty-one", "the twenty-one", "twenty-oneth"],
        "correct_indices": [0],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "How do you read this date: 15/03/2024?",
        "options": [
            "The fifteen of March",
            "Fifteen March",
            "The fifteenth of March",
            "March the fifteen",
        ],
        "correct_indices": [2],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "B",
    },
    {
        "text": "Choose the correct form: ___",
        "options": ["two-thirds", "two-third", "two thirds", "twos third"],
        "correct_indices": [0],
        "topic": "grammar",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "She finished ___ in the race.",
        "options": ["three", "the three", "third", "the third"],
        "correct_indices": [2],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "The meeting is on ___ of July.",
        "options": ["the four", "fourth", "the fourth", "four"],
        "correct_indices": [2],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "B",
    },
    {
        "text": "Write the number: 1,500,000",
        "options": [
            "one million five hundred thousand",
            "fifteen hundred thousand",
            "one and half million",
            "one million and five hundred",
        ],
        "correct_indices": [0],
        "topic": "grammar",
        "language_level": "A2",
        "difficulty": "C",
    },
]

# Adverb questions (A1-B2)
ADVERB_QUESTIONS = [
    {
        "text": "Form an adverb from 'quick':",
        "options": ["quicky", "quickly", "quickful", "quicken"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "Choose the correct word order: She ___ reads books.",
        "options": ["always", "reads always", "always she", "she always"],
        "correct_indices": [0],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "B",
    },
    {
        "text": "He speaks English ___.",
        "options": ["good", "well", "goodly", "goods"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "I ___ go to the gym on Mondays.",
        "options": ["usual", "usually", "usualy", "in usual"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "She sings ___. (beautiful)",
        "options": ["beautiful", "beautifully", "more beautiful", "beautifuler"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "___ have I seen such a beautiful sunset.",
        "options": ["Never", "Ever", "Always", "Usually"],
        "correct_indices": [0],
        "topic": "grammar",
        "language_level": "B2",
        "difficulty": "C",
    },
    {
        "text": "The adverb in 'He runs very fast' is:",
        "options": ["runs", "He", "fast", "very"],
        "correct_indices": [2],
        "topic": "grammar",
        "language_level": "B1",
        "difficulty": "B",
    },
]

# Mood questions - Conditionals, Imperative (A2-B2)
MOOD_QUESTIONS = [
    {
        "text": "Complete: If I ___ you, I would apologize.",
        "options": ["am", "was", "were", "be"],
        "correct_indices": [2],
        "topic": "grammar",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "Choose the imperative: ___",
        "options": [
            "You close the door.",
            "Close the door!",
            "The door closes.",
            "Closing the door.",
        ],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "If she ___ harder, she would have passed.",
        "options": ["studied", "had studied", "studies", "would study"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "B2",
        "difficulty": "C",
    },
    {
        "text": "I wish I ___ taller.",
        "options": ["am", "was", "were", "be"],
        "correct_indices": [2],
        "topic": "grammar",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "___ quiet during the exam!",
        "options": ["Be", "Being", "Been", "To be"],
        "correct_indices": [0],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "If only I ___ more time to study!",
        "options": ["have", "had", "having", "would have"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "B2",
        "difficulty": "C",
    },
    {
        "text": "It's essential that he ___ on time.",
        "options": ["arrives", "arrive", "arrived", "arriving"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "B2",
        "difficulty": "C",
    },
]

# Lexicology - Synonyms, Antonyms, Collocations (A1-B2)
LEXICOLOGY_QUESTIONS = [
    {
        "text": "Choose the synonym of 'happy':",
        "options": ["sad", "angry", "joyful", "tired"],
        "correct_indices": [2],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "Choose the antonym of 'ancient':",
        "options": ["old", "modern", "historic", "traditional"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "Complete the collocation: make a ___",
        "options": ["homework", "mistake", "sport", "exam"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "Choose the synonym of 'significant':",
        "options": ["small", "important", "minor", "trivial"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "Complete: take ___ of something",
        "options": ["care", "a care", "caring", "cared"],
        "correct_indices": [0],
        "topic": "grammar",
        "language_level": "A2",
        "difficulty": "A",
    },
    {
        "text": "The antonym of 'optimistic' is:",
        "options": ["hopeful", "pessimistic", "positive", "cheerful"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "Complete: heavy ___",
        "options": ["rain", "sun", "wind", "cloud"],
        "correct_indices": [0],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "'Commence' is a formal synonym for:",
        "options": ["finish", "continue", "begin", "stop"],
        "correct_indices": [2],
        "topic": "grammar",
        "language_level": "B2",
        "difficulty": "C",
    },
]

# Reading - Kazakhstan
READING_KZ_QUESTIONS = [
    {
        "text": "Kazakhstan is the ___ largest country in the world.",
        "options": ["largest", "fifth largest", "ninth largest", "second largest"],
        "correct_indices": [2],
        "topic": "reading",
        "language_level": "A1",
        "difficulty": "A",
        "reading_passage": READING_KAZAKHSTAN,
    },
    {
        "text": "Kazakhstan gained independence in:",
        "options": ["1990", "1991", "1997", "2000"],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "A1",
        "difficulty": "A",
        "reading_passage": READING_KAZAKHSTAN,
    },
    {
        "text": "The capital was moved from Almaty in:",
        "options": ["1991", "1995", "1997", "2000"],
        "correct_indices": [2],
        "topic": "reading",
        "language_level": "A2",
        "difficulty": "B",
        "reading_passage": READING_KAZAKHSTAN,
    },
    {
        "text": "Kazakhstan is a leading producer of:",
        "options": [
            "gold and silver",
            "uranium and petroleum",
            "copper and zinc",
            "iron and aluminum",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "A2",
        "difficulty": "B",
        "reading_passage": READING_KAZAKHSTAN,
    },
    {
        "text": "The Bolashak program is for:",
        "options": ["tourism", "studying abroad", "sports", "healthcare"],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "B1",
        "difficulty": "B",
        "reading_passage": READING_KAZAKHSTAN,
    },
    {
        "text": "'Landlocked' means:",
        "options": [
            "surrounded by mountains",
            "having no sea coast",
            "locked by land laws",
            "having many lakes",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "B1",
        "difficulty": "C",
        "reading_passage": READING_KAZAKHSTAN,
    },
    {
        "text": "According to the text, which languages are widely spoken?",
        "options": [
            "Only Kazakh",
            "Russian and Kazakh",
            "English and Kazakh",
            "Russian only",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "A2",
        "difficulty": "B",
        "reading_passage": READING_KAZAKHSTAN,
    },
    {
        "text": "The main idea of the text is:",
        "options": [
            "Kazakhstan's geography",
            "Kazakhstan's development and opportunities",
            "Kazakhstan's problems",
            "Kazakhstan's history only",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "B2",
        "difficulty": "C",
        "reading_passage": READING_KAZAKHSTAN,
    },
]

# Reading - UK
READING_UK_QUESTIONS = [
    {
        "text": "The UK consists of:",
        "options": [
            "Two countries",
            "Three countries",
            "Four countries",
            "Five countries",
        ],
        "correct_indices": [2],
        "topic": "reading",
        "language_level": "A1",
        "difficulty": "A",
        "reading_passage": READING_BRITAIN,
    },
    {
        "text": "Oxford and Cambridge are mentioned as:",
        "options": ["Cities", "Universities", "Museums", "Sports clubs"],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "A1",
        "difficulty": "A",
        "reading_passage": READING_BRITAIN,
    },
    {
        "text": "Which is NOT mentioned as central to British life?",
        "options": ["Pub culture", "Afternoon tea", "Baseball", "Football"],
        "correct_indices": [2],
        "topic": "reading",
        "language_level": "A2",
        "difficulty": "B",
        "reading_passage": READING_BRITAIN,
    },
    {
        "text": "The UK's political system is:",
        "options": [
            "A republic",
            "A constitutional monarchy",
            "A democracy only",
            "A federation",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "A2",
        "difficulty": "B",
        "reading_passage": READING_BRITAIN,
    },
    {
        "text": "British scientists mentioned include:",
        "options": [
            "Einstein and Galileo",
            "Newton and Hawking",
            "Darwin and Curie",
            "Edison and Tesla",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "B1",
        "difficulty": "B",
        "reading_passage": READING_BRITAIN,
    },
    {
        "text": "The British education system emphasizes:",
        "options": [
            "Memorization",
            "Independent thinking and research",
            "Group work only",
            "Practical skills only",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "B1",
        "difficulty": "C",
        "reading_passage": READING_BRITAIN,
    },
    {
        "text": "'Renowned' in the text means:",
        "options": ["New", "Famous", "Old", "Local"],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "B2",
        "difficulty": "C",
        "reading_passage": READING_BRITAIN,
    },
    {
        "text": "The author's attitude toward the UK is:",
        "options": ["Critical", "Neutral", "Positive", "Negative"],
        "correct_indices": [2],
        "topic": "reading",
        "language_level": "B2",
        "difficulty": "C",
        "reading_passage": READING_BRITAIN,
    },
]

# Reading - Science/Education
READING_SCIENCE_QUESTIONS = [
    {
        "text": "What is transforming education according to the text?",
        "options": ["Teachers", "Technology", "Books", "Parents"],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "A1",
        "difficulty": "A",
        "reading_passage": READING_SCIENCE,
    },
    {
        "text": "AI tutors can:",
        "options": [
            "Replace teachers completely",
            "Adapt to individual student needs",
            "Only teach mathematics",
            "Work without internet",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "A2",
        "difficulty": "B",
        "reading_passage": READING_SCIENCE,
    },
    {
        "text": "'Digital divide' refers to:",
        "options": [
            "Different types of computers",
            "Unequal access to technology",
            "Digital calculations",
            "Online games",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "B1",
        "difficulty": "C",
        "reading_passage": READING_SCIENCE,
    },
    {
        "text": "Which challenge is NOT mentioned?",
        "options": [
            "Screen time",
            "Online safety",
            "High costs",
            "Loss of face-to-face interaction",
        ],
        "correct_indices": [2],
        "topic": "reading",
        "language_level": "B1",
        "difficulty": "B",
        "reading_passage": READING_SCIENCE,
    },
    {
        "text": "'Hybrid learning' combines:",
        "options": [
            "Two languages",
            "Traditional and digital methods",
            "Different subjects",
            "Multiple teachers",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "B2",
        "difficulty": "C",
        "reading_passage": READING_SCIENCE,
    },
    {
        "text": "The text suggests that technology in education:",
        "options": [
            "Is completely negative",
            "Should be avoided",
            "Will grow but has challenges",
            "Is only for rich countries",
        ],
        "correct_indices": [2],
        "topic": "reading",
        "language_level": "B1",
        "difficulty": "B",
        "reading_passage": READING_SCIENCE,
    },
    {
        "text": "What must teachers learn?",
        "options": [
            "New languages",
            "New technology skills",
            "New subjects",
            "New sports",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "A2",
        "difficulty": "B",
        "reading_passage": READING_SCIENCE,
    },
    {
        "text": "The purpose of the text is to:",
        "options": [
            "Criticize technology",
            "Advertise educational apps",
            "Discuss technology's role in education",
            "Compare different countries",
        ],
        "correct_indices": [2],
        "topic": "reading",
        "language_level": "B2",
        "difficulty": "C",
        "reading_passage": READING_SCIENCE,
    },
]


def seed_specification_questions():
    """Add questions based on specification topics"""
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
            NOUN_QUESTIONS
            + NUMERAL_QUESTIONS
            + ADVERB_QUESTIONS
            + MOOD_QUESTIONS
            + LEXICOLOGY_QUESTIONS
            + READING_KZ_QUESTIONS
            + READING_UK_QUESTIONS
            + READING_SCIENCE_QUESTIONS
        )

        added = 0

        print(f"Adding {len(all_questions)} new questions...")

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
                reading_passage=q_data.get("reading_passage"),
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

        print(f"\n{'='*50}")
        print(f"Successfully added {added} questions!")
        print("=" * 50)
        print("\nBreakdown:")
        print(f"  - Noun: {len(NOUN_QUESTIONS)}")
        print(f"  - Numeral: {len(NUMERAL_QUESTIONS)}")
        print(f"  - Adverb: {len(ADVERB_QUESTIONS)}")
        print(f"  - Mood: {len(MOOD_QUESTIONS)}")
        print(f"  - Lexicology: {len(LEXICOLOGY_QUESTIONS)}")
        print(f"  - Reading (Kazakhstan): {len(READING_KZ_QUESTIONS)}")
        print(f"  - Reading (UK): {len(READING_UK_QUESTIONS)}")
        print(f"  - Reading (Science): {len(READING_SCIENCE_QUESTIONS)}")

        # Show totals
        total_grammar = (
            db.query(DBQuestion)
            .filter(
                DBQuestion.subject_id == SubjectId.ENGLISH.value,
                DBQuestion.topic.ilike("%grammar%"),
            )
            .count()
        )

        total_reading = (
            db.query(DBQuestion)
            .filter(
                DBQuestion.subject_id == SubjectId.ENGLISH.value,
                DBQuestion.topic.ilike("%reading%"),
            )
            .count()
        )

        print(f"\n📊 TOTAL English Questions:")
        print(f"  - Grammar: {total_grammar}")
        print(f"  - Reading: {total_reading}")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    print("=" * 50)
    print("Specification-based Questions Seeder")
    print("=" * 50)
    seed_specification_questions()
