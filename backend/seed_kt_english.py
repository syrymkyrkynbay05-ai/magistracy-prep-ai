"""
КТ форматындағы English сұрақтарын мәліметтер базасына қосу скрипті.
Бұл скрипт seed_db.py-ге қосымша ретінде жұмыс істейді.

КТ құрылымы:
- 1-16: Тыңдалым (Listening) - topic: "listening"
- 17-34: Лексика-грамматика (Grammar) - topic: "grammar"
- 35-50: Оқылым (Reading) - topic: "reading" + reading_passage
"""

import os
import sys
import uuid

backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import DBSubject, DBQuestion, DBOption, SubjectId, QuestionType

# Reading passages for comprehension questions
READING_PASSAGE_1 = """Green Homes, Dream Homes

These days, more and more people want to help the Earth. Recycling and using eco-friendly shopping bags are small changes to our daily lives that can bring important benefits to the Earth.

Many people now choose to do even bigger things for the Earth. Some people choose to spend a little more money on their new homes in order to have a 'green' home. The green movement started about 40 years ago, and it is very big now. Using solar energy is a very popular way to have a 'green' home.

Builders of green homes think about many different ways to make a building more eco-friendly. Building materials are one of the biggest decisions. The United States uses 40 percent of all its raw materials on new buildings. Green builders also want to use materials that last a very long time.

Of course, location is also an important part of eco-construction. Homes need to be close to the things people need for their daily lives, or to public transportation. Homes also need to be in a place that doesn't hurt the environment around them. Green homes are designed to help the people living in them to recycle things, use less water, and minimize energy use easily.

Although building a green home is often more expensive than a regular home, most owners say it's a good idea. Most say that they are happy because their homes are more environmentally friendly, safer, cleaner, and better homes for their families."""

READING_PASSAGE_2 = """A MUSICAL BOOST

Is there a connection between music and language? According to recent studies, the answer is yes: music boosts certain language abilities in the brain. Here, we look at two examples.

Music and Hearing
A recent study by researcher Nina Kraus shows that playing a musical instrument can improve a person's hearing ability. As a part of the study, two groups of people listened to a person talking in a noisy room. The people in the first group were musicians, while those in the second group had no musical training. The musicians were able to hear the talking person more clearly.

Musicians hear better, says Kraus, because they learn to pay attention to certain sounds. Think about violinists in an orchestra. When the violinists play with the group, they hear their own instrument and many others too. But the violinists must listen closely to what they are playing, and ignore the other sounds. In this way, musicians are able to concentrate on certain sounds, even in a room with lots of noise.

Music and Speaking
Gottfried Schlaug, a doctor at Harvard Medical School, works with stroke patients. Because of their illness, these people cannot say their names, addresses, or other information normally. However, they can still sing. Dr. Schlaug was surprised to find that singing words helped his patients to eventually speak. Why does this work? Schlaug isn't sure. Music seems to activate different parts of the brain, including the damaged parts. This somehow helps patients to use that part of the brain again.

Understanding the Results
Music improves concentration, memory, listening skills, and our overall language abilities. It can even help sick people get better. Playing an instrument or singing, says Nina Kraus, can help us do better in school and keep our brain sharp as we get older. Music, she adds is not only enjoyable, it's also good for us in many other ways."""


