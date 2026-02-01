"""
Толық база кеңейту:
1. Listening - жаңа аудио тақырыптар (университет, саяхат, жұмыс, денсаулық)
2. Grammar - Phrasal verbs, Word formation
3. Reading - Австралия, Ғалымдар, Технология
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
# 1. LISTENING QUESTIONS - Жаңа аудио тақырыптар
# ============================================================================

# Audio Text 3: University Life
LISTENING_UNIVERSITY = [
    {
        "text": "According to the dialogue, when does the university library close?",
        "options": ["At 8 PM", "At 10 PM", "At midnight", "At 6 PM"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "The student wants to borrow books about:",
        "options": ["History", "Computer science", "Medicine", "Law"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "How many books can students borrow at once?",
        "options": ["3 books", "5 books", "7 books", "10 books"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "B",
    },
    {
        "text": "The librarian suggests the student to:",
        "options": [
            "Use online databases",
            "Buy new books",
            "Visit another library",
            "Ask a professor",
        ],
        "correct_indices": [0],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "The student's library card is valid for:",
        "options": ["One month", "One semester", "One year", "Forever"],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "What happens if books are returned late?",
        "options": [
            "Nothing happens",
            "Students pay a fine",
            "Students are banned",
            "Books are confiscated",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "The library has a special section for:",
        "options": [
            "Children",
            "Graduate students",
            "Teachers only",
            "Foreign students",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "C",
    },
    {
        "text": "According to the dialogue, the library is located:",
        "options": [
            "Next to the main building",
            "In the city center",
            "On campus",
            "In a separate building downtown",
        ],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
]

# Audio Text 4: Travel and Hotel
LISTENING_TRAVEL = [
    {
        "text": "The guest wants to book a room for:",
        "options": ["One night", "Three nights", "A week", "Two weeks"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "What type of room does the guest prefer?",
        "options": ["Single room", "Double room", "Suite", "Dormitory"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "The hotel offers free:",
        "options": ["Lunch", "Dinner", "Breakfast", "All meals"],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "Check-in time is at:",
        "options": ["12 PM", "2 PM", "3 PM", "5 PM"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "The guest asks about:",
        "options": ["Swimming pool", "Wi-Fi password", "Parking", "Restaurant hours"],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "The hotel is located near:",
        "options": ["The beach", "The airport", "The city center", "The mountains"],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "The receptionist recommends visiting:",
        "options": [
            "A local museum",
            "A shopping mall",
            "A famous restaurant",
            "All of the above",
        ],
        "correct_indices": [3],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "C",
    },
    {
        "text": "Payment can be made by:",
        "options": ["Cash only", "Card only", "Cash or card", "Bank transfer only"],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
]

# Audio Text 5: Job Interview
LISTENING_JOB = [
    {
        "text": "The candidate is applying for a position as:",
        "options": ["Manager", "Software developer", "Accountant", "Teacher"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "A",
    },
    {
        "text": "The candidate has ___ years of experience.",
        "options": ["2", "3", "5", "10"],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "The interviewer asks about the candidate's:",
        "options": ["Family", "Hobbies", "Previous projects", "Travel plans"],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "The company is looking for someone who can:",
        "options": [
            "Work independently",
            "Work only in teams",
            "Travel frequently",
            "Speak multiple languages",
        ],
        "correct_indices": [0],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "The salary will be discussed:",
        "options": [
            "At this interview",
            "In the second interview",
            "After hiring",
            "By email",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "C",
    },
    {
        "text": "The candidate's main strength is:",
        "options": [
            "Communication skills",
            "Problem-solving abilities",
            "Leadership experience",
            "Technical knowledge",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B2",
        "difficulty": "C",
    },
    {
        "text": "The working hours are:",
        "options": ["8 AM to 5 PM", "9 AM to 6 PM", "Flexible", "Night shifts"],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "The interviewer will contact the candidate:",
        "options": ["Today", "Tomorrow", "Within a week", "Within a month"],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "A",
    },
]

# Audio Text 6: Health and Doctor
LISTENING_HEALTH = [
    {
        "text": "The patient complains about:",
        "options": ["Headache", "Stomachache", "Back pain", "Toothache"],
        "correct_indices": [0],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "How long has the patient had these symptoms?",
        "options": ["One day", "Three days", "A week", "A month"],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "The doctor recommends:",
        "options": ["Taking medicine", "Surgery", "More exercise", "Eating less"],
        "correct_indices": [0],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "The patient should take the medicine:",
        "options": [
            "Once a day",
            "Twice a day",
            "Three times a day",
            "Before sleeping only",
        ],
        "correct_indices": [2],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "The patient should avoid:",
        "options": ["Coffee", "Water", "Vegetables", "Fruits"],
        "correct_indices": [0],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "The doctor suggests the patient to:",
        "options": [
            "Stay home and rest",
            "Go to work normally",
            "Exercise more",
            "Travel abroad",
        ],
        "correct_indices": [0],
        "topic": "listening",
        "language_level": "B1",
        "difficulty": "C",
    },
    {
        "text": "The next appointment is scheduled for:",
        "options": ["Tomorrow", "Next week", "Next month", "In three months"],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "The patient needs to bring ___ to the next appointment:",
        "options": [
            "Nothing",
            "Test results",
            "A family member",
            "Medical records from another hospital",
        ],
        "correct_indices": [1],
        "topic": "listening",
        "language_level": "B2",
        "difficulty": "C",
    },
]


# ============================================================================
# 2. GRAMMAR - Phrasal Verbs & Word Formation
# ============================================================================

PHRASAL_VERBS = [
    {
        "text": "Please ___ the TV. I want to watch the news.",
        "options": ["turn on", "turn off", "turn up", "turn over"],
        "correct_indices": [0],
        "topic": "grammar",
        "language_level": "A2",
        "difficulty": "A",
    },
    {
        "text": "I need to ___ early tomorrow for my flight.",
        "options": ["get up", "get on", "get off", "get over"],
        "correct_indices": [0],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "She ___ her grandmother. They look very similar.",
        "options": ["takes after", "takes on", "takes off", "takes up"],
        "correct_indices": [0],
        "topic": "grammar",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "We need to ___ this problem before the deadline.",
        "options": ["figure out", "figure on", "figure in", "figure up"],
        "correct_indices": [0],
        "topic": "grammar",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "The meeting has been ___ until next week.",
        "options": ["put on", "put off", "put up", "put away"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "B2",
        "difficulty": "C",
    },
    {
        "text": "I can't ___ with this noise anymore!",
        "options": ["put up", "put on", "put off", "put down"],
        "correct_indices": [0],
        "topic": "grammar",
        "language_level": "B2",
        "difficulty": "C",
    },
    {
        "text": "She ___ jogging last month to lose weight.",
        "options": ["took on", "took off", "took up", "took after"],
        "correct_indices": [2],
        "topic": "grammar",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "The plane ___ at 6 AM.",
        "options": ["takes on", "takes off", "takes up", "takes after"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "I need to ___ some information about the project.",
        "options": ["look for", "look up", "look after", "look into"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "Who will ___ the children while we're away?",
        "options": ["look for", "look up", "look after", "look into"],
        "correct_indices": [2],
        "topic": "grammar",
        "language_level": "A2",
        "difficulty": "A",
    },
]

WORD_FORMATION = [
    {
        "text": "Choose the noun form: happy → ___",
        "options": ["happily", "happiness", "happier", "unhappy"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "Choose the adjective form: danger → ___",
        "options": ["dangerously", "dangerous", "endanger", "danger"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "Choose the verb form: decision → ___",
        "options": ["decisive", "decisively", "decide", "decided"],
        "correct_indices": [2],
        "topic": "grammar",
        "language_level": "A2",
        "difficulty": "B",
    },
    {
        "text": "The ___ of the new building took two years. (construct)",
        "options": ["construct", "construction", "constructive", "constructor"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "His ___ to help others is admirable. (willing)",
        "options": ["willing", "willingness", "willingly", "unwilling"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "B1",
        "difficulty": "C",
    },
    {
        "text": "The opposite of 'possible' is:",
        "options": ["unpossible", "impossile", "impossible", "dispossible"],
        "correct_indices": [2],
        "topic": "grammar",
        "language_level": "A1",
        "difficulty": "A",
    },
    {
        "text": "The ___ quality of the product impressed everyone. (except)",
        "options": ["exceptional", "exception", "exceptionally", "excepted"],
        "correct_indices": [0],
        "topic": "grammar",
        "language_level": "B2",
        "difficulty": "C",
    },
    {
        "text": "She works as a ___ at the hospital. (psychology)",
        "options": ["psychology", "psychological", "psychologist", "psychologically"],
        "correct_indices": [2],
        "topic": "grammar",
        "language_level": "B1",
        "difficulty": "B",
    },
    {
        "text": "The ___ of the problem requires careful analysis. (complex)",
        "options": ["complex", "complexity", "complexly", "complexion"],
        "correct_indices": [1],
        "topic": "grammar",
        "language_level": "B2",
        "difficulty": "C",
    },
    {
        "text": "We need to ___ our approach. (modern)",
        "options": ["modern", "modernly", "modernize", "modernity"],
        "correct_indices": [2],
        "topic": "grammar",
        "language_level": "B1",
        "difficulty": "B",
    },
]


# ============================================================================
# 3. READING - Австралия, Ғалымдар, Технология
# ============================================================================

READING_AUSTRALIA = """AUSTRALIA: THE LAND DOWN UNDER

