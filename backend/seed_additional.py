"""
Қосымша Grammar және Reading сұрақтары.
Бұл скрипт бар сұрақтарға қосымша ретінде жұмыс істейді.
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


# Additional Reading Passages
READING_PASSAGE_3 = """THE FUTURE OF TRANSPORTATION

Self-driving cars are no longer science fiction. Major technology companies and car manufacturers are racing to develop autonomous vehicles that can navigate roads without human input. These vehicles use a combination of sensors, cameras, and artificial intelligence to detect obstacles, read traffic signs, and make driving decisions.

Proponents argue that self-driving cars will make roads safer by eliminating human error, which causes over 90% of accidents. They also promise to reduce traffic congestion through more efficient driving patterns and could provide mobility to elderly and disabled individuals who cannot drive.

However, there are significant challenges. Technical issues remain, including the ability to handle unpredictable situations like construction zones or severe weather. There are also ethical questions about how vehicles should make decisions in unavoidable accident scenarios. Additionally, the widespread adoption of autonomous vehicles could lead to job losses for millions of professional drivers.

Despite these concerns, experts predict that self-driving cars will become common within the next decade. Several cities are already testing autonomous taxi services, and some highways allow limited use of self-driving features. The transportation revolution is coming, whether we're ready or not."""

READING_PASSAGE_4 = """SOCIAL MEDIA AND MENTAL HEALTH

Social media platforms have transformed how we communicate, share information, and connect with others. With billions of users worldwide, platforms like Facebook, Instagram, and TikTok have become integral parts of daily life, especially for younger generations.

Research suggests a complex relationship between social media use and mental health. On one hand, these platforms can provide valuable social connections, community support, and access to information. They allow people to maintain relationships across distances and find others with similar interests.

On the other hand, studies have linked heavy social media use to increased rates of anxiety, depression, and loneliness, particularly among teenagers. The constant comparison to others' carefully curated posts can lead to feelings of inadequacy. Cyberbullying remains a serious problem, and the addictive design of these platforms can disrupt sleep and reduce face-to-face interactions.

Experts recommend a balanced approach. Setting time limits, being mindful of how social media affects your mood, and prioritizing in-person relationships can help maximize benefits while minimizing harm. Some schools have begun teaching digital literacy to help students navigate social media more healthily."""

READING_PASSAGE_5 = """CLIMATE CHANGE AND GLOBAL ACTION

Climate change is one of the most pressing challenges facing humanity. Rising global temperatures are causing more frequent extreme weather events, melting ice caps, rising sea levels, and disrupting ecosystems worldwide. Scientists agree that human activities, particularly the burning of fossil fuels, are the primary cause.

International efforts to address climate change have increased in recent years. The Paris Agreement, signed by nearly 200 countries, aims to limit global warming to 1.5 degrees Celsius above pre-industrial levels. Many nations have committed to achieving net-zero carbon emissions by 2050.

Renewable energy sources like solar and wind power are becoming increasingly cost-competitive with fossil fuels. Electric vehicles are gaining market share, and new technologies for carbon capture are being developed. However, progress has been uneven, and current commitments are still insufficient to meet climate goals.

Individual actions also matter. Reducing energy consumption, eating less meat, using public transportation, and supporting sustainable businesses can make a difference. While systemic changes are necessary, collective individual actions can help drive the transition to a more sustainable future."""

READING_PASSAGE_6 = """THE DIGITAL WORKPLACE

The COVID-19 pandemic accelerated a trend that was already underway: the shift to remote work. Millions of employees around the world suddenly found themselves working from home, using video conferencing tools and collaboration software to stay connected with colleagues.

For many workers, remote work has been a revelation. Eliminating commutes saves time and reduces stress. Flexible schedules allow better work-life balance. Workers report higher productivity and satisfaction when they can control their environment and minimize interruptions.

However, remote work also presents challenges. The lack of face-to-face interaction can lead to feelings of isolation and disconnect from company culture. Communication can be more difficult, and the boundaries between work and personal life can blur when your office is your home. Some tasks require in-person collaboration that video calls cannot fully replicate.

Many organizations are now adopting hybrid models that combine remote and in-office work. This approach aims to capture the benefits of flexibility while maintaining opportunities for in-person connection and collaboration. The future of work is likely to be more flexible and varied than ever before."""