# КТ форматындағы English сұрақтары
KT_ENGLISH_QUESTIONS = {
    # LISTENING QUESTIONS (1-16) - topic: "listening"
    "listening": [
        # Text 1: Akio Morita / Great Leaders (1-8)
        {
            "text": "Akio Morita did not succeed the first time when",
            "options": [
                "his company explained to sell its first product",
                "his company attempted to sell its first product",
                "his company turned to sell its first product",
                "his company decided to sell its first product",
            ],
            "correct_indices": [1],
            "topic": "listening",
        },
        {
            "text": "The great leaders",
            "options": [
                "should have the same profession",
                "have to work in the same sphere",
                "may be different people",
                "should have the same major",
            ],
            "correct_indices": [2],
            "topic": "listening",
        },
        {
            "text": "Many top companies have rules that",
            "options": [
                "destroy open communication",
                "borrow open communication",
                "support open communication",
                "lend open communication",
            ],
            "correct_indices": [2],
            "topic": "listening",
        },
        {
            "text": "When great leaders face difficulty",
            "options": [
                "they worry a lot",
                "they are afraid of it",
                "they run away",
                "they do not panic",
            ],
            "correct_indices": [3],
            "topic": "listening",
        },
        {
            "text": "Great leaders have a goal in mind and do",
            "options": [
                "what they need to discover it",
                "what they need to research it",
                "what they need to accomplish it",
                "what they need to scrutinize it",
            ],
            "correct_indices": [2],
            "topic": "listening",
        },
        {
            "text": "But this did not stop Morita as he",
            "options": [
                "preferred to create a multi-billion-dollar company!",
                "continued to create a multi-billion-dollar company!",
                "wanted to create a multi-billion-dollar company!",
                "planned to create a multi-billion-dollar company!",
            ],
            "correct_indices": [1],
            "topic": "listening",
        },
        {
            "text": "According to the text great leaders'",
            "options": [
                "parents are usually rich",
                "negative features outweigh the positive ones",
                "communication skills are their weaknesses",
                "positive features outweigh the negative ones",
            ],
            "correct_indices": [3],
            "topic": "listening",
        },
        {
            "text": "According to the text great leaders have",
            "options": [
                "negative personality",
                "positive personality",
                "negative qualities outweigh the positive ones",
                "negative qualities",
            ],
            "correct_indices": [1],
            "topic": "listening",
        },
        # Text 2: Film Reviews (9-16)
        {
            "text": "In which film did Jennifer Peckory play a manager?",
            "options": ['"Call"', '"Swim"', '"Jennifer Peckory"', '"Jungle Fever"'],
            "correct_indices": [0],
            "topic": "listening",
        },
        {
            "text": 'What skill does the main character in "Swim" want to learn?',
            "options": ["training tigers", "cooking", "being a friend", "swimming"],
            "correct_indices": [3],
            "topic": "listening",
        },
        {
            "text": "What is the first film that is reviewed?",
            "options": ["Jungle", "Swim", "Call", "Jungle Fever"],
            "correct_indices": [3],
            "topic": "listening",
        },
        {
            "text": "Which film tells us a love story?",
            "options": ['"Call"', '"Jennifer Peckory"', '"Swim"', '"Jungle Fever"'],
            "correct_indices": [0],
            "topic": "listening",
        },
        {
            "text": 'Where does the chef in "Call" work?',
            "options": [
                "in the zoo",
                "in a swimming pool",
                "an Italian pizza takeaway",
                "in the jungle",
            ],
            "correct_indices": [2],
            "topic": "listening",
        },
        {
            "text": "What films are reviewed in the program?",
            "options": [
                "films about animals",
                "new films",
                "old films",
                "classical films",
            ],
            "correct_indices": [1],
            "topic": "listening",
        },
        {
            "text": 'How old is the character of "Swim"?',
            "options": ["22", "20", "12", "25"],
            "correct_indices": [2],
            "topic": "listening",
        },
        {
            "text": "What film did Steve Wills take part in?",
            "options": ['"Swim"', '"Jennifer Peckory"', '"Call"', '"Jungle Fever"'],
            "correct_indices": [2],
            "topic": "listening",
        },
    ],
    # GRAMMAR/VOCABULARY QUESTIONS (17-34) - topic: "grammar"
    "grammar": [
        {
            "text": "Money can't buy you ____ happiness.",
            "options": ["the", "some", "any", "-"],
            "correct_indices": [3],
            "topic": "grammar",
        },
        {
            "text": "He could read for _ hours.",
            "options": ["an", "-", "a", "the"],
            "correct_indices": [1],
            "topic": "grammar",
        },
        {
            "text": "He'll need to be able to run .........than this if he's going to do the competition.",
            "options": ["farther", "more far", "far", "less far"],
            "correct_indices": [0],
            "topic": "grammar",
        },
        {
            "text": "Marat works very hard. It's not _ that he's always tired.",
            "options": ["surprise", "surprising", "surprised", "surprissed"],
            "correct_indices": [1],
            "topic": "grammar",
        },
        {
            "text": "We went shopping and spent _ money.",
            "options": ["many", "a lot of", "a lot", "lots"],
            "correct_indices": [1],
            "topic": "grammar",
        },
        {
            "text": "Which unit is still often used in Britain to talk about distance despite the metric system?",
            "options": ["centimeters", "kilometres", "metres", "miles"],
            "correct_indices": [3],
            "topic": "grammar",
        },
        {
            "text": "I ________ home when I met Daniel. He looked sad. Maybe, he was sick.",
            "options": ["walked", "had walked", "was walking", "to walk"],
            "correct_indices": [2],
            "topic": "grammar",
        },
        {
            "text": "I will return your book ___.",
            "options": [
                "on two weeks",
                "in two weeks",
                "to two weeks",
                "about two weeks",
            ],
            "correct_indices": [1],
            "topic": "grammar",
        },
        {
            "text": "I've just started to learn how to drive. Now I _ how difficult it is.",
            "options": ["am knowing", "knowing", "know", "knew"],
            "correct_indices": [2],
            "topic": "grammar",
        },
        {
            "text": "I ____by a loud noise at night.",
            "options": ["woke up", "was woken up", "were woken up", "was woke"],
            "correct_indices": [1],
            "topic": "grammar",
        },
        {
            "text": "Our company .... significantly over the past year.",
            "options": ["has grown", "was grown", "grown", "grow"],
            "correct_indices": [0],
            "topic": "grammar",
        },
        {
            "text": "_ the music awards live tomorrow nights?",
            "options": [
                "Are they gone to broadcast",
                "Are they going broadcast",
                "Are they go to broadcast",
                "Are they going to broadcast",
            ],
            "correct_indices": [3],
            "topic": "grammar",
        },
        {
            "text": "At the time the company closed down I ____ there for several years.",
            "options": [
                "had been working",
                "have had working",
                "was been working",
                "was working",
            ],
            "correct_indices": [0],
            "topic": "grammar",
        },
        {
            "text": ".... I have a look at that bag in the window, please.",
            "options": ["could", "must", "need", "should"],
            "correct_indices": [0],
            "topic": "grammar",
        },
        {
            "text": "The company is expected ... a healthy profit this year.",
            "options": ["to make", "make", "for making", "making"],
            "correct_indices": [0],
            "topic": "grammar",
        },
        {
            "text": "On _ home, I found my daughter waiting outside her front door.",
            "options": ["returning", "returns", "return", "to return"],
            "correct_indices": [0],
            "topic": "grammar",
        },
        {
            "text": "If you ... too much fast food, it's not good for your health.",
            "options": ["eat", "would eat", "are eaten", "eating"],
            "correct_indices": [0],
            "topic": "grammar",
        },
        {
            "text": "What if your cat suddenly ... to you right now? How would you react?",
            "options": [
                "started talking",
                "had started talking",
                "start talking",
                "starting to talk",
            ],
            "correct_indices": [0],
            "topic": "grammar",
        },
    ],
    # READING QUESTIONS (35-50) - topic: "reading" with reading_passage
    "reading": [
        # Text 1: Green Homes (35-42)
        {
            "text": "Popular way of having a green home is using",
            "options": [
                "energy from the earth",
                "energy from the sun",
                "energy from the wind",
                "energy from the sky",
            ],
            "correct_indices": [1],
            "topic": "reading",
            "reading_passage": READING_PASSAGE_1,
        },
        {
            "text": "There are many volunteers who show their _____ to make a contribution to the Earth's protection.",
            "options": ["difference", "hatred", "opinion", "desire"],
            "correct_indices": [3],
            "topic": "reading",
            "reading_passage": READING_PASSAGE_1,
        },
        {
            "text": "The quality of green homes depends on",
            "options": [
                "cheap raw materials",
                "up-to-date building materials",
                "regular building materials",
                "long-lasting building materials",
            ],
            "correct_indices": [3],
            "topic": "reading",
            "reading_passage": READING_PASSAGE_1,
        },
        {
            "text": "According to the text, eco-friendly way of life is",
            "options": [
                "not affordable for the population",
                "less popular among population",
                "a future plan of the state",
                "approved by the majority",
            ],
            "correct_indices": [3],
            "topic": "reading",
            "reading_passage": READING_PASSAGE_1,
        },
        {
            "text": "Building a regular home is often",
            "options": [
                "more expensive than building green home",
                "much more expensive than building green home",
                "cheaper than building green home",
                "more reasonable than building green home",
            ],
            "correct_indices": [2],
            "topic": "reading",
            "reading_passage": READING_PASSAGE_1,
        },
        {
            "text": "If people need to build eco-friendly houses",
            "options": [
                "it is not efficient for the economy of a country",
                "it is good for the Earth",
                "it is cheap",
                "it is good for homeless people",
            ],
            "correct_indices": [1],
            "topic": "reading",
            "reading_passage": READING_PASSAGE_1,
        },
        {
            "text": "These days people use",
            "options": [
                "eco-friendly shopping bags a lot",
                "paper shopping bags a lot",
                "modern shopping bags a lot",
                "plastic shopping bags a lot",
            ],
            "correct_indices": [0],
            "topic": "reading",
            "reading_passage": READING_PASSAGE_1,
        },
        {
            "text": "The green movement",
            "options": [
                "started many years ago",
                "started several years ago",
                "has lasted for a decade",
                "has started recently",
            ],
            "correct_indices": [0],
            "topic": "reading",
            "reading_passage": READING_PASSAGE_1,
        },
        # Text 2: A Musical Boost (43-50)
        {
            "text": "Music improves:",
            "options": [
                "reading skills in the brain",
                "writing skills in the brain",
                "hearing abilities in the brain",
                "language abilities in the brain",
            ],
            "correct_indices": [3],
            "topic": "reading",
            "reading_passage": READING_PASSAGE_2,
        },
        {
            "text": "The text is about:",
            "options": [
                "a connection between music and language abilities",
                "playing different types of musical instruments",
                "different instruments and musicians",
                "brain functioning and different types of patients",
            ],
            "correct_indices": [0],
            "topic": "reading",
            "reading_passage": READING_PASSAGE_2,
        },
        {
            "text": "According to the researcher Nina Kraus playing a musical instrument:",
            "options": [
                "can boost a person's hearing ability",
                "can boost a person's dancing skills",
                "can boost a person's ability to talk in a noisy room",
                "can boost a person's writing skills",
            ],
            "correct_indices": [0],
            "topic": "reading",
            "reading_passage": READING_PASSAGE_2,
        },
        {
            "text": "The synonym of improve is",
            "options": ["roast", "boost", "toast", "goast"],
            "correct_indices": [1],
            "topic": "reading",
            "reading_passage": READING_PASSAGE_2,
        },
        {
            "text": "The reason why musicians can hear better is",
            "options": [
                "that they are trained to pay attention to particular sounds",
                "that they are trained to sing and play different instruments",
                "that they hear their own instruments and many others",
                "that they use certain language abilities in the brain",
            ],
            "correct_indices": [0],
            "topic": "reading",
            "reading_passage": READING_PASSAGE_2,
        },
        {
            "text": "Find the true statement",
            "options": [
                "Nina Kraus plays in an orchestra",
                "Nina Kraus is a violinist",
                "Nina Kraus is a graduate of Harvard University",
                "Nina Kraus is a researcher",
            ],
            "correct_indices": [3],
            "topic": "reading",
            "reading_passage": READING_PASSAGE_2,
        },
        {
            "text": "Music helps people to improve",
            "options": [
                "reading, speaking and dancing",
                "sleeping, swimming and walking",
                "memory, listening and concentration",
                "writing, listening and painting",
            ],
            "correct_indices": [2],
            "topic": "reading",
            "reading_passage": READING_PASSAGE_2,
        },
        {
            "text": "The synonym of to ignore:",
            "options": [
                "to stay for",
                "to look for",
                "to vote for",
                "to pay no attention to",
            ],
            "correct_indices": [3],
            "topic": "reading",
            "reading_passage": READING_PASSAGE_2,
        },
    ],
}