Australia is the world's sixth-largest country and the only nation to occupy an entire continent. Located in the Southern Hemisphere, it is known for its unique wildlife, stunning landscapes, and multicultural society.

The country is home to some of the world's most unusual animals, including kangaroos, koalas, and platypuses. The Great Barrier Reef, the world's largest coral reef system, attracts millions of tourists each year. Australia's vast outback covers most of the interior, featuring red deserts and ancient rock formations like Uluru.

Australia has one of the highest standards of living in the world. Its major cities, including Sydney, Melbourne, and Brisbane, consistently rank among the most livable cities globally. The education system is highly regarded, with several universities ranking in the world's top 100.

The country has a strong economy based on mining, agriculture, and services. It is one of the world's largest exporters of coal, iron ore, and gold. Agriculture plays a significant role, with Australia being a major producer of wool, beef, and wheat.

Despite its many advantages, Australia faces environmental challenges, including droughts, bushfires, and the effects of climate change on the Great Barrier Reef. The government and citizens are increasingly focused on sustainable practices and renewable energy."""

READING_SCIENTISTS = """MARIE CURIE: A PIONEER IN SCIENCE

Marie Curie was a Polish-born physicist and chemist who became the first woman to win a Nobel Prize, and the only person to win Nobel Prizes in two different sciences: Physics and Chemistry.