# Қосымша Grammar сұрақтары
ADDITIONAL_GRAMMAR_QUESTIONS = [
    # Articles
    {
        "text": "I saw ___ interesting movie last night.",
        "options": ["a", "an", "the", "-"],
        "correct_indices": [1],
        "topic": "grammar",
    },
    {
        "text": "___ water in this bottle is very cold.",
        "options": ["A", "An", "The", "-"],
        "correct_indices": [2],
        "topic": "grammar",
    },
    {
        "text": "She wants to become ___ engineer.",
        "options": ["a", "an", "the", "-"],
        "correct_indices": [1],
        "topic": "grammar",
    },
    {
        "text": "We visited ___ Eiffel Tower in Paris.",
        "options": ["a", "an", "the", "-"],
        "correct_indices": [2],
        "topic": "grammar",
    },
    # Tenses
    {
        "text": "By this time next year, I ___ my degree.",
        "options": ["will finish", "will have finished", "finish", "have finished"],
        "correct_indices": [1],
        "topic": "grammar",
    },
    {
        "text": "She ___ English for five years before she moved to London.",
        "options": ["studied", "had studied", "has studied", "was studying"],
        "correct_indices": [1],
        "topic": "grammar",
    },
    {
        "text": "Look! The children ___ in the garden.",
        "options": ["play", "plays", "are playing", "played"],
        "correct_indices": [2],
        "topic": "grammar",
    },
    {
        "text": "I ___ never ___ to Japan, but I'd love to go.",
        "options": ["have/been", "had/been", "was/been", "am/being"],
        "correct_indices": [0],
        "topic": "grammar",
    },
    {
        "text": "When I called, she ___ dinner.",
        "options": ["cooks", "cooked", "was cooking", "has cooked"],
        "correct_indices": [2],
        "topic": "grammar",
    },
    {
        "text": "The train ___ at 9 o'clock every morning.",
        "options": ["leave", "leaves", "is leaving", "left"],
        "correct_indices": [1],
        "topic": "grammar",
    },
    # Modal verbs
    {
        "text": "You ___ smoke in the hospital. It's forbidden.",
        "options": ["mustn't", "don't have to", "shouldn't", "needn't"],
        "correct_indices": [0],
        "topic": "grammar",
    },
    {
        "text": "You ___ take an umbrella. It might rain.",
        "options": ["must", "should", "have to", "need"],
        "correct_indices": [1],
        "topic": "grammar",
    },
    {
        "text": "___ you help me with this heavy box, please?",
        "options": ["Could", "Must", "Should", "Need"],
        "correct_indices": [0],
        "topic": "grammar",
    },
    {
        "text": "They ___ be at home. I saw them at the mall.",
        "options": ["can't", "mustn't", "shouldn't", "needn't"],
        "correct_indices": [0],
        "topic": "grammar",
    },
    # Passive voice
    {
        "text": "The bridge ___ last year.",
        "options": ["built", "was built", "is built", "has built"],
        "correct_indices": [1],
        "topic": "grammar",
    },
    {
        "text": "English ___ in many countries.",
        "options": ["speaks", "spoke", "is spoken", "has spoken"],
        "correct_indices": [2],
        "topic": "grammar",
    },
    {
        "text": "The cake ___ by my grandmother right now.",
        "options": ["is being made", "is made", "was made", "has been made"],
        "correct_indices": [0],
        "topic": "grammar",
    },
    # Conditionals
    {
        "text": "If I ___ rich, I would travel around the world.",
        "options": ["am", "was", "were", "be"],
        "correct_indices": [2],
        "topic": "grammar",
    },
    {
        "text": "If you heat ice, it ___.",
        "options": ["melts", "melted", "will melt", "would melt"],
        "correct_indices": [0],
        "topic": "grammar",
    },
    {
        "text": "I would have passed the exam if I ___ harder.",
        "options": ["study", "studied", "had studied", "would study"],
        "correct_indices": [2],
        "topic": "grammar",
    },
    # Reported speech
    {
        "text": "She said that she ___ the book the day before.",
        "options": ["read", "reads", "had read", "has read"],
        "correct_indices": [2],
        "topic": "grammar",
    },
    {
        "text": "He asked me where I ___.",
        "options": ["live", "lived", "am living", "have lived"],
        "correct_indices": [1],
        "topic": "grammar",
    },
    # Comparatives/Superlatives
    {
        "text": "This is ___ book I've ever read.",
        "options": [
            "the most interesting",
            "more interesting",
            "most interesting",
            "interesting",
        ],
        "correct_indices": [0],
        "topic": "grammar",
    },
    {
        "text": "She speaks English ___ than her brother.",
        "options": ["good", "better", "best", "well"],
        "correct_indices": [1],
        "topic": "grammar",
    },
    {
        "text": "The more you practice, ___ you become.",
        "options": ["the better", "better", "the best", "good"],
        "correct_indices": [0],
        "topic": "grammar",
    },
    # Prepositions
    {
        "text": "I'm interested ___ learning new languages.",
        "options": ["in", "on", "at", "for"],
        "correct_indices": [0],
        "topic": "grammar",
    },
    {
        "text": "She is good ___ mathematics.",
        "options": ["in", "on", "at", "for"],
        "correct_indices": [2],
        "topic": "grammar",
    },
    {
        "text": "We arrived ___ the airport early in the morning.",
        "options": ["in", "on", "at", "to"],
        "correct_indices": [2],
        "topic": "grammar",
    },
    {
        "text": "He depends ___ his parents for financial support.",
        "options": ["in", "on", "at", "for"],
        "correct_indices": [1],
        "topic": "grammar",
    },
    # Gerunds and Infinitives
    {
        "text": "I enjoy ___ books in my free time.",
        "options": ["read", "reading", "to read", "reads"],
        "correct_indices": [1],
        "topic": "grammar",
    },
    {
        "text": "She decided ___ a new car.",
        "options": ["buy", "buying", "to buy", "bought"],
        "correct_indices": [2],
        "topic": "grammar",
    },
    {
        "text": "Would you mind ___ the window?",
        "options": ["open", "opening", "to open", "opened"],
        "correct_indices": [1],
        "topic": "grammar",
    },
    # Word formation
    {
        "text": "The ___ of the new building took two years.",
        "options": ["construct", "construction", "constructive", "constructor"],
        "correct_indices": [1],
        "topic": "grammar",
    },
    {
        "text": "She gave a very ___ speech at the conference.",
        "options": ["impress", "impressive", "impression", "impressively"],
        "correct_indices": [1],
        "topic": "grammar",
    },
    {
        "text": "His ___ to help others is admirable.",
        "options": ["willing", "willingness", "will", "willingly"],
        "correct_indices": [1],
        "topic": "grammar",
    },
    # Relative clauses
    {
        "text": "The woman ___ lives next door is a doctor.",
        "options": ["who", "which", "whose", "whom"],
        "correct_indices": [0],
        "topic": "grammar",
    },
    {
        "text": "This is the book ___ I told you about.",
        "options": ["who", "which", "whose", "whom"],
        "correct_indices": [1],
        "topic": "grammar",
    },
    {
        "text": "The man ___ car was stolen reported to the police.",
        "options": ["who", "which", "whose", "whom"],
        "correct_indices": [2],
        "topic": "grammar",
    },
    # Quantifiers
    {
        "text": "There isn't ___ milk in the refrigerator.",
        "options": ["some", "any", "much", "many"],
        "correct_indices": [1],
        "topic": "grammar",
    },
    {
        "text": "___ students have already finished the exam.",
        "options": ["Much", "Little", "Few", "Several"],
        "correct_indices": [3],
        "topic": "grammar",
    },
]