def seed_kt_english_questions():
    """Add КТ format English questions to database"""
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

        added_count = 0

        for category, questions in KT_ENGLISH_QUESTIONS.items():
            print(f"Adding {len(questions)} {category} questions...")

            for q_data in questions:
                q_id = str(uuid.uuid4())

                # Create question
                db_question = DBQuestion(
                    id=q_id,
                    subject_id=SubjectId.ENGLISH.value,
                    text=q_data["text"],
                    type=QuestionType.SINGLE,
                    topic=q_data["topic"],
                    difficulty="medium",
                    reading_passage=q_data.get("reading_passage"),
                )
                db.add(db_question)

                # Create options
                correct_ids = []
                for idx, opt_text in enumerate(q_data["options"]):
                    opt_id = str(uuid.uuid4())
                    db_option = DBOption(id=opt_id, question_id=q_id, text=opt_text)
                    db.add(db_option)

                    if idx in q_data["correct_indices"]:
                        correct_ids.append(opt_id)

                db_question.correct_option_ids = ",".join(correct_ids)
                added_count += 1

        db.commit()
        print(f"\nSuccessfully added {added_count} КТ format English questions!")
        print("- 16 Listening questions")
        print("- 18 Grammar questions")
        print("- 16 Reading questions (with passages)")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    print("=" * 50)
    print("КТ English Questions Seeder")
    print("=" * 50)
    seed_kt_english_questions()
