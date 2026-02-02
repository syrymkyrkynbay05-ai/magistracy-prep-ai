"""
Seed TGO (Test for Readiness to Learn) questions.
Based on "Оқуға дайындығын анықтау тесті" specification (2024).

Structure:
1. Critical Thinking (Сыни ойлау) - 15 questions
   - Quantitative Comparison
   - Problem Solving
   - Data Interpretation
2. Analytical Thinking (Аналитикалық ойлау) - 15 questions
   - Logic / Sentence formatting
   - Text Analysis (Reading Comprehension)

Total: 30 questions per variant.
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
# CRITICAL THINKING (СЫНИ ОЙЛАУ)
# ============================================================================

CRITICAL_THINKING = [
    # --- Салыстыру (Quantitative Comparison) ---
    {
        "text": "А және В бағандарындағы шамаларды салыстырыңыз.\nА бағаны: 0.75\nВ бағаны: 3/4",
        "options": [
            "А бағанындағы шама үлкен",
            "В бағанындағы шама үлкен",
            "Екі бағандағы шамалар тең",
            "Ақпарат жеткіліксіз",
        ],
        "correct_indices": [2],
        "topic": "critical_thinking",
        "difficulty": "A",
        "hint": "3/4 бөлшегін ондық бөлшекке айналдырыңыз.",
    },
    {
        "text": "А және В бағандарындағы шамаларды салыстырыңыз.\nА бағаны: (-2)^4\nВ бағаны: -2^4",
        "options": [
            "А бағанындағы шама үлкен",
            "В бағанындағы шама үлкен",
            "Екі бағандағы шамалар тең",
            "Ақпарат жеткіліксіз",
        ],
        "correct_indices": [0],  # 16 vs -16
        "topic": "critical_thinking",
        "difficulty": "B",
        "hint": "Дәреженің жұп немесе тақ екеніне және жақшаға мән беріңіз.",
    },
    {
        "text": "А және В бағандарындағы шамаларды салыстырыңыз.\nА бағаны: Шеңбердің ұзындығы (радиусы = 5)\nВ бағаны: 30",
        "options": [
            "А бағанындағы шама үлкен",
            "В бағанындағы шама үлкен",
            "Екі бағандағы шамалар тең",
            "Ақпарат жеткіліксіз",
        ],
        "correct_indices": [0],  # 2*pi*5 = 10*3.14 = 31.4 > 30
        "topic": "critical_thinking",
        "difficulty": "B",
        "hint": "Шеңбер ұзындығы C = 2πr. π ≈ 3.14",
    },
    # --- Есептер (Problem Solving) ---
    {
        "text": "Дүкендегі тауар 20%-ға қымбаттады, содан кейін жаңа бағасы 20%-ға арзандады. Тауардың соңғы бағасы бастапқы бағамен салыстырғанда қалай өзгерді?",
        "options": [
            "Өзгерген жоқ",
            "4%-ға қымбаттады",
            "4%-ға арзандады",
            "1%-ға арзандады",
        ],
        "correct_indices": [2],  # 100 -> 120 -> 120 - 24 = 96 (-4%)
        "topic": "critical_thinking",
        "difficulty": "B",
        "hint": "Бастапқы бағаны 100 деп алыңыз.",
    },
    {
        "text": "Пойыз 60 км/сағ жылдамдықпен 2 сағат, содан кейін 80 км/сағ жылдамдықпен 3 сағат жүрді. Пойыздың орташа жылдамдығын табыңыз.",
        "options": ["70 км/сағ", "72 км/сағ", "75 км/сағ", "68 км/сағ"],
        "correct_indices": [1],  # (120 + 240) / 5 = 360 / 5 = 72
        "topic": "critical_thinking",
        "difficulty": "B",
    },
    {
        "text": "Тіктөртбұрыштың ұзындығы 8 см, ал периметрі 28 см. Тіктөртбұрыштың ауданын табыңыз.",
        "options": ["20 см²", "48 см²", "64 см²", "96 см²"],
        "correct_indices": [1],  # 2(8+b)=28 -> 8+b=14 -> b=6. S=8*6=48
        "topic": "critical_thinking",
        "difficulty": "A",
    },
    {
        "text": "Егер 3x + 5 = 20 болса, 6x - 2 мәні нешеге тең?",
        "options": ["23", "28", "30", "32"],
        "correct_indices": [1],  # 3x=15 -> x=5. 6(5)-2 = 28
        "topic": "critical_thinking",
        "difficulty": "A",
    },
    {
        "text": "Сыныпта 25 оқушы бар. Олардың 15-і ағылшын тілін, 12-сі неміс тілін үйренеді. 5 оқушы екі тілді де үйренбейді. Неше оқушы екі тілді де үйренеді?",
        "options": ["2", "5", "7", "8"],
        "correct_indices": [2],  # 25-5=20 (үйренетіндер). 15+12-x=20 -> 27-x=20 -> x=7
        "topic": "critical_thinking",
        "difficulty": "C",
    },
    {
        "text": "Заңдылықты табыңыз: 2, 5, 11, 23, ___",
        "options": ["36", "45", "47", "52"],
        "correct_indices": [2],  # x2 + 1 format: 2*2+1=5 ... 23*2+1=47
        "topic": "critical_thinking",
        "difficulty": "B",
    },
    {
        "text": "Кітаптың беттерін нөмірлеу үшін 55 цифр қолданылды. Кітап неше беттен тұрады?",
        "options": ["22", "32", "55", "99"],
        "correct_indices": [1],  # 1-9 (9 цифр). 55-9=46. 46/2 = 23. 9+23 = 32 бет.
        "topic": "critical_thinking",
        "difficulty": "C",
        "hint": "1-ден 9-ға дейін 9 цифр. Екі таңбалы сандар 10-нан басталады.",
    },
    {
        "text": "Жәшікте 4 қызыл, 5 көк және 6 жасыл шар бар. Қарамай алынған шардың көк болу ықтималдығы қандай?",
        "options": ["1/3", "1/2", "5/15", "4/15"],
        "correct_indices": [0],  # Total 15. Blue 5. 5/15 = 1/3
        "topic": "critical_thinking",
        "difficulty": "B",
    },
    # --- Графиктер және деректер (Interpretation) ---
    {
        "text": "Диаграммада студенттердің сүйікті пәндері көрсетілген: Матем (40%), Физика (30%), Химия (20%), Биология (?). Егер барлық студенттер 200 болса, Биологияны таңдағандар саны қанша?",
        "options": ["10", "20", "30", "40"],
        "correct_indices": [1],  # 100 - (40+30+20) = 10%. 10% of 200 = 20
        "topic": "critical_thinking",
        "difficulty": "A",
    },
    {
        "text": "Төмендегі кестеде компанияның 3 жылдық табысы көрсетілген:\n2020: 5 млн\n2021: 7 млн\n2022: 6.5 млн\nТабыстың ең үлкен өсімі қай жылы байқалды?",
        "options": ["2020", "2021", "2022", "Бәрінде бірдей"],
        "correct_indices": [1],
        "topic": "critical_thinking",
        "difficulty": "A",
    },
    {
        "text": "Графикте y = 2x + 1 функциясы бейнеленген. Бұл түзу (0, b) нүктесі арқылы өтеді. b-ның мәнін табыңыз.",
        "options": ["0", "1", "2", "Анықтау мүмкін емес"],
        "correct_indices": [1],  # x=0, y=1
        "topic": "critical_thinking",
        "difficulty": "B",
    },
    {
        "text": "Компанияда 5 қызметкердің жалақылары: 100, 120, 110, 300, 120 мың теңге. Жалақының медианасын табыңыз.",
        "options": ["110", "120", "150", "300"],
        "correct_indices": [1],  # Sorted: 100, 110, 120, 120, 300. Median = 120
        "topic": "critical_thinking",
        "difficulty": "C",
    },
]


# ============================================================================
# ANALYTICAL THINKING (АНАЛИТИКАЛЫҚ ОЙЛАУ)
# ============================================================================

ANALYTICAL_THINKING = [
    # --- Логика және сөйлем ---
    {
        "text": "Бос орынды толтырыңыз: Жоғары білім беру жүйесі тек теориялық біліммен шектелмей, ___ дағдыларды да дамытуы керек.",
        "options": ["абстрактілі", "практикалық", "тарихи", "музыкалық"],
        "correct_indices": [1],
        "topic": "analytical_thinking",
        "difficulty": "A",
    },
    {
        "text": "Аналогияны табыңыз: Дәрігер : Аурухана = Мұғалім : ???",
        "options": ["Оқушы", "Кітап", "Мектеп", "Сынып"],
        "correct_indices": [2],
        "topic": "analytical_thinking",
        "difficulty": "A",
    },
    {
        "text": "Егер 'Барлық құстар ұшады' деген тұжырым жалған болса, төмендегілердің қайсысы ақиқат?",
        "options": [
            "Ешқандай құс ұшпайды",
            "Кейбір құстар ұшпайды",
            "Барлық құстар жүзеді",
            "Құстардың қанаты жоқ",
        ],
        "correct_indices": [1],
        "topic": "analytical_thinking",
        "difficulty": "B",
    },
    # --- Мәтінді талдау (Reading - Text 1) ---
    # Мәтін: Жасанды интеллект
    {
        "text": "[Мәтін] Жасанды интеллект (ЖИ) қазіргі таңда медицина, білім беру және өндіріс салаларында кеңінен қолданылуда. Ол дәрігерлерге диагноз қоюға, мұғалімдерге жеке оқу жоспарларын құруға көмектеседі. Алайда, ЖИ-дің дамуы жұмыс орындарының қысқаруына әкелуі мүмкін деген қауіп те бар. Сонымен қатар, этикалық мәселелер, мысалы, алгоритмдердің объективтілігі, әлі де шешімін таппаған сұрақтардың бірі.\n\nМәтіннің негізгі ойы қандай?",
        "options": [
            "ЖИ тек медицинада қолданылады",
            "ЖИ зиянды және оны тоқтату керек",
            "ЖИ көптеген мүмкіндіктер береді, бірақ қауіптері мен этикалық мәселелері бар",
            "ЖИ жұмыс орындарын толығымен жояды",
        ],
        "correct_indices": [2],
        "topic": "analytical_thinking",
        "difficulty": "B",
    },
    {
        "text": "[Мәтін бойынша] Автор ЖИ-дің қандай кемшілігін атап өтті?",
        "options": [
            "Электр қуатын көп тұтынуы",
            "Жұмыс орындарының қысқару қаупі мен этикалық мәселелер",
            "Бағдарламалық қамтамасыз етудің қымбаттығы",
            "Интернетке тәуелділігі",
        ],
        "correct_indices": [1],
        "topic": "analytical_thinking",
        "difficulty": "A",
    },
    {
        "text": "[Мәтін бойынша] «Алгоритмдердің объективтілігі» сөзі нені білдіреді?",
        "options": [
            "ЖИ-дің жылдам жұмыс істеуі",
            "ЖИ-дің шешім қабылдаудағы бейтараптығы мен әділдігі",
            "ЖИ-дің барлық тілдерді түсінуі",
            "ЖИ-дің адамға бағынуы",
        ],
        "correct_indices": [1],
        "topic": "analytical_thinking",
        "difficulty": "C",
    },
    # --- Мәтінді талдау (Reading - Text 2) ---
    # Мәтін: Климат өзгерісі
    {
        "text": "[Мәтін] Климаттың өзгеруі – бүкіл әлемдік мәселе. Ғалымдардың айтуынша, Жер шарының орташа температурасы соңғы жүз жылда айтарлықтай көтерілді. Бұл мұздықтардың еруіне, теңіз деңгейінің көтерілуіне және табиғи апаттардың жиілеуіне әкеліп соқтырады. Негізгі себептердің бірі – адам әрекетінен туындаған парник газдарының бөлінуі. Мәселені шешу үшін халықаралық ынтымақтастық пен жаңартылатын энергия көздеріне көшу қажет.\n\nМәтінге сәйкес, климат өзгерісінің негізгі салдары қандай?",
        "options": [
            "Жер температурасының төмендеуі",
            "Табиғи апаттардың азаюы",
            "Мұздықтардың еруі және теңіз деңгейінің көтерілуі",
            "Жаңартылатын энергия көздерінің азаюы",
        ],
        "correct_indices": [2],
        "topic": "analytical_thinking",
        "difficulty": "A",
    },
    {
        "text": "[Мәтін бойынша] Климат өзгерісінің басты себебі ретінде не көрсетілген?",
        "options": [
            "Күн белсенділігі",
            "Жанартаулардың атқылауы",
            "Адам әрекетінен туындаған парник газдары",
            "Мұхит ағыстарының өзгеруі",
        ],
        "correct_indices": [2],
        "topic": "analytical_thinking",
        "difficulty": "B",
    },
    {
        "text": "[Мәтін бойынша] Автор мәселені шешудің қандай жолын ұсынады?",
        "options": [
            "Өндірісті тоқтату",
            "Халықаралық ынтымақтастық және жасыл энергияға көшу",
            "Жерден басқа ғаламшарға көшу",
            "Климатты жасанды түрде өзгерту",
        ],
        "correct_indices": [1],
        "topic": "analytical_thinking",
        "difficulty": "B",
    },
    {
        "text": "[Мәтін бойынша] «Парник газдары» термині мәтінмәнінде нені білдіреді?",
        "options": [
            "Өсімдіктер шығаратын оттегі",
            "Ауаны салқындататын газдар",
            "Жылуды ұстап тұратын және температураны көтеретін газдар",
            "Зиянсыз табиғи газдар",
        ],
        "correct_indices": [2],
        "topic": "analytical_thinking",
        "difficulty": "C",
    },
    # --- Ақпаратты синтездеу ---
    {
        "text": "Екі пікір берілген:\n1. Ғаламтор ақпаратқа қолжетімділікті арттырды.\n2. Ақпараттың көптігі жалған ақпараттың таралуына әкелді.\nОсы екі пікірді біріктіретін ең дұрыс қорытынды қандай?",
        "options": [
            "Ғаламтор тек пайдалы",
            "Ғаламтор тек зиянды",
            "Ғаламтордың пайдасымен қатар, ақпаратты сүзгіден өткізу мәселесі де бар",
            "Адамдар ғаламторды қолданбауы керек",
        ],
        "correct_indices": [2],
        "topic": "analytical_thinking",
        "difficulty": "C",
    },
    {
        "text": "Үш дос (Асан, Үсен, Есен) әртүрлі спорт түрімен айналысады: футбол, бокс, күрес.\n- Асан күреспен айналыспайды.\n- Үсен бокспен айналыспайды және Асан футбол ойнамайды.\nЕсен қандай спорт түрімен айналысады?",
        "options": ["Футбол", "Бокс", "Күрес", "Анықтау мүмкін емес"],
        "correct_indices": [0],
        # Logic:
        # Asan != Kures
        # Usen != Box
        # Asan != Football -> Asan must be Box (since not Kures, not Football)
        # So Asan = Box.
        # Usen != Box, Usen != ??
        # Wait. Asan=Box.
        # Usen can be Football or Kures.
        # Esen can be Football or Kures.
        # Any other info? "Asan football oynamaydy".
        # Asan = Box.
        # What about Usen and Esen?
        # Check condition again.
        # "Usen boks emes".
        # If Asan is Box, then Usen is NOT Box (already true).
        # We need one more constraint or I made logic simple.
        # Let's re-read carefully: "Aсан күреспен айналыспайды". "Үсен бокспен айналыспайды және Асан футбол ойнамайды".
        # Asan: Not Kures, Not Football -> Asan = Box.
        # Usen: Not Box. (Must be Kures or Football)
        # Esen: (Must be Kures or Football)
        # Ah, usually "Each does different sport".
        # Is there enough info for Esen?
        # Maybe I missed something. Let's fix the question to be solvable.
        # "Үсен бокспен айналыспайды және Үсен футбол ойнамайды" -> Usen = Kures.
        # Then Esen = Football.
        # Let's update the text in code.
        "topic": "analytical_thinking",
        "difficulty": "C",
    },
    {
        "text": "Егер А > B және B > C болса, демек:",
        "options": ["A < C", "A = C", "A > C", "Бұлар өзара байланыссыз"],
        "correct_indices": [2],
        "topic": "analytical_thinking",
        "difficulty": "A",
    },
    {
        "text": "Кәсіпкер жаңа жоба бастады. Егер жоба сәтті болса, ол пайда табады. Егер жоба сәтсіз болса, ол тәжірибе жинақтайды. Кәсіпкер жобаны бастады. Қорытынды:",
        "options": [
            "Ол міндетті түрде пайда табады",
            "Ол міндетті түрде шығынға ұшырайды",
            "Ол не пайда табады, не тәжірибе жинақтайды",
            "Ол ештеңе алмайды",
        ],
        "correct_indices": [2],
        "topic": "analytical_thinking",
        "difficulty": "B",
    },
    {
        "text": "Мәтін үзіндісі: «Эмоционалды интеллект (EQ) – адамның өз эмоцияларын және өзгенің эмоцияларын түсіну қабілеті. Зерттеулер көрсеткендей, EQ деңгейі жоғары адамдар стреске төзімді келеді және командада жақсы жұмыс істейді.»\nТөмендегілердің қайсысы мәтіннен шығатын ең нақты қорытынды?",
        "options": [
            "IQ маңызды емес, тек EQ маңызды",
            "EQ деңгейі жоғары болу жұмыс орнындағы жетістікке оң әсер етуі мүмкін",
            "Барлық басшылардың EQ деңгейі жоғары",
            "Стресс тек EQ төмен адамдарда болады",
        ],
        "correct_indices": [1],
        "topic": "analytical_thinking",
        "difficulty": "B",
    },
]

# Update logic question 2 in list to be solvable
ANALYTICAL_THINKING[11][
    "text"
] = "Үш дос (Асан, Үсен, Есен) әртүрлі спорт түрімен айналысады: футбол, бокс, күрес.\n- Асан күреспен айналыспайды.\n- Үсен бокспен де, футболмен де айналыспайды.\nЕсен қандай спорт түрімен айналысады?"
# Asan != Kures.
# Usen != Box, Usen != Football -> Usen = Kures.
# Asan != Kures (Usen is Kures), so Asan can be Box or Football.
# But we know "Usen Kures".
# Wait. Asan != Kures. If Usen = Kures.
# Remaining sports for Asan: Box, Football.
# Remaining for Esen: Box, Football.
# Is there info about Asan? "Асан күреспен айналыспайды". That's it.
# Still ambiguous for Esen.
# Let's add: "Асан футбол ойнамайды".
# Then: Asan != Kures, Asan != Football -> Asan = Box.
# Usen != Box, Usen != Football -> Usen = Kures.
# Then Esen must be Football.
ANALYTICAL_THINKING[11][
    "text"
] = "Үш дос (Асан, Үсен, Есен) әртүрлі спорт түрімен айналысады: футбол, бокс, күрес.\n- Асан күреспен айналыспайды және футбол ойнамайды.\n- Үсен бокспен айналыспайды.\nЕсен қандай спорт түрімен айналысады?"
# Solve:
# Asan: Not Kures, Not Football -> Asan = Box.
# Usen: Not Box. (Can be Kures or Football). But Asan is Box. So Usen is Kures or Football.
# Wait, Asan took Box.
# Usen != Box. So Usen is Kures or Football.
# We need to know which one Usen is to know Esen.
# Let's make it simpler.
# Asan = Box.
# If Usen is Kures -> Esen is Football.
# If Usen is Football -> Esen is Kures.
# "Үсен бокспен айналыспайды" doesn't help distinguish.
# Let's change condition 2: "Үсен футбол ойнамайды".
# Then Usen (not Box - occupied? No we don't know).
# Let's rewrite completely.
ANALYTICAL_THINKING[11][
    "text"
] = "Үш дос (Асан, Үсен, Есен) әртүрлі спортпен айналысады: футбол, бокс, күрес.\n1) Асан күреспен айналыспайды.\n2) Үсен футбол ойнамайды.\n3) Есен бокспен айналыспайды.\n4) Асан мен Үсен бірге жаттықпайды (спорт түрлері бөлек).\nЕгер Асан боксер болса, Есен кім? (Бұл да күрделі)\n\nДұрыс нұсқа:\nАсан, Үсен, Есен - футболшы, боксшы, палуан.\n1. Асан палуан емес.\n2. Үсен боксшы емес.\n3. Есен футболшы емес.\n4. Асан футболшы емес.\n\nШешуі:\nАсан: палуан емес, футболшы емес -> Асан = Боксшы.\nҮсен: Боксшы емес (Асан боксшы), футболшы ма, палуан ба? \nЕсен: Футболшы емес.\nЕгер Асан Боксшы болса, Үсен мен Есенге Футбол мен Палуан қалды.\nЕсен футболшы емес -> Есен = Палуан.\nСонда Үсен = Футболшы.\n\nСұрақ: Есен қандай спорт түрімен айналысады?\nЖауап: Палуан (Күрес).\n"
# Let's put this logic into the question text.
ANALYTICAL_THINKING[11][
    "text"
] = "Үш дос (Асан, Үсен, Есен) әртүрлі спортпен айналысады: футбол, бокс, күрес.\n- Асан күреспен де, футболмен де айналыспайды.\n- Есен футболмен айналыспайды.\nЕсен қандай спорт түрімен айналысады?"
ANALYTICAL_THINKING[11]["options"] = ["Футбол", "Бокс", "Күрес", "Анықтау мүмкін емес"]
ANALYTICAL_THINKING[11]["correct_indices"] = [2]  # Kures
# Solve:
# Asan != Kures, Asan != Football -> Asan = Box.
# Esen != Football. Esen != Box (Asan is Box). -> Esen = Kures.
# Correct.


def seed_tgo_questions():
    """Add TGO questions to database."""
    db = SessionLocal()

    try:
        # Ensure TGO subject exists
        tgo_subject = (
            db.query(DBSubject).filter(DBSubject.id == SubjectId.TGO.value).first()
        )
        if not tgo_subject:
            print("Creating TGO Subject...")
            tgo_subject = DBSubject(
                id=SubjectId.TGO.value, name="Оқуға дайындығын анықтау тесті (TGO)"
            )
            db.add(tgo_subject)
            db.commit()

        all_questions = CRITICAL_THINKING + ANALYTICAL_THINKING
        added = 0

        print(f"Adding {len(all_questions)} TGO questions...")

        for q_data in all_questions:
            q_id = str(uuid.uuid4())

            db_question = DBQuestion(
                id=q_id,
                subject_id=SubjectId.TGO.value,
                text=q_data["text"],
                type=QuestionType.SINGLE,
                topic=q_data["topic"],
                difficulty=q_data.get("difficulty", "medium"),
                hint=q_data.get("hint"),
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

        print(f"\n[OK] Successfully added {added} TGO questions!")
        print(f"  - Critical Thinking: {len(CRITICAL_THINKING)}")
        print(f"  - Analytical Thinking: {len(ANALYTICAL_THINKING)}")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    print("=" * 60)
    print("[TGO] Readiness Test Questions Seeder")
    print("=" * 60)
    seed_tgo_questions()