Born in Warsaw in 1867, Curie moved to Paris to pursue her education at a time when women had limited opportunities in science. She met Pierre Curie, a fellow scientist, and they married in 1895. Together, they discovered the elements polonium and radium, fundamentally changing our understanding of atomic science.

After Pierre's tragic death in 1906, Marie continued their research alone. She became the first female professor at the University of Paris and dedicated herself to applying radioactivity to medicine. During World War I, she developed mobile X-ray units, known as "petites Curies," which helped doctors locate bullets and shrapnel in wounded soldiers.

Curie faced significant discrimination throughout her career due to her gender and foreign origin. Despite this, she remained committed to her work and mentored many young scientists. Her notebooks are still so radioactive that they are kept in lead-lined boxes.

Marie Curie died in 1934 from aplastic anemia, likely caused by prolonged exposure to radiation. Her legacy lives on through the Marie Curie fellowships and the Curie Institutes in Paris and Warsaw, which continue to conduct cutting-edge cancer research."""

READING_AI = """ARTIFICIAL INTELLIGENCE: SHAPING THE FUTURE

Artificial Intelligence (AI) refers to computer systems that can perform tasks typically requiring human intelligence. From voice assistants to self-driving cars, AI is rapidly becoming part of everyday life.

Machine learning, a subset of AI, allows computers to learn from data without being explicitly programmed. This technology powers recommendation systems on Netflix and Spotify, fraud detection in banking, and language translation services. Deep learning, using neural networks inspired by the human brain, has achieved remarkable results in image recognition and natural language processing.

The benefits of AI are numerous. In healthcare, AI helps diagnose diseases earlier and develop new treatments. In education, adaptive learning systems personalize instruction for each student. In business, AI automates routine tasks, allowing humans to focus on creative and strategic work.

However, AI also raises concerns. There are fears about job displacement as machines become capable of performing more tasks. Privacy concerns arise from AI's ability to analyze vast amounts of personal data. Questions about bias in AI systems have emerged, as algorithms can perpetuate existing social inequalities.