# Қосымша Reading сұрақтары
ADDITIONAL_READING_QUESTIONS = [
    # Reading Passage 3: The Future of Transportation
    {
        "text": "According to the text, what causes over 90% of car accidents?",
        "options": [
            "Technical failures",
            "Human error",
            "Weather conditions",
            "Poor road design",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_3,
    },
    {
        "text": "Self-driving cars use all of the following EXCEPT:",
        "options": ["Sensors", "Cameras", "Human drivers", "Artificial intelligence"],
        "correct_indices": [2],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_3,
    },
    {
        "text": "What benefit of self-driving cars is mentioned for elderly people?",
        "options": [
            "Lower insurance costs",
            "Mobility opportunities",
            "Entertainment features",
            "Medical monitoring",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_3,
    },
    {
        "text": "Which challenge for self-driving cars is NOT mentioned?",
        "options": [
            "Handling construction zones",
            "Severe weather",
            "High cost",
            "Ethical decisions",
        ],
        "correct_indices": [2],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_3,
    },
    {
        "text": "The word 'autonomous' in the text means:",
        "options": ["Fast", "Safe", "Self-operating", "Electric"],
        "correct_indices": [2],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_3,
    },
    {
        "text": "According to experts, self-driving cars will:",
        "options": [
            "Never be safe",
            "Become common in the next decade",
            "Only work in cities",
            "Replace all human drivers immediately",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_3,
    },
    {
        "text": "What job losses are mentioned as a concern?",
        "options": [
            "Factory workers",
            "Professional drivers",
            "Engineers",
            "Sales people",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_3,
    },
    {
        "text": "The main purpose of this text is to:",
        "options": [
            "Advertise self-driving cars",
            "Explain both benefits and challenges",
            "Criticize new technology",
            "Compare different car brands",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_3,
    },
    # Reading Passage 4: Social Media and Mental Health
    {
        "text": "According to the text, social media use is especially high among:",
        "options": [
            "Elderly people",
            "Business professionals",
            "Younger generations",
            "Rural populations",
        ],
        "correct_indices": [2],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_4,
    },
    {
        "text": "What positive aspect of social media is mentioned?",
        "options": [
            "Making money",
            "Social connections",
            "Physical fitness",
            "Career advancement",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_4,
    },
    {
        "text": "Heavy social media use has been linked to:",
        "options": [
            "Better sleep",
            "Higher grades",
            "Anxiety and depression",
            "Improved memory",
        ],
        "correct_indices": [2],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_4,
    },
    {
        "text": 'What does "carefully curated posts" suggest?',
        "options": [
            "Random photos",
            "Carefully selected and edited content",
            "News articles",
            "Advertisement",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_4,
    },
    {
        "text": "What recommendation do experts make?",
        "options": [
            "Avoid social media completely",
            "Use only one platform",
            "Set time limits",
            "Share more personal information",
        ],
        "correct_indices": [2],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_4,
    },
    {
        "text": "What are some schools teaching?",
        "options": ["Coding", "Digital literacy", "Photography", "Marketing"],
        "correct_indices": [1],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_4,
    },
    {
        "text": "The author's attitude toward social media is:",
        "options": [
            "Completely negative",
            "Completely positive",
            "Balanced",
            "Indifferent",
        ],
        "correct_indices": [2],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_4,
    },
    {
        "text": "Social media platforms mentioned include all EXCEPT:",
        "options": ["Facebook", "Instagram", "Twitter", "TikTok"],
        "correct_indices": [2],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_4,
    },
    # Reading Passage 5: Climate Change
    {
        "text": "What is the primary cause of climate change according to scientists?",
        "options": [
            "Natural cycles",
            "Solar activity",
            "Human activities",
            "Volcanic eruptions",
        ],
        "correct_indices": [2],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_5,
    },
    {
        "text": "The Paris Agreement aims to limit global warming to:",
        "options": ["0.5 degrees", "1.5 degrees", "2.5 degrees", "3 degrees"],
        "correct_indices": [1],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_5,
    },
    {
        "text": "How many countries signed the Paris Agreement?",
        "options": ["About 50", "About 100", "About 150", "Nearly 200"],
        "correct_indices": [3],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_5,
    },
    {
        "text": "Which individual action is NOT mentioned in the text?",
        "options": [
            "Reducing energy consumption",
            "Eating less meat",
            "Buying new cars",
            "Using public transportation",
        ],
        "correct_indices": [2],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_5,
    },
    {
        "text": "The phrase 'net-zero carbon emissions' means:",
        "options": [
            "No carbon at all",
            "Balanced carbon output and removal",
            "Low carbon only",
            "Carbon underground",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_5,
    },
    {
        "text": "According to the text, renewable energy is:",
        "options": [
            "Too expensive",
            "Becoming cost-competitive",
            "Only for wealthy countries",
            "Unreliable",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_5,
    },
    {
        "text": "Climate change effects include all EXCEPT:",
        "options": [
            "Extreme weather",
            "Rising sea levels",
            "Lower temperatures",
            "Melting ice caps",
        ],
        "correct_indices": [2],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_5,
    },
    {
        "text": "What is the main message of the text?",
        "options": [
            "Climate change is not real",
            "Only governments can solve climate change",
            "Both systemic and individual changes are needed",
            "Technology will solve everything",
        ],
        "correct_indices": [2],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_5,
    },
    # Reading Passage 6: The Digital Workplace
    {
        "text": "What accelerated the shift to remote work?",
        "options": [
            "New technology",
            "The COVID-19 pandemic",
            "Company policies",
            "Worker demands",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_6,
    },
    {
        "text": "Which benefit of remote work is mentioned?",
        "options": [
            "Higher salaries",
            "More meetings",
            "No commute time",
            "Free equipment",
        ],
        "correct_indices": [2],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_6,
    },
    {
        "text": "What challenge of remote work is discussed?",
        "options": [
            "Computer viruses",
            "Feelings of isolation",
            "Language barriers",
            "Bad internet",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_6,
    },
    {
        "text": "What model are many organizations adopting?",
        "options": ["Fully remote", "Fully in-office", "Hybrid", "Rotating shifts"],
        "correct_indices": [2],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_6,
    },
    {
        "text": "According to workers, remote work leads to:",
        "options": [
            "Lower productivity",
            "Higher productivity",
            "Same productivity",
            "No change",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_6,
    },
    {
        "text": "What can blur when working from home?",
        "options": [
            "Vision",
            "Work-life boundaries",
            "Internet connection",
            "Communication",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_6,
    },
    {
        "text": 'The phrase "control their environment" refers to:',
        "options": [
            "Temperature control",
            "Choosing where and how to work",
            "Managing other people",
            "Environmental protection",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_6,
    },
    {
        "text": "The conclusion suggests that the future of work will be:",
        "options": [
            "Completely remote",
            "Back to traditional offices",
            "More flexible",
            "Unchanged",
        ],
        "correct_indices": [2],
        "topic": "reading",
        "reading_passage": READING_PASSAGE_6,
    },
]


def seed_additional_questions():
    """Add additional Grammar and Reading questions to database"""
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

        added_grammar = 0
        added_reading = 0

        # Add Grammar questions
        print("Adding additional Grammar questions...")
        for q_data in ADDITIONAL_GRAMMAR_QUESTIONS:
            q_id = str(uuid.uuid4())

            db_question = DBQuestion(
                id=q_id,
                subject_id=SubjectId.ENGLISH.value,
                text=q_data["text"],
                type=QuestionType.SINGLE,
                topic=q_data["topic"],
                difficulty="medium",
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
            added_grammar += 1

        # Add Reading questions
        print("Adding additional Reading questions...")
        for q_data in ADDITIONAL_READING_QUESTIONS:
            q_id = str(uuid.uuid4())

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

            correct_ids = []
            for idx, opt_text in enumerate(q_data["options"]):
                opt_id = str(uuid.uuid4())
                db_option = DBOption(id=opt_id, question_id=q_id, text=opt_text)
                db.add(db_option)

                if idx in q_data["correct_indices"]:
                    correct_ids.append(opt_id)

            db_question.correct_option_ids = ",".join(correct_ids)
            added_reading += 1

        db.commit()

        print(f"\n{'='*50}")
        print("Successfully added additional questions!")
        print(f"- Grammar questions: +{added_grammar}")
        print(f"- Reading questions: +{added_reading} (4 new passages)")
        print(f"{'='*50}")

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

        print(f"\nТОТАL English Questions:")
        print(f"- Grammar: {total_grammar}")
        print(f"- Reading: {total_reading}")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    print("=" * 50)
    print("Additional Grammar & Reading Questions Seeder")
    print("=" * 50)
    seed_additional_questions()