Experts emphasize the need for responsible AI development. This includes ensuring transparency in how AI makes decisions, protecting privacy, and considering the social impact of AI deployment. As AI continues to evolve, the challenge is to harness its benefits while minimizing its risks."""

READING_AUSTRALIA_QUESTIONS = [
    {
        "text": "Australia is the only nation that:",
        "options": [
            "Has kangaroos",
            "Occupies an entire continent",
            "Is in the Southern Hemisphere",
            "Has a desert",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "A1",
        "difficulty": "A",
        "reading_passage": READING_AUSTRALIA,
    },
    {
        "text": "The Great Barrier Reef is:",
        "options": ["A mountain range", "A desert", "A coral reef system", "A forest"],
        "correct_indices": [2],
        "topic": "reading",
        "language_level": "A1",
        "difficulty": "A",
        "reading_passage": READING_AUSTRALIA,
    },
    {
        "text": "Which animal is NOT mentioned as Australian?",
        "options": ["Kangaroo", "Koala", "Lion", "Platypus"],
        "correct_indices": [2],
        "topic": "reading",
        "language_level": "A1",
        "difficulty": "A",
        "reading_passage": READING_AUSTRALIA,
    },
    {
        "text": "Australia's economy is based on:",
        "options": [
            "Only tourism",
            "Mining, agriculture, and services",
            "Only farming",
            "Only technology",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "A2",
        "difficulty": "B",
        "reading_passage": READING_AUSTRALIA,
    },
    {
        "text": "'The outback' refers to:",
        "options": ["Coastal areas", "Cities", "Interior/desert regions", "Mountains"],
        "correct_indices": [2],
        "topic": "reading",
        "language_level": "B1",
        "difficulty": "B",
        "reading_passage": READING_AUSTRALIA,
    },
    {
        "text": "Environmental challenges mentioned include:",
        "options": [
            "Earthquakes",
            "Tsunamis",
            "Bushfires and droughts",
            "Volcanic eruptions",
        ],
        "correct_indices": [2],
        "topic": "reading",
        "language_level": "B1",
        "difficulty": "C",
        "reading_passage": READING_AUSTRALIA,
    },
    {
        "text": "Australia is a major exporter of:",
        "options": [
            "Rice and tea",
            "Coal and iron ore",
            "Coffee and cocoa",
            "Silk and cotton",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "A2",
        "difficulty": "B",
        "reading_passage": READING_AUSTRALIA,
    },
    {
        "text": "The text suggests Australia is:",
        "options": [
            "A poor country",
            "A developed country with high living standards",
            "An undeveloped country",
            "A small country",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "B2",
        "difficulty": "C",
        "reading_passage": READING_AUSTRALIA,
    },
]

READING_SCIENTISTS_QUESTIONS = [
    {
        "text": "Marie Curie was born in:",
        "options": ["France", "Poland", "Germany", "Russia"],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "A1",
        "difficulty": "A",
        "reading_passage": READING_SCIENTISTS,
    },
    {
        "text": "How many Nobel Prizes did Marie Curie win?",
        "options": ["One", "Two", "Three", "Four"],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "A1",
        "difficulty": "A",
        "reading_passage": READING_SCIENTISTS,
    },
    {
        "text": "Marie Curie discovered:",
        "options": [
            "Oxygen and hydrogen",
            "Polonium and radium",
            "Gold and silver",
            "Carbon and nitrogen",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "A2",
        "difficulty": "B",
        "reading_passage": READING_SCIENTISTS,
    },
    {
        "text": "'Petites Curies' were:",
        "options": [
            "Marie's daughters",
            "Mobile X-ray units",
            "Laboratory equipment",
            "Research papers",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "B1",
        "difficulty": "B",
        "reading_passage": READING_SCIENTISTS,
    },
    {
        "text": "Marie faced discrimination because of:",
        "options": [
            "Her age",
            "Her gender and nationality",
            "Her education",
            "Her wealth",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "B1",
        "difficulty": "C",
        "reading_passage": READING_SCIENTISTS,
    },
    {
        "text": "Marie Curie died from:",
        "options": ["Old age", "Radiation exposure", "An accident", "Heart disease"],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "B1",
        "difficulty": "B",
        "reading_passage": READING_SCIENTISTS,
    },
    {
        "text": "Pierre Curie was Marie's:",
        "options": ["Brother", "Father", "Husband", "Teacher"],
        "correct_indices": [2],
        "topic": "reading",
        "language_level": "A1",
        "difficulty": "A",
        "reading_passage": READING_SCIENTISTS,
    },
    {
        "text": "The main idea of the text is:",
        "options": [
            "Nobel Prize history",
            "Marie Curie's life and achievements",
            "Polish scientists",
            "Radiation dangers",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "B2",
        "difficulty": "C",
        "reading_passage": READING_SCIENTISTS,
    },
]

READING_AI_QUESTIONS = [
    {
        "text": "AI stands for:",
        "options": [
            "Automatic Intelligence",
            "Artificial Intelligence",
            "Applied Internet",
            "Advanced Information",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "A1",
        "difficulty": "A",
        "reading_passage": READING_AI,
    },
    {
        "text": "Machine learning allows computers to:",
        "options": [
            "Only follow programs",
            "Learn from data",
            "Think like humans",
            "Create emotions",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "A2",
        "difficulty": "B",
        "reading_passage": READING_AI,
    },
    {
        "text": "Which is NOT mentioned as an AI application?",
        "options": [
            "Voice assistants",
            "Self-driving cars",
            "Weather prediction",
            "Fraud detection",
        ],
        "correct_indices": [2],
        "topic": "reading",
        "language_level": "A2",
        "difficulty": "B",
        "reading_passage": READING_AI,
    },
    {
        "text": "In healthcare, AI helps to:",
        "options": [
            "Replace doctors",
            "Diagnose diseases and develop treatments",
            "Only keep records",
            "Build hospitals",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "B1",
        "difficulty": "B",
        "reading_passage": READING_AI,
    },
    {
        "text": "A concern about AI is:",
        "options": [
            "It's too slow",
            "It's too expensive",
            "Job displacement",
            "It doesn't work",
        ],
        "correct_indices": [2],
        "topic": "reading",
        "language_level": "B1",
        "difficulty": "C",
        "reading_passage": READING_AI,
    },
    {
        "text": "'Bias in AI' means:",
        "options": [
            "AI is too fast",
            "Algorithms can perpetuate inequalities",
            "AI is biased toward humans",
            "AI works only on computers",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "B2",
        "difficulty": "C",
        "reading_passage": READING_AI,
    },
    {
        "text": "Deep learning uses:",
        "options": [
            "Simple calculations",
            "Neural networks",
            "Only text data",
            "Human teachers",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "B1",
        "difficulty": "B",
        "reading_passage": READING_AI,
    },
    {
        "text": "Experts emphasize the need for:",
        "options": [
            "Stopping AI development",
            "Responsible AI development",
            "Making AI secret",
            "Only using AI in labs",
        ],
        "correct_indices": [1],
        "topic": "reading",
        "language_level": "B2",
        "difficulty": "C",
        "reading_passage": READING_AI,
    },
]


def seed_expanded_base():
    """Add expanded questions to database"""
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
            LISTENING_UNIVERSITY
            + LISTENING_TRAVEL
            + LISTENING_JOB
            + LISTENING_HEALTH
            + PHRASAL_VERBS
            + WORD_FORMATION
            + READING_AUSTRALIA_QUESTIONS
            + READING_SCIENTISTS_QUESTIONS
            + READING_AI_QUESTIONS
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

        print(f"\n{'='*60}")
        print(f"✅ Successfully added {added} questions!")
        print("=" * 60)
        print("\n📚 Breakdown:")
        print(f"  LISTENING:")
        print(f"    - University: {len(LISTENING_UNIVERSITY)}")
        print(f"    - Travel: {len(LISTENING_TRAVEL)}")
        print(f"    - Job Interview: {len(LISTENING_JOB)}")
        print(f"    - Health: {len(LISTENING_HEALTH)}")
        print(f"  GRAMMAR:")
        print(f"    - Phrasal Verbs: {len(PHRASAL_VERBS)}")
        print(f"    - Word Formation: {len(WORD_FORMATION)}")
        print(f"  READING:")
        print(f"    - Australia: {len(READING_AUSTRALIA_QUESTIONS)}")
        print(f"    - Scientists: {len(READING_SCIENTISTS_QUESTIONS)}")
        print(f"    - AI/Technology: {len(READING_AI_QUESTIONS)}")

        # Show totals
        total_listening = (
            db.query(DBQuestion)
            .filter(
                DBQuestion.subject_id == SubjectId.ENGLISH.value,
                DBQuestion.topic.ilike("%listening%"),
            )
            .count()
        )

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
        print(f"  - Listening: {total_listening}")
        print(f"  - Grammar: {total_grammar}")
        print(f"  - Reading: {total_reading}")
        print(f"  - TOTAL: {total_listening + total_grammar + total_reading}")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    print("=" * 60)
    print("🚀 Expanded Base Seeder")
    print("   Listening + Grammar + Reading")
    print("=" * 60)
    seed_expanded_base()
