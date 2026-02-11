import os
import sys
import uuid

# Add backend directory to path for imports when running from project root
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.dirname(current_dir)
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import DBSubject, DBQuestion, DBOption, SubjectId, QuestionType
from auth import DBUser  # Ensure 'users' table is registered in Base.metadata

# Static questions database (No AI needed)
STATIC_QUESTIONS = {
    SubjectId.ENGLISH: [
        # Grammar - Conditionals
        {
            "text": "Choose the correct form: If I ___ you, I would study harder.",
            "options": ["am", "was", "were", "be"],
            "correct_indices": [2],
            "topic": "Conditionals",
        },
        {
            "text": "Complete: If the car is not there, we ___ have to walk.",
            "options": ["will", "would", "can", "could"],
            "correct_indices": [0],
            "topic": "Conditionals",
        },
        {
            "text": "Choose the correct form: If I had known earlier, I ___ helped you.",
            "options": ["will have", "would have", "can have", "should"],
            "correct_indices": [1],
            "topic": "Conditionals",
        },
        {
            "text": "Which sentence uses the Second Conditional correctly?",
            "options": [
                "If I win, I will celebrate.",
                "If I won, I would celebrate.",
                "If I had won, I would have celebrated.",
                "If I win, I would celebrate.",
            ],
            "correct_indices": [1],
            "topic": "Conditionals",
        },
        {
            "text": "What does 'Conditionals' mean in grammar?",
            "options": [
                "Past actions",
                "Hypothetical or real conditions",
                "Future plans",
                "Continuous actions",
            ],
            "correct_indices": [1],
            "topic": "Conditionals",
        },
        # Grammar - Tenses
        {
            "text": "Identify the tense: 'They have been working here for five years.'",
            "options": [
                "Present Simple",
                "Present Perfect Continuous",
                "Past Perfect",
                "Future Simple",
            ],
            "correct_indices": [1],
            "topic": "Tenses",
        },
        {
            "text": "Identify the tense: 'She had finished her homework before dinner.'",
            "options": [
                "Past Simple",
                "Past Continuous",
                "Past Perfect",
                "Present Perfect",
            ],
            "correct_indices": [2],
            "topic": "Tenses",
        },
        {
            "text": "Which tense is used for actions happening right now?",
            "options": [
                "Present Simple",
                "Present Continuous",
                "Past Simple",
                "Future Simple",
            ],
            "correct_indices": [1],
            "topic": "Tenses",
        },
        {
            "text": "Complete: By next year, I ___ graduated from university.",
            "options": ["will", "will have", "have", "had"],
            "correct_indices": [1],
            "topic": "Tenses",
        },
        {
            "text": "Which sentence is in Future Perfect?",
            "options": [
                "I will go tomorrow.",
                "I will have finished by 5 PM.",
                "I am going tomorrow.",
                "I have finished.",
            ],
            "correct_indices": [1],
            "topic": "Tenses",
        },
        # Grammar - Modal Verbs
        {
            "text": "Which modal verb expresses ability?",
            "options": ["should", "must", "can", "would"],
            "correct_indices": [2],
            "topic": "Modal Verbs",
        },
        {
            "text": "Which modal verb expresses obligation?",
            "options": ["can", "could", "must", "might"],
            "correct_indices": [2],
            "topic": "Modal Verbs",
        },
        {
            "text": "Complete: You ___ see a doctor if you feel sick.",
            "options": ["can", "should", "would", "might"],
            "correct_indices": [1],
            "topic": "Modal Verbs",
        },
        {
            "text": "'Could' is the past form of which modal verb?",
            "options": ["can", "will", "shall", "may"],
            "correct_indices": [0],
            "topic": "Modal Verbs",
        },
        {
            "text": "What do modal verbs express?",
            "options": [
                "Only past actions",
                "Ability, possibility, obligation, permission",
                "Only future actions",
                "Only questions",
            ],
            "correct_indices": [1],
            "topic": "Modal Verbs",
        },
        # Vocabulary - Synonyms
        {
            "text": "What is the synonym of 'improve'?",
            "options": ["decrease", "boost", "weaken", "deteriorate"],
            "correct_indices": [1],
            "topic": "Synonyms",
        },
        {
            "text": "What is the synonym of 'founded'?",
            "options": ["lost", "established", "destroyed", "forgotten"],
            "correct_indices": [1],
            "topic": "Synonyms",
        },
        {
            "text": "What is the synonym of 'begin'?",
            "options": ["end", "start", "finish", "stop"],
            "correct_indices": [1],
            "topic": "Synonyms",
        },
        {
            "text": "What is the synonym of 'difficult'?",
            "options": ["easy", "simple", "hard", "clear"],
            "correct_indices": [2],
            "topic": "Synonyms",
        },
        # Vocabulary - Antonyms
        {
            "text": "What is the antonym of 'increase'?",
            "options": ["grow", "expand", "decrease", "rise"],
            "correct_indices": [2],
            "topic": "Antonyms",
        },
        {
            "text": "What is the antonym of 'ancient'?",
            "options": ["old", "modern", "historic", "traditional"],
            "correct_indices": [1],
            "topic": "Antonyms",
        },
        # Vocabulary - Academic Words
        {
            "text": "What does 'globalization' mean?",
            "options": [
                "Local business only",
                "Worldwide integration and interaction",
                "Government policy",
                "Environmental protection",
            ],
            "correct_indices": [1],
            "topic": "Academic Vocabulary",
        },
        {
            "text": "What does 'e-learning' refer to?",
            "options": [
                "Traditional classroom learning",
                "Learning through electronic media",
                "Physical education",
                "Library studies",
            ],
            "correct_indices": [1],
            "topic": "Academic Vocabulary",
        },
        {
            "text": "What is a 'start-up'?",
            "options": [
                "An old company",
                "A newly established business",
                "A government agency",
                "A charity organization",
            ],
            "correct_indices": [1],
            "topic": "Academic Vocabulary",
        },
        {
            "text": "Who are 'pedestrians'?",
            "options": [
                "Car drivers",
                "Bicycle riders",
                "People walking on foot",
                "Bus passengers",
            ],
            "correct_indices": [2],
            "topic": "Academic Vocabulary",
        },
        # Vocabulary - Prefixes
        {
            "text": "Which prefix makes a word negative?",
            "options": ["re-", "pre-", "un-", "over-"],
            "correct_indices": [2],
            "topic": "Prefixes",
        },
        {
            "text": "What does the prefix 'dis-' mean in 'disagree'?",
            "options": ["Again", "Before", "Not/Opposite", "Too much"],
            "correct_indices": [2],
            "topic": "Prefixes",
        },
        {
            "text": "What does the prefix 'im-' mean in 'impossible'?",
            "options": ["Possible", "Not", "Again", "Before"],
            "correct_indices": [1],
            "topic": "Prefixes",
        },
        {
            "text": "Which word has a negative prefix?",
            "options": ["happy", "unhappy", "happiness", "happily"],
            "correct_indices": [1],
            "topic": "Prefixes",
        },
        # Reading Comprehension
        {
            "text": "What does 'Main Idea' mean in reading?",
            "options": [
                "The first sentence",
                "The central point or message of the text",
                "The last paragraph",
                "The title only",
            ],
            "correct_indices": [1],
            "topic": "Reading",
        },
        {
            "text": "What does 'context' help you understand?",
            "options": [
                "The author's name",
                "The meaning of unknown words",
                "The publication date",
                "The page number",
            ],
            "correct_indices": [1],
            "topic": "Reading",
        },
        {
            "text": "In reading tasks, what does 'True/False' require?",
            "options": [
                "Writing an essay",
                "Checking if a statement matches the text",
                "Translating the text",
                "Summarizing the text",
            ],
            "correct_indices": [1],
            "topic": "Reading",
        },
        {
            "text": "What is 'vocabulary in context'?",
            "options": [
                "Memorizing words",
                "Understanding word meaning from surrounding text",
                "Spelling practice",
                "Grammar rules",
            ],
            "correct_indices": [1],
            "topic": "Reading",
        },
        {
            "text": "Music has been shown to improve which abilities according to research?",
            "options": [
                "Only physical strength",
                "Language and cognitive abilities",
                "Only mathematical skills",
                "Only artistic skills",
            ],
            "correct_indices": [1],
            "topic": "Reading",
        },
        # Additional Grammar - Passive Voice
        {
            "text": "Choose the passive form: 'They built this house in 1990.'",
            "options": [
                "This house built in 1990.",
                "This house was built in 1990.",
                "This house is built in 1990.",
                "This house has built in 1990.",
            ],
            "correct_indices": [1],
            "topic": "Passive Voice",
        },
        {
            "text": "Which sentence is in passive voice?",
            "options": [
                "She writes a letter.",
                "The letter was written by her.",
                "She is writing a letter.",
                "She has written a letter.",
            ],
            "correct_indices": [1],
            "topic": "Passive Voice",
        },
        {
            "text": "Complete: The cake ___ by my mother.",
            "options": ["baked", "was baked", "is baking", "bakes"],
            "correct_indices": [1],
            "topic": "Passive Voice",
        },
        # Additional Grammar - Articles
        {
            "text": "Choose the correct article: I saw ___ elephant at the zoo.",
            "options": ["a", "an", "the", "no article"],
            "correct_indices": [1],
            "topic": "Articles",
        },
        {
            "text": "Which article is used before unique objects?",
            "options": ["a", "an", "the", "no article"],
            "correct_indices": [2],
            "topic": "Articles",
        },
        {
            "text": "Complete: ___ sun rises in the east.",
            "options": ["A", "An", "The", "No article"],
            "correct_indices": [2],
            "topic": "Articles",
        },
        # Additional Grammar - Prepositions
        {
            "text": "Choose the correct preposition: I arrived ___ the airport at 3 PM.",
            "options": ["in", "on", "at", "to"],
            "correct_indices": [2],
            "topic": "Prepositions",
        },
        {
            "text": "Complete: She is interested ___ learning languages.",
            "options": ["on", "at", "in", "for"],
            "correct_indices": [2],
            "topic": "Prepositions",
        },
        {
            "text": "Which preposition is correct: He depends ___ his parents.",
            "options": ["in", "on", "at", "of"],
            "correct_indices": [1],
            "topic": "Prepositions",
        },
        # Additional Vocabulary - Word Formation
        {
            "text": "What is the noun form of 'important'?",
            "options": ["importantly", "importance", "importantness", "importation"],
            "correct_indices": [1],
            "topic": "Word Formation",
        },
        {
            "text": "What is the adjective form of 'success'?",
            "options": ["succeed", "successfully", "successful", "succession"],
            "correct_indices": [2],
            "topic": "Word Formation",
        },
        {
            "text": "What is the verb form of 'decision'?",
            "options": ["decisive", "decide", "decided", "decidedly"],
            "correct_indices": [1],
            "topic": "Word Formation",
        },
        # Additional Vocabulary - Collocations
        {
            "text": "Complete the collocation: make a ___",
            "options": ["homework", "decision", "research", "progress"],
            "correct_indices": [1],
            "topic": "Collocations",
        },
        {
            "text": "Complete the collocation: do ___",
            "options": ["a mistake", "homework", "a decision", "an effort"],
            "correct_indices": [1],
            "topic": "Collocations",
        },
        {
            "text": "Complete the collocation: take ___",
            "options": ["a photo", "homework", "a decision", "progress"],
            "correct_indices": [0],
            "topic": "Collocations",
        },
        # Additional Reading Skills
        {
            "text": "What is 'skimming' in reading?",
            "options": [
                "Reading every word carefully",
                "Reading quickly for general idea",
                "Reading aloud",
                "Memorizing the text",
            ],
            "correct_indices": [1],
            "topic": "Reading Skills",
        },
        {
            "text": "What is 'scanning' in reading?",
            "options": [
                "Reading for overall meaning",
                "Looking for specific information",
                "Reading slowly",
                "Translating the text",
            ],
            "correct_indices": [1],
            "topic": "Reading Skills",
        },
        {
            "text": "What does 'inference' mean in reading?",
            "options": [
                "Direct statement",
                "Conclusion based on evidence",
                "Translation",
                "Summary",
            ],
            "correct_indices": [1],
            "topic": "Reading Skills",
        },
        # === ADDITIONAL CONDITIONALS (10 more) ===
        {
            "text": "Complete: If it ___ tomorrow, we will stay home.",
            "options": ["rains", "will rain", "rained", "would rain"],
            "correct_indices": [0],
            "topic": "Conditionals",
        },
        {
            "text": "If she ___ harder, she would pass the exam.",
            "options": ["studies", "studied", "will study", "study"],
            "correct_indices": [1],
            "topic": "Conditionals",
        },
        {
            "text": "Complete: If I ___ rich, I would travel the world.",
            "options": ["am", "will be", "were", "was being"],
            "correct_indices": [2],
            "topic": "Conditionals",
        },
        {
            "text": "Which is Third Conditional?",
            "options": [
                "If I study, I pass.",
                "If I studied, I would pass.",
                "If I had studied, I would have passed.",
                "If I study, I will pass.",
            ],
            "correct_indices": [2],
            "topic": "Conditionals",
        },
        {
            "text": "Complete: If you had told me, I ___ helped.",
            "options": ["will have", "would have", "can", "should"],
            "correct_indices": [1],
            "topic": "Conditionals",
        },
        {
            "text": "Zero Conditional expresses:",
            "options": [
                "Unreal situations",
                "General truths",
                "Past regrets",
                "Future plans",
            ],
            "correct_indices": [1],
            "topic": "Conditionals",
        },
        {
            "text": "Complete: If water reaches 100°C, it ___.",
            "options": ["will boil", "boils", "would boil", "boiled"],
            "correct_indices": [1],
            "topic": "Conditionals",
        },
        {
            "text": "If I were a bird, I ___ fly away.",
            "options": ["will", "would", "can", "could have"],
            "correct_indices": [1],
            "topic": "Conditionals",
        },
        {
            "text": "Which sentence is First Conditional?",
            "options": [
                "If I have time, I visit him.",
                "If I have time, I will visit him.",
                "If I had time, I would visit him.",
                "If I had had time, I would have visited him.",
            ],
            "correct_indices": [1],
            "topic": "Conditionals",
        },
        {
            "text": "Complete: ___ I knew, I would have helped.",
            "options": ["If", "When", "Had", "Should"],
            "correct_indices": [2],
            "topic": "Conditionals",
        },
        # === ADDITIONAL TENSES (15 more) ===
        {
            "text": "Identify: 'She has just arrived.'",
            "options": [
                "Past Simple",
                "Present Perfect",
                "Past Perfect",
                "Present Simple",
            ],
            "correct_indices": [1],
            "topic": "Tenses",
        },
        {
            "text": "Identify: 'They were playing when I called.'",
            "options": [
                "Past Simple",
                "Past Perfect",
                "Past Continuous",
                "Present Continuous",
            ],
            "correct_indices": [2],
            "topic": "Tenses",
        },
        {
            "text": "Complete: I ___ to London three times.",
            "options": ["go", "went", "have been", "am going"],
            "correct_indices": [2],
            "topic": "Tenses",
        },
        {
            "text": "Which tense: 'By the time you arrive, I will have left.'",
            "options": [
                "Future Simple",
                "Future Perfect",
                "Future Continuous",
                "Present Perfect",
            ],
            "correct_indices": [1],
            "topic": "Tenses",
        },
        {
            "text": "Complete: She ___ English every day.",
            "options": ["study", "studies", "is studying", "studied"],
            "correct_indices": [1],
            "topic": "Tenses",
        },
        {
            "text": "When do we use Present Simple?",
            "options": [
                "For temporary actions",
                "For habits and routines",
                "For past events",
                "For future plans",
            ],
            "correct_indices": [1],
            "topic": "Tenses",
        },
        {
            "text": "Complete: Look! It ___.",
            "options": ["rains", "is raining", "rained", "has rained"],
            "correct_indices": [1],
            "topic": "Tenses",
        },
        {
            "text": "Identify: 'I had never seen such a beautiful sunset before.'",
            "options": [
                "Past Simple",
                "Past Perfect",
                "Present Perfect",
                "Past Continuous",
            ],
            "correct_indices": [1],
            "topic": "Tenses",
        },
        {
            "text": "Complete: This time tomorrow, I ___ in Paris.",
            "options": ["will be", "am", "was", "have been"],
            "correct_indices": [0],
            "topic": "Tenses",
        },
        {
            "text": "Which sentence is Present Perfect Continuous?",
            "options": [
                "I have worked here for 5 years.",
                "I have been working here for 5 years.",
                "I work here for 5 years.",
                "I worked here for 5 years.",
            ],
            "correct_indices": [1],
            "topic": "Tenses",
        },
        {
            "text": "Complete: When I arrived, the movie ___.",
            "options": [
                "already started",
                "has already started",
                "had already started",
                "starts",
            ],
            "correct_indices": [2],
            "topic": "Tenses",
        },
        {
            "text": "Which keyword signals Present Perfect?",
            "options": ["yesterday", "last week", "just", "tomorrow"],
            "correct_indices": [2],
            "topic": "Tenses",
        },
        {
            "text": "Complete: We ___ for three hours before we took a break.",
            "options": ["worked", "had been working", "have worked", "are working"],
            "correct_indices": [1],
            "topic": "Tenses",
        },
        {
            "text": "Which tense uses 'will + be + -ing'?",
            "options": [
                "Future Simple",
                "Future Continuous",
                "Future Perfect",
                "Present Continuous",
            ],
            "correct_indices": [1],
            "topic": "Tenses",
        },
        {
            "text": "Complete: She ___ to work every day by bus.",
            "options": ["go", "goes", "is going", "went"],
            "correct_indices": [1],
            "topic": "Tenses",
        },
        # === ADDITIONAL MODAL VERBS (10 more) ===
        {
            "text": "Which modal expresses possibility?",
            "options": ["must", "might", "should", "need"],
            "correct_indices": [1],
            "topic": "Modal Verbs",
        },
        {
            "text": "Complete: You ___ smoke here. It's forbidden.",
            "options": ["mustn't", "don't have to", "shouldn't", "can't"],
            "correct_indices": [0],
            "topic": "Modal Verbs",
        },
        {
            "text": "'May I come in?' expresses:",
            "options": ["ability", "permission", "obligation", "advice"],
            "correct_indices": [1],
            "topic": "Modal Verbs",
        },
        {
            "text": "Complete: You ___ to respect your elders.",
            "options": ["should", "ought", "must", "could"],
            "correct_indices": [1],
            "topic": "Modal Verbs",
        },
        {
            "text": "'You needn't worry' means:",
            "options": [
                "It's forbidden",
                "It's not necessary",
                "It's possible",
                "It's certain",
            ],
            "correct_indices": [1],
            "topic": "Modal Verbs",
        },
        {
            "text": "Which modal expresses strong probability?",
            "options": ["might", "may", "must", "could"],
            "correct_indices": [2],
            "topic": "Modal Verbs",
        },
        {
            "text": "'Would you like some tea?' is a:",
            "options": ["Command", "Offer", "Obligation", "Prohibition"],
            "correct_indices": [1],
            "topic": "Modal Verbs",
        },
        {
            "text": "Complete: I ___ swim when I was 5.",
            "options": ["can", "could", "may", "should"],
            "correct_indices": [1],
            "topic": "Modal Verbs",
        },
        {
            "text": "'Shall' is commonly used with:",
            "options": ["He/She", "They", "I/We", "You"],
            "correct_indices": [2],
            "topic": "Modal Verbs",
        },
        {
            "text": "Complete: He ___ be at home. His car is there.",
            "options": ["can't", "must", "shouldn't", "needn't"],
            "correct_indices": [1],
            "topic": "Modal Verbs",
        },
        # === ADDITIONAL SYNONYMS (10 more) ===
        {
            "text": "Synonym of 'enormous':",
            "options": ["tiny", "huge", "average", "small"],
            "correct_indices": [1],
            "topic": "Synonyms",
        },
        {
            "text": "Synonym of 'intelligent':",
            "options": ["foolish", "smart", "slow", "careless"],
            "correct_indices": [1],
            "topic": "Synonyms",
        },
        {
            "text": "Synonym of 'purchase':",
            "options": ["sell", "buy", "rent", "borrow"],
            "correct_indices": [1],
            "topic": "Synonyms",
        },
        {
            "text": "Synonym of 'frequently':",
            "options": ["rarely", "seldom", "often", "never"],
            "correct_indices": [2],
            "topic": "Synonyms",
        },
        {
            "text": "Synonym of 'authentic':",
            "options": ["fake", "genuine", "artificial", "false"],
            "correct_indices": [1],
            "topic": "Synonyms",
        },
        {
            "text": "Synonym of 'hazardous':",
            "options": ["safe", "dangerous", "harmless", "secure"],
            "correct_indices": [1],
            "topic": "Synonyms",
        },
        {
            "text": "Synonym of 'approximately':",
            "options": ["exactly", "precisely", "about", "always"],
            "correct_indices": [2],
            "topic": "Synonyms",
        },
        {
            "text": "Synonym of 'sufficient':",
            "options": ["lacking", "enough", "scarce", "insufficient"],
            "correct_indices": [1],
            "topic": "Synonyms",
        },
        {
            "text": "Synonym of 'accomplish':",
            "options": ["fail", "achieve", "abandon", "neglect"],
            "correct_indices": [1],
            "topic": "Synonyms",
        },
        {
            "text": "Synonym of 'comprehend':",
            "options": ["ignore", "understand", "forget", "confuse"],
            "correct_indices": [1],
            "topic": "Synonyms",
        },
        # === ADDITIONAL ANTONYMS (10 more) ===
        {
            "text": "Antonym of 'brave':",
            "options": ["courageous", "cowardly", "bold", "fearless"],
            "correct_indices": [1],
            "topic": "Antonyms",
        },
        {
            "text": "Antonym of 'temporary':",
            "options": ["brief", "short", "permanent", "momentary"],
            "correct_indices": [2],
            "topic": "Antonyms",
        },
        {
            "text": "Antonym of 'generous':",
            "options": ["kind", "selfish", "giving", "charitable"],
            "correct_indices": [1],
            "topic": "Antonyms",
        },
        {
            "text": "Antonym of 'transparent':",
            "options": ["clear", "opaque", "visible", "obvious"],
            "correct_indices": [1],
            "topic": "Antonyms",
        },
        {
            "text": "Antonym of 'artificial':",
            "options": ["fake", "synthetic", "natural", "man-made"],
            "correct_indices": [2],
            "topic": "Antonyms",
        },
        {
            "text": "Antonym of 'voluntary':",
            "options": ["willing", "optional", "compulsory", "free"],
            "correct_indices": [2],
            "topic": "Antonyms",
        },
        {
            "text": "Antonym of 'optimistic':",
            "options": ["hopeful", "pessimistic", "positive", "cheerful"],
            "correct_indices": [1],
            "topic": "Antonyms",
        },
        {
            "text": "Antonym of 'expand':",
            "options": ["grow", "enlarge", "contract", "spread"],
            "correct_indices": [2],
            "topic": "Antonyms",
        },
        {
            "text": "Antonym of 'admit':",
            "options": ["accept", "deny", "confess", "acknowledge"],
            "correct_indices": [1],
            "topic": "Antonyms",
        },
        {
            "text": "Antonym of 'familiar':",
            "options": ["known", "strange", "common", "usual"],
            "correct_indices": [1],
            "topic": "Antonyms",
        },
        # === ADDITIONAL ACADEMIC VOCABULARY (10 more) ===
        {
            "text": "What does 'hypothesis' mean?",
            "options": [
                "Final answer",
                "Proposed explanation",
                "Proven fact",
                "Random guess",
            ],
            "correct_indices": [1],
            "topic": "Academic Vocabulary",
        },
        {
            "text": "What does 'methodology' refer to?",
            "options": ["Results", "System of methods", "Conclusion", "Introduction"],
            "correct_indices": [1],
            "topic": "Academic Vocabulary",
        },
        {
            "text": "What is 'infrastructure'?",
            "options": [
                "Basic physical structures for society",
                "Government policies",
                "Cultural traditions",
                "Educational programs",
            ],
            "correct_indices": [0],
            "topic": "Academic Vocabulary",
        },
        {
            "text": "What does 'sustainable' mean?",
            "options": [
                "Temporary",
                "Maintainable without depletion",
                "Expensive",
                "Outdated",
            ],
            "correct_indices": [1],
            "topic": "Academic Vocabulary",
        },
        {
            "text": "What is 'biodiversity'?",
            "options": [
                "Single species protection",
                "Variety of life forms",
                "Chemical processes",
                "Urban development",
            ],
            "correct_indices": [1],
            "topic": "Academic Vocabulary",
        },
        {
            "text": "What does 'innovation' mean?",
            "options": [
                "Traditional method",
                "New idea or method",
                "Outdated practice",
                "Common routine",
            ],
            "correct_indices": [1],
            "topic": "Academic Vocabulary",
        },
        {
            "text": "What is 'curriculum'?",
            "options": [
                "School building",
                "Courses of study",
                "Student grades",
                "Teacher salary",
            ],
            "correct_indices": [1],
            "topic": "Academic Vocabulary",
        },
        {
            "text": "What does 'consensus' mean?",
            "options": [
                "Disagreement",
                "General agreement",
                "Individual opinion",
                "Opposition",
            ],
            "correct_indices": [1],
            "topic": "Academic Vocabulary",
        },
        {
            "text": "What is 'plagiarism'?",
            "options": [
                "Original work",
                "Copying others' work without credit",
                "Correct citation",
                "Creative writing",
            ],
            "correct_indices": [1],
            "topic": "Academic Vocabulary",
        },
        {
            "text": "What does 'empirical' mean?",
            "options": [
                "Based on theory",
                "Based on observation",
                "Based on belief",
                "Based on tradition",
            ],
            "correct_indices": [1],
            "topic": "Academic Vocabulary",
        },
        # === LISTENING GROUP 1: My Family and Home (8 questions) ===
        {
            "text": "How old is Anna?",
            "options": ["Twenty-one", "Twenty-three", "Twenty-five", "Twenty-seven"],
            "correct_indices": [1],
            "topic": "Listening",
            "reading_passage": "AUDIO:/english/My Family and Home.mp3",
        },
        {
            "text": "Where does Anna live?",
            "options": ["Astana", "London", "Almaty", "New York"],
            "correct_indices": [2],
            "topic": "Listening",
            "reading_passage": "AUDIO:/english/My Family and Home.mp3",
        },
        {
            "text": "How many people are in Anna's family?",
            "options": ["Three", "Four", "Five", "Six"],
            "correct_indices": [1],
            "topic": "Listening",
            "reading_passage": "AUDIO:/english/My Family and Home.mp3",
        },
        {
            "text": "What is Anna's mother's profession?",
            "options": ["Doctor", "Engineer", "Teacher", "Scientist"],
            "correct_indices": [2],
            "topic": "Listening",
            "reading_passage": "AUDIO:/english/My Family and Home.mp3",
        },
        {
            "text": "What is Anna's father's profession?",
            "options": ["Teacher", "Engineer", "Pilot", "Lawyer"],
            "correct_indices": [1],
            "topic": "Listening",
            "reading_passage": "AUDIO:/english/My Family and Home.mp3",
        },
        {
            "text": "Where does Anna's father work?",
            "options": [
                "Near their house",
                "In the city center",
                "In a small school",
                "From home",
            ],
            "correct_indices": [1],
            "topic": "Listening",
            "reading_passage": "AUDIO:/english/My Family and Home.mp3",
        },
        {
            "text": "How old is Anna's brother?",
            "options": ["Seventeen", "Twenty-three", "Ten", "Seven"],
            "correct_indices": [0],
            "topic": "Listening",
            "reading_passage": "AUDIO:/english/My Family and Home.mp3",
        },
        {
            "text": "What do they often do on weekends?",
            "options": [
                "Go shopping",
                "Travel abroad",
                "Cook dinner and watch movies",
                "Play football",
            ],
            "correct_indices": [2],
            "topic": "Listening",
            "reading_passage": "AUDIO:/english/My Family and Home.mp3",
        },
        # === LISTENING GROUP 2: At the University (8 questions) ===
        {
            "text": "Is it Marat's first day at the university?",
            "options": [
                "Yes, it is",
                "No, it's his second year",
                "No, he is a teacher",
                "He doesn't study there",
            ],
            "correct_indices": [0],
            "topic": "Listening",
            "reading_passage": "AUDIO:/english/At the University.mp3",
        },
        {
            "text": "What is Marat studying?",
            "options": ["History", "Intl Relations", "Computer Science", "Physics"],
            "correct_indices": [2],
            "topic": "Listening",
            "reading_passage": "AUDIO:/english/At the University.mp3",
        },
        {
            "text": "What is Aisha studying?",
            "options": [
                "Computer Science",
                "International Relations",
                "Medicine",
                "Arts",
            ],
            "correct_indices": [1],
            "topic": "Listening",
            "reading_passage": "AUDIO:/english/At the University.mp3",
        },
        {
            "text": "Where is the library located?",
            "options": [
                "Next to the cafeteria",
                "Opposite the park",
                "Next to the main building",
                "Far from the university",
            ],
            "correct_indices": [2],
            "topic": "Listening",
            "reading_passage": "AUDIO:/english/At the University.mp3",
        },
        {
            "text": "Does Marat know where the library is?",
            "options": [
                "Yes, he knows",
                "No, he is still learning",
                "He is the librarian",
                "He doesn't need to know",
            ],
            "correct_indices": [1],
            "topic": "Listening",
            "reading_passage": "AUDIO:/english/At the University.mp3",
        },
        {
            "text": "What time does Aisha's class finish?",
            "options": [
                "At 12 o'clock",
                "At 1 o'clock",
                "At 2 o'clock",
                "At 4 o'clock",
            ],
            "correct_indices": [2],
            "topic": "Listening",
            "reading_passage": "AUDIO:/english/At the University.mp3",
        },
        {
            "text": "Where will they go first after class?",
            "options": ["To the library", "To the cafeteria", "To the gym", "Home"],
            "correct_indices": [1],
            "topic": "Listening",
            "reading_passage": "AUDIO:/english/At the University.mp3",
        },
        {
            "text": "What will Aisha show Marat?",
            "options": ["Her class", "The library", "The cafeteria", "The whole city"],
            "correct_indices": [1],
            "topic": "Listening",
            "reading_passage": "AUDIO:/english/At the University.mp3",
        },
        # === ADDITIONAL PREFIXES & SUFFIXES (10 more) ===
        {
            "text": "What does 're-' mean in 'rewrite'?",
            "options": ["not", "before", "again", "under"],
            "correct_indices": [2],
            "topic": "Prefixes",
        },
        {
            "text": "Which word has the prefix 'pre-'?",
            "options": ["preview", "review", "view", "interview"],
            "correct_indices": [0],
            "topic": "Prefixes",
        },
        {
            "text": "The suffix '-ful' means:",
            "options": ["without", "full of", "again", "before"],
            "correct_indices": [1],
            "topic": "Prefixes",
        },
        {
            "text": "Which word has negative prefix 'in-'?",
            "options": ["inside", "incomplete", "include", "increase"],
            "correct_indices": [1],
            "topic": "Prefixes",
        },
        {
            "text": "The suffix '-less' means:",
            "options": ["full of", "without", "more", "again"],
            "correct_indices": [1],
            "topic": "Prefixes",
        },
        {
            "text": "What does 'over-' mean in 'overwork'?",
            "options": ["under", "too much", "again", "not"],
            "correct_indices": [1],
            "topic": "Prefixes",
        },
        {
            "text": "Which word means 'not legal'?",
            "options": ["legal", "illegal", "legalize", "legally"],
            "correct_indices": [1],
            "topic": "Prefixes",
        },
        {
            "text": "The prefix 'mis-' in 'misunderstand' means:",
            "options": ["correct", "wrong", "again", "before"],
            "correct_indices": [1],
            "topic": "Prefixes",
        },
        {
            "text": "Which suffix creates a noun from 'develop'?",
            "options": ["-ment", "-ful", "-less", "-able"],
            "correct_indices": [0],
            "topic": "Prefixes",
        },
        {
            "text": "The prefix 'sub-' means:",
            "options": ["above", "under", "against", "with"],
            "correct_indices": [1],
            "topic": "Prefixes",
        },
        # === READING GROUP 1: Artificial Intelligence (8 questions) ===
        {
            "text": "What is the main theme of the passage?",
            "options": [
                "History of computers",
                "Evolution of AI",
                "Robotics in medicine",
                "Internet safety",
            ],
            "correct_indices": [1],
            "topic": "Reading",
            "reading_passage": "Artificial Intelligence (AI) has rapidly advanced from a theoretical concept to a transformative technology in the 21st century. While early systems were limited to simple logic, modern machine learning models can now recognize images, translate languages, and even generate human-like text. The potential applications are vast, ranging from autonomous vehicles to personalized healthcare. However, this growth also raises ethical concerns regarding privacy, job displacement, and the need for rigorous regulation to ensure AI alignment with human values.",
        },
        {
            "text": "According to the passage, modern AI systems can:",
            "options": [
                "Only perform simple logic",
                "Recognize images and translate languages",
                "Operate without data",
                "Fix themselves without human help",
            ],
            "correct_indices": [1],
            "topic": "Reading",
            "reading_passage": "Artificial Intelligence (AI) has rapidly advanced from a theoretical concept to a transformative technology in the 21st century. While early systems were limited to simple logic, modern machine learning models can now recognize images, translate languages, and even generate human-like text. The potential applications are vast, ranging from autonomous vehicles to personalized healthcare. However, this growth also raises ethical concerns regarding privacy, job displacement, and the need for rigorous regulation to ensure AI alignment with human values.",
        },
        {
            "text": "What were early AI systems limited to?",
            "options": [
                "Generating text",
                "Simple logic",
                "Driving cars",
                "Healthcare",
            ],
            "correct_indices": [1],
            "topic": "Reading",
            "reading_passage": "Artificial Intelligence (AI) has rapidly advanced from a theoretical concept to a transformative technology in the 21st century. While early systems were limited to simple logic, modern machine learning models can now recognize images, translate languages, and even generate human-like text. The potential applications are vast, ranging from autonomous vehicles to personalized healthcare. However, this growth also raises ethical concerns regarding privacy, job displacement, and the need for rigorous regulation to ensure AI alignment with human values.",
        },
        {
            "text": "Which application is NOT mentioned in the text?",
            "options": [
                "Autonomous vehicles",
                "Personalized healthcare",
                "Robotic surgery",
                "Language translation",
            ],
            "correct_indices": [2],
            "topic": "Reading",
            "reading_passage": "Artificial Intelligence (AI) has rapidly advanced from a theoretical concept to a transformative technology in the 21st century. While early systems were limited to simple logic, modern machine learning models can now recognize images, translate languages, and even generate human-like text. The potential applications are vast, ranging from autonomous vehicles to personalized healthcare. However, this growth also raises ethical concerns regarding privacy, job displacement, and the need for rigorous regulation to ensure AI alignment with human values.",
        },
        {
            "text": "What ethical concern is cited regarding AI?",
            "options": [
                "High electricity costs",
                "Job displacement",
                "Lack of memory",
                "Slow processing speed",
            ],
            "correct_indices": [1],
            "topic": "Reading",
            "reading_passage": "Artificial Intelligence (AI) has rapidly advanced from a theoretical concept to a transformative technology in the 21st century. While early systems were limited to simple logic, modern machine learning models can now recognize images, translate languages, and even generate human-like text. The potential applications are vast, ranging from autonomous vehicles to personalized healthcare. However, this growth also raises ethical concerns regarding privacy, job displacement, and the need for rigorous regulation to ensure AI alignment with human values.",
        },
        {
            "text": "What is needed to ensure AI alignment with human values?",
            "options": [
                "Faster processors",
                "Rigorous regulation",
                "More data",
                "Cheaper hardware",
            ],
            "correct_indices": [1],
            "topic": "Reading",
            "reading_passage": "Artificial Intelligence (AI) has rapidly advanced from a theoretical concept to a transformative technology in the 21st century. While early systems were limited to simple logic, modern machine learning models can now recognize images, translate languages, and even generate human-like text. The potential applications are vast, ranging from autonomous vehicles to personalized healthcare. However, this growth also raises ethical concerns regarding privacy, job displacement, and the need for rigorous regulation to ensure AI alignment with human values.",
        },
        {
            "text": "The word 'transformative' in the text most likely means:",
            "options": [
                "Harmful",
                "Significant and life-changing",
                "Temporary",
                "Ancient",
            ],
            "correct_indices": [1],
            "topic": "Reading",
            "reading_passage": "Artificial Intelligence (AI) has rapidly advanced from a theoretical concept to a transformative technology in the 21st century. While early systems were limited to simple logic, modern machine learning models can now recognize images, translate languages, and even generate human-like text. The potential applications are vast, ranging from autonomous vehicles to personalized healthcare. However, this growth also raises ethical concerns regarding privacy, job displacement, and the need for rigorous regulation to ensure AI alignment with human values.",
        },
        {
            "text": "In what century did AI become a transformative technology?",
            "options": ["19th", "20th", "21st", "22nd"],
            "correct_indices": [2],
            "topic": "Reading",
            "reading_passage": "Artificial Intelligence (AI) has rapidly advanced from a theoretical concept to a transformative technology in the 21st century. While early systems were limited to simple logic, modern machine learning models can now recognize images, translate languages, and even generate human-like text. The potential applications are vast, ranging from autonomous vehicles to personalized healthcare. However, this growth also raises ethical concerns regarding privacy, job displacement, and the need for rigorous regulation to ensure AI alignment with human values.",
        },
        # === READING GROUP 2: Climate Change (8 questions) ===
        {
            "text": "What is the primary cause of global warming mentioned?",
            "options": [
                "Solar flares",
                "Greenhouse gas emissions",
                "Volcanic activity",
                "Ocean currents",
            ],
            "correct_indices": [1],
            "topic": "Reading",
            "reading_passage": "Climate change is one of the most pressing challenges of our time. Scientific evidence clearly shows that the Earth's average temperature is rising due to increased levels of greenhouse gases in the atmosphere, primarily from human activities such as burning fossil fuels and deforestation. This global warming leads to melting polar ice caps, rising sea levels, and more frequent extreme weather events. To mitigate these effects, many nations are transitioning to renewable energy sources like wind and solar power, emphasizing the importance of international cooperation in reducing carbon footprints.",
        },
        {
            "text": "Which human activity contributes to climate change according to the text?",
            "options": [
                "Planting trees",
                "Burning fossil fuels",
                "Recycling plastic",
                "Using solar energy",
            ],
            "correct_indices": [1],
            "topic": "Reading",
            "reading_passage": "Climate change is one of the most pressing challenges of our time. Scientific evidence clearly shows that the Earth's average temperature is rising due to increased levels of greenhouse gases in the atmosphere, primarily from human activities such as burning fossil fuels and deforestation. This global warming leads to melting polar ice caps, rising sea levels, and more frequent extreme weather events. To mitigate these effects, many nations are transitioning to renewable energy sources like wind and solar power, emphasizing the importance of international cooperation in reducing carbon footprints.",
        },
        {
            "text": "Global warming causes which of the following?",
            "options": [
                "Lower sea levels",
                "Melting polar ice caps",
                "Less frequent weather events",
                "Cooler summers",
            ],
            "correct_indices": [1],
            "topic": "Reading",
            "reading_passage": "Climate change is one of the most pressing challenges of our time. Scientific evidence clearly shows that the Earth's average temperature is rising due to increased levels of greenhouse gases in the atmosphere, primarily from human activities such as burning fossil fuels and deforestation. This global warming leads to melting polar ice caps, rising sea levels, and more frequent extreme weather events. To mitigate these effects, many nations are transitioning to renewable energy sources like wind and solar power, emphasizing the importance of international cooperation in reducing carbon footprints.",
        },
        {
            "text": "What are nations doing to mitigate climate change?",
            "options": [
                "Burning more coal",
                "Transitioning to renewable energy",
                "Ignoring international treaties",
                "Cutting down forests",
            ],
            "correct_indices": [1],
            "topic": "Reading",
            "reading_passage": "Climate change is one of the most pressing challenges of our time. Scientific evidence clearly shows that the Earth's average temperature is rising due to increased levels of greenhouse gases in the atmosphere, primarily from human activities such as burning fossil fuels and deforestation. This global warming leads to melting polar ice caps, rising sea levels, and more frequent extreme weather events. To mitigate these effects, many nations are transitioning to renewable energy sources like wind and solar power, emphasizing the importance of international cooperation in reducing carbon footprints.",
        },
        {
            "text": "What is emphasized as important for reducing carbon footprints?",
            "options": [
                "Competition",
                "International cooperation",
                "Local isolation",
                "Higher prices",
            ],
            "correct_indices": [1],
            "topic": "Reading",
            "reading_passage": "Climate change is one of the most pressing challenges of our time. Scientific evidence clearly shows that the Earth's average temperature is rising due to increased levels of greenhouse gases in the atmosphere, primarily from human activities such as burning fossil fuels and deforestation. This global warming leads to melting polar ice caps, rising sea levels, and more frequent extreme weather events. To mitigate these effects, many nations are transitioning to renewable energy sources like wind and solar power, emphasizing the importance of international cooperation in reducing carbon footprints.",
        },
        {
            "text": "De-forestation means:",
            "options": [
                "Planting new forests",
                "Cutting down trees in large areas",
                "Protecting wildlife",
                "Cleaning oceans",
            ],
            "correct_indices": [1],
            "topic": "Reading",
            "reading_passage": "Climate change is one of the most pressing challenges of our time. Scientific evidence clearly shows that the Earth's average temperature is rising due to increased levels of greenhouse gases in the atmosphere, primarily from human activities such as burning fossil fuels and deforestation. This global warming leads to melting polar ice caps, rising sea levels, and more frequent extreme weather events. To mitigate these effects, many nations are transitioning to renewable energy sources like wind and solar power, emphasizing the importance of international cooperation in reducing carbon footprints.",
        },
        {
            "text": "Wind and solar power are examples of:",
            "options": [
                "Fossil fuels",
                "Renewable energy",
                "Non-recyclable materials",
                "Pollutants",
            ],
            "correct_indices": [1],
            "topic": "Reading",
            "reading_passage": "Climate change is one of the most pressing challenges of our time. Scientific evidence clearly shows that the Earth's average temperature is rising due to increased levels of greenhouse gases in the atmosphere, primarily from human activities such as burning fossil fuels and deforestation. This global warming leads to melting polar ice caps, rising sea levels, and more frequent extreme weather events. To mitigate these effects, many nations are transitioning to renewable energy sources like wind and solar power, emphasizing the importance of international cooperation in reducing carbon footprints.",
        },
        {
            "text": "The main purpose of the text is to:",
            "options": [
                "Sell solar panels",
                "Inform about climate change",
                "Promote car sales",
                "Criticize scientists",
            ],
            "correct_indices": [1],
            "topic": "Reading",
            "reading_passage": "Climate change is one of the most pressing challenges of our time. Scientific evidence clearly shows that the Earth's average temperature is rising due to increased levels of greenhouse gases in the atmosphere, primarily from human activities such as burning fossil fuels and deforestation. This global warming leads to melting polar ice caps, rising sea levels, and more frequent extreme weather events. To mitigate these effects, many nations are transitioning to renewable energy sources like wind and solar power, emphasizing the importance of international cooperation in reducing carbon footprints.",
        },
    ],
    SubjectId.TGO: [
        # Mathematical Logic - Comparison
        {
            "text": "A бағаны: 200-дің 10%-ы. B бағаны: 20. Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [2],
            "topic": "Салыстыру есептері",
        },
        {
            "text": "A бағаны: 210-ның 13%-ы. B бағаны: 215-тің 12%-ы. Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [0],
            "topic": "Салыстыру есептері",
        },
        {
            "text": "A бағаны: 50-нің 20%-ы. B бағаны: 40-тың 25%-ы. Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [2],
            "topic": "Салыстыру есептері",
        },
        {
            "text": "A бағаны: 0.5 × 100. B бағаны: 100 ÷ 2. Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [2],
            "topic": "Салыстыру есептері",
        },
        # Mathematical Logic - Word Problems
        {
            "text": "Машина 60 км/сағ жылдамдықпен 3 сағат жүрді. Қанша жол жүрді?",
            "options": ["120 км", "180 км", "200 км", "240 км"],
            "correct_indices": [1],
            "topic": "Жылдамдық есептері",
        },
        {
            "text": "S = v × t формуласында S нені білдіреді?",
            "options": ["Жылдамдық", "Уақыт", "Қашықтық (жол)", "Жеделдету"],
            "correct_indices": [2],
            "topic": "Жылдамдық есептері",
        },
        {
            "text": "Тауар бағасы 5000 теңге. 20% жеңілдік болса, соңғы баға қанша?",
            "options": ["4000 теңге", "4500 теңге", "3500 теңге", "5500 теңге"],
            "correct_indices": [0],
            "topic": "Пайыздар",
        },
        {
            "text": "Жұмысты А 6 сағатта, Б 3 сағатта орындайды. Бірге істесе қанша сағатта бітеді?",
            "options": ["4 сағат", "3 сағат", "2 сағат", "9 сағат"],
            "correct_indices": [2],
            "topic": "Бірлескен жұмыс",
        },
        # Mathematical Logic - Inequalities
        {
            "text": "2x + 3 ≤ 15 теңсіздігінің шешімі қандай?",
            "options": ["x ≤ 6", "x ≤ 9", "x ≥ 6", "x = 6"],
            "correct_indices": [0],
            "topic": "Теңсіздіктер",
        },
        {
            "text": "Теңсіздік дегеніміз не?",
            "options": [
                "Екі шаманың теңдігі",
                "Айнымалының белгілі бір шектен үлкен/кіші екенін көрсететін өрнек",
                "Функция түрі",
                "Цикл операторы",
            ],
            "correct_indices": [1],
            "topic": "Теңсіздіктер",
        },
        # Analytical Thinking - Number Sequences
        {
            "text": "Сан тізбегін жалғастырыңыз: 2, 4, 8, 16, ...",
            "options": ["20", "24", "32", "64"],
            "correct_indices": [2],
            "topic": "Сандық қатарлар",
        },
        {
            "text": "Сан тізбегін жалғастырыңыз: 1, 1, 2, 3, 5, 8, ...",
            "options": ["10", "11", "12", "13"],
            "correct_indices": [3],
            "topic": "Сандық қатарлар",
        },
        {
            "text": "Сан тізбегін жалғастырыңыз: 3, 6, 9, 12, ...",
            "options": ["14", "15", "16", "18"],
            "correct_indices": [1],
            "topic": "Сандық қатарлар",
        },
        {
            "text": "Сан тізбегін жалғастырыңыз: 1, 4, 9, 16, 25, ...",
            "options": ["30", "36", "49", "64"],
            "correct_indices": [1],
            "topic": "Сандық қатарлар",
        },
        {
            "text": "Сан тізбегін жалғастырыңыз: 100, 50, 25, ...",
            "options": ["10", "12.5", "15", "20"],
            "correct_indices": [1],
            "topic": "Сандық қатарлар",
        },
        # Analytical Thinking - Probability
        {
            "text": "Қапта 3 ақ және 2 қара шар бар. Кездейсоқ алынған шардың ақ болу ықтималдығы қандай?",
            "options": ["2/5", "3/5", "1/2", "1/5"],
            "correct_indices": [1],
            "topic": "Ықтималдық",
        },
        {
            "text": "Зар лақтырғанда 6 түсу ықтималдығы қандай?",
            "options": ["1/6", "1/3", "1/2", "1"],
            "correct_indices": [0],
            "topic": "Ықтималдық",
        },
        {
            "text": "Ықтималдық дегеніміз не?",
            "options": [
                "Сандар қосындысы",
                "Оқиғаның орындалу мүмкіндігі",
                "Теңдеу шешімі",
                "Функция мәні",
            ],
            "correct_indices": [1],
            "topic": "Ықтималдық",
        },
        # Analytical Thinking - Combinatorics
        {
            "text": "3 түрлі кітапты сөреге неше түрлі тәсілмен орналастыруға болады?",
            "options": ["3", "6", "9", "12"],
            "correct_indices": [1],
            "topic": "Комбинаторика",
        },
        {
            "text": "4 адамнан 2 адамды таңдаудың неше жолы бар?",
            "options": ["4", "6", "8", "12"],
            "correct_indices": [1],
            "topic": "Комбинаторика",
        },
        # Critical Thinking - Text Analysis
        {
            "text": "Main idea (негізгі ой) дегеніміз не?",
            "options": [
                "Мәтіннің соңғы сөйлемі",
                "Мәтіннің басты ойы",
                "Автордың аты",
                "Мәтіннің атауы",
            ],
            "correct_indices": [1],
            "topic": "Мәтінді талдау",
        },
        {
            "text": "Мәтінді талдау кезінде ең алдымен не анықталады?",
            "options": [
                "Сөздер саны",
                "Автордың негізгі ойы",
                "Беттер саны",
                "Жазылған күні",
            ],
            "correct_indices": [1],
            "topic": "Мәтінді талдау",
        },
        {
            "text": "Екі мәтінді салыстырғанда қандай аспектілер қарастырылады?",
            "options": [
                "Тек ұқсастық",
                "Тек айырмашылық",
                "Ұқсастық, айырмашылық, стиль, мақсат",
                "Тек автор",
            ],
            "correct_indices": [2],
            "topic": "Мәтінді талдау",
        },
        {
            "text": "Логикалық қорытынды жасау нені талап етеді?",
            "options": [
                "Мәтінді көшіріп жазу",
                "Мәтіндегі ақпаратқа сүйеніп тұжырым жасау",
                "Мәтінді аудару",
                "Автормен сұхбат жасау",
            ],
            "correct_indices": [1],
            "topic": "Сыни ойлау",
        },
        {
            "text": "Сыни ойлау дегеніміз не?",
            "options": [
                "Мәтінді жаттау",
                "Ақпаратты талдап, бағалай білу",
                "Тез оқу",
                "Көп жазу",
            ],
            "correct_indices": [1],
            "topic": "Сыни ойлау",
        },
        # Tables and Graphs
        {
            "text": "Кестедегі деректерді талдау кезінде не маңызды?",
            "options": [
                "Түстер",
                "Трендті табу және салыстыру",
                "Кесте өлшемі",
                "Қаріп түрі",
            ],
            "correct_indices": [1],
            "topic": "Кестелер мен графиктер",
        },
        {
            "text": "Графикте көрсетілген өсу трендін қалай анықтауға болады?",
            "options": [
                "Сызық төмен түседі",
                "Сызық жоғары көтеріледі",
                "Сызық тұрақты",
                "Сызық жоқ",
            ],
            "correct_indices": [1],
            "topic": "Кестелер мен графиктер",
        },
        # Additional Math Logic
        {
            "text": "5! (факториал) неге тең?",
            "options": ["25", "120", "60", "100"],
            "correct_indices": [1],
            "topic": "Математикалық логика",
        },
        {
            "text": "Екі поезд қарама-қарсы бағытта 60 км/сағ және 80 км/сағ жылдамдықпен жүріп, 2 сағаттан кейін қашықтықтары қанша болады?",
            "options": ["140 км", "280 км", "200 км", "320 км"],
            "correct_indices": [1],
            "topic": "Жылдамдық есептері",
        },
        {
            "text": "Үшбұрыштың ішкі бұрыштарының қосындысы неге тең?",
            "options": ["90°", "180°", "270°", "360°"],
            "correct_indices": [1],
            "topic": "Геометрия",
        },
        {
            "text": "Шаршының периметрі 40 см. Қабырғасы қанша?",
            "options": ["8 см", "10 см", "20 см", "40 см"],
            "correct_indices": [1],
            "topic": "Геометрия",
        },
        {
            "text": "Егер x + 5 = 12 болса, x неге тең?",
            "options": ["5", "7", "12", "17"],
            "correct_indices": [1],
            "topic": "Алгебра",
        },
        # === ADDITIONAL САЛЫСТЫРУ ЕСЕПТЕРІ (15 more) ===
        {
            "text": "A бағаны: 300-дің 15%-ы. B бағаны: 45. Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [2],
            "topic": "Салыстыру есептері",
        },
        {
            "text": "A бағаны: 1000-ның 5%-ы. B бағаны: 500-дің 10%-ы. Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [2],
            "topic": "Салыстыру есептері",
        },
        {
            "text": "A бағаны: 80-нің 25%-ы. B бағаны: 60-тың 30%-ы. Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [0],
            "topic": "Салыстыру есептері",
        },
        {
            "text": "A бағаны: √144. B бағаны: 11. Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [0],
            "topic": "Салыстыру есептері",
        },
        {
            "text": "A бағаны: 2³. B бағаны: 3². Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [1],
            "topic": "Салыстыру есептері",
        },
        {
            "text": "A бағаны: 0.25. B бағаны: 1/4. Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [2],
            "topic": "Салыстыру есептері",
        },
        {
            "text": "A бағаны: 150-нің 40%-ы. B бағаны: 200-дің 30%-ы. Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [2],
            "topic": "Салыстыру есептері",
        },
        {
            "text": "A бағаны: 7 × 8. B бағаны: 9 × 6. Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [0],
            "topic": "Салыстыру есептері",
        },
        {
            "text": "A бағаны: 15² - 10². B бағаны: 125. Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [2],
            "topic": "Салыстыру есептері",
        },
        {
            "text": "A бағаны: 1/3 + 1/6. B бағаны: 1/2. Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [2],
            "topic": "Салыстыру есептері",
        },
        {
            "text": "A бағаны: 0.6 × 50. B бағаны: 0.3 × 100. Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [2],
            "topic": "Салыстыру есептері",
        },
        {
            "text": "A бағаны: 90 ÷ 6. B бағаны: 45 ÷ 3. Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [2],
            "topic": "Салыстыру есептері",
        },
        {
            "text": "A бағаны: 4! B бағаны: 20. Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [0],
            "topic": "Салыстыру есептері",
        },
        {
            "text": "A бағаны: √81 + √16. B бағаны: 12. Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [0],
            "topic": "Салыстыру есептері",
        },
        {
            "text": "A бағаны: 250-нің 8%-ы. B бағаны: 400-дің 5%-ы. Салыстырыңыз.",
            "options": ["A > B", "A < B", "A = B", "Анықтау мүмкін емес"],
            "correct_indices": [2],
            "topic": "Салыстыру есептері",
        },
        # === ADDITIONAL ЖЫЛДАМДЫҚ ЕСЕПТЕРІ (10 more) ===
        {
            "text": "Велосипедші 15 км/сағ жылдамдықпен 2 сағат жүрді. Жүрген жолы неше км?",
            "options": ["20 км", "25 км", "30 км", "35 км"],
            "correct_indices": [2],
            "topic": "Жылдамдық есептері",
        },
        {
            "text": "Машина 240 км жолды 4 сағатта жүрді. Жылдамдығы қандай?",
            "options": ["50 км/сағ", "60 км/сағ", "70 км/сағ", "80 км/сағ"],
            "correct_indices": [1],
            "topic": "Жылдамдық есептері",
        },
        {
            "text": "Пойыз 90 км/сағ жылдамдықпен 450 км жолды қанша сағатта жүреді?",
            "options": ["4 сағат", "5 сағат", "6 сағат", "7 сағат"],
            "correct_indices": [1],
            "topic": "Жылдамдық есептері",
        },
        {
            "text": "v = S/t формуласында v нені білдіреді?",
            "options": ["Жол", "Уақыт", "Жылдамдық", "Үдеу"],
            "correct_indices": [2],
            "topic": "Жылдамдық есептері",
        },
        {
            "text": "Екі адам қарама-қарсы бағытта жүрсе, олардың арақашықтығы қалай өзгереді?",
            "options": ["Азаяды", "Өзгермейді", "Артады", "Анықтау мүмкін емес"],
            "correct_indices": [2],
            "topic": "Жылдамдық есептері",
        },
        {
            "text": "Жаяу адам 5 км/сағ жылдамдықпен 3 сағатта қанша жол жүреді?",
            "options": ["10 км", "12 км", "15 км", "18 км"],
            "correct_indices": [2],
            "topic": "Жылдамдық есептері",
        },
        {
            "text": "Ұшақ 800 км/сағ жылдамдықпен 2400 км ұшты. Қанша уақыт кетті?",
            "options": ["2 сағат", "3 сағат", "4 сағат", "5 сағат"],
            "correct_indices": [1],
            "topic": "Жылдамдық есептері",
        },
        {
            "text": "Екі қала арасы 300 км. Машина 4 сағатта жетті. Орташа жылдамдық қандай?",
            "options": ["65 км/сағ", "70 км/сағ", "75 км/сағ", "80 км/сағ"],
            "correct_indices": [2],
            "topic": "Жылдамдық есептері",
        },
        {
            "text": "Велосипедші 12 км жолды 30 минутта жүрді. Жылдамдығы қандай?",
            "options": ["20 км/сағ", "24 км/сағ", "36 км/сағ", "40 км/сағ"],
            "correct_indices": [1],
            "topic": "Жылдамдық есептері",
        },
        {
            "text": "Жүргіш 20 км/сағ жылдамдықпен қозғалса, 100 км-ге қанша уақыт кетеді?",
            "options": ["4 сағат", "5 сағат", "6 сағат", "7 сағат"],
            "correct_indices": [1],
            "topic": "Жылдамдық есептері",
        },
        # === ADDITIONAL ПАЙЫЗДАР (15 more) ===
        {
            "text": "120-ның 25%-ы қанша?",
            "options": ["25", "30", "35", "40"],
            "correct_indices": [1],
            "topic": "Пайыздар",
        },
        {
            "text": "Тауар бағасы 8000 теңге. 15% жеңілдіктен кейінгі баға қанша?",
            "options": ["6000 теңге", "6500 теңге", "6800 теңге", "7200 теңге"],
            "correct_indices": [2],
            "topic": "Пайыздар",
        },
        {
            "text": "Жалақы 200000 теңге. 10% қосымша берілсе, барлығы қанша?",
            "options": ["210000 теңге", "220000 теңге", "230000 теңге", "240000 теңге"],
            "correct_indices": [1],
            "topic": "Пайыздар",
        },
        {
            "text": "60 студенттің 40%-ы қыздар. Қанша қыз?",
            "options": ["20", "24", "28", "30"],
            "correct_indices": [1],
            "topic": "Пайыздар",
        },
        {
            "text": "Банкке 100000 теңге салынды. Жылына 12% пайда болса, 1 жылда қанша болады?",
            "options": ["110000", "112000", "115000", "120000"],
            "correct_indices": [1],
            "topic": "Пайыздар",
        },
        {
            "text": "Саны 50. Оның 1%-ы қанша?",
            "options": ["0.5", "1", "5", "50"],
            "correct_indices": [0],
            "topic": "Пайыздар",
        },
        {
            "text": "180 теңгеден 20 теңге шегерілді. Неше пайыз жеңілдік?",
            "options": ["10%", "11%", "12%", "15%"],
            "correct_indices": [1],
            "topic": "Пайыздар",
        },
        {
            "text": "Тауар бағасы 25% көтерілді және 5000 теңге болды. Бастапқы баға қандай?",
            "options": ["3750", "4000", "4500", "4750"],
            "correct_indices": [1],
            "topic": "Пайыздар",
        },
        {
            "text": "500-дің 100%-ы неге тең?",
            "options": ["50", "100", "250", "500"],
            "correct_indices": [3],
            "topic": "Пайыздар",
        },
        {
            "text": "Кітаптың бағасы 30% арзандады. Енді 2100 теңге. Бастапқы баға?",
            "options": ["2730", "3000", "3150", "3500"],
            "correct_indices": [1],
            "topic": "Пайыздар",
        },
        {
            "text": "45 минут 1 сағаттың неше пайызы?",
            "options": ["45%", "55%", "65%", "75%"],
            "correct_indices": [3],
            "topic": "Пайыздар",
        },
        {
            "text": "Автомобиль бағасы 10% төмендеді, содан кейін тағы 10% төмендеді. Жалпы неше % төмендеді?",
            "options": ["19%", "20%", "21%", "22%"],
            "correct_indices": [0],
            "topic": "Пайыздар",
        },
        {
            "text": "400-дің 75%-ы қанша?",
            "options": ["275", "300", "325", "350"],
            "correct_indices": [1],
            "topic": "Пайыздар",
        },
        {
            "text": "90 теңге 300 теңгенің неше пайызы?",
            "options": ["25%", "30%", "35%", "40%"],
            "correct_indices": [1],
            "topic": "Пайыздар",
        },
        {
            "text": "Бастапқы баға 2000 теңге. 50% жеңілдіктен кейінгі баға?",
            "options": ["800", "1000", "1200", "1500"],
            "correct_indices": [1],
            "topic": "Пайыздар",
        },
        # === ADDITIONAL БІРЛЕСКЕН ЖҰМЫС (10 more) ===
        {
            "text": "А жұмысты 4 сағатта, Б 6 сағатта бітіреді. Бірге істесе қанша сағат?",
            "options": ["2.4 сағат", "3 сағат", "4 сағат", "5 сағат"],
            "correct_indices": [0],
            "topic": "Бірлескен жұмыс",
        },
        {
            "text": "Бір кран бассейнді 3 сағатта толтырады, екіншісі 6 сағатта. Екеуі бірге қанша сағатта толтырады?",
            "options": ["1 сағат", "2 сағат", "3 сағат", "4 сағат"],
            "correct_indices": [1],
            "topic": "Бірлескен жұмыс",
        },
        {
            "text": "3 жұмысшы жұмысты 6 күнде бітіреді. 6 жұмысшы қанша күнде бітіреді?",
            "options": ["2 күн", "3 күн", "4 күн", "12 күн"],
            "correct_indices": [1],
            "topic": "Бірлескен жұмыс",
        },
        {
            "text": "1 адам жұмысты 12 сағатта бітіреді. 4 адам бірге істесе қанша сағатта?",
            "options": ["3 сағат", "4 сағат", "6 сағат", "8 сағат"],
            "correct_indices": [0],
            "topic": "Бірлескен жұмыс",
        },
        {
            "text": "А жұмыстың 1/5 бөлігін 2 сағатта бітіреді. Бүкіл жұмысты қанша сағатта бітіреді?",
            "options": ["8 сағат", "10 сағат", "12 сағат", "15 сағат"],
            "correct_indices": [1],
            "topic": "Бірлескен жұмыс",
        },
        {
            "text": "Егер 5 адам жұмысты 10 күнде бітірсе, 10 адам қанша күнде бітіреді?",
            "options": ["3 күн", "4 күн", "5 күн", "20 күн"],
            "correct_indices": [2],
            "topic": "Бірлескен жұмыс",
        },
        {
            "text": "А мен Б бірге жұмысты 4 сағатта бітіреді. А жалғыз 6 сағатта бітіреді. Б жалғыз неше сағатта?",
            "options": ["8 сағат", "10 сағат", "12 сағат", "14 сағат"],
            "correct_indices": [2],
            "topic": "Бірлескен жұмыс",
        },
        {
            "text": "Құбыр бассейнді 5 сағатта толтырады. 3 сағатта бассейннің қанша бөлігі толады?",
            "options": ["1/5", "2/5", "3/5", "4/5"],
            "correct_indices": [2],
            "topic": "Бірлескен жұмыс",
        },
        {
            "text": "2 трактор егістікті 6 сағатта жырта алады. 3 трактор қанша сағатта жыртады?",
            "options": ["3 сағат", "4 сағат", "5 сағат", "9 сағат"],
            "correct_indices": [1],
            "topic": "Бірлескен жұмыс",
        },
        {
            "text": "Жұмыс ставкасы 1000 теңге/сағ. 8 сағат жұмыс істегенде қанша ақша алады?",
            "options": ["6000", "7000", "8000", "9000"],
            "correct_indices": [2],
            "topic": "Бірлескен жұмыс",
        },
        # === ADDITIONAL САНДЫҚ ҚАТАРЛАР (15 more) ===
        {
            "text": "Тізбекті жалғастырыңыз: 5, 10, 15, 20, ...",
            "options": ["22", "24", "25", "30"],
            "correct_indices": [2],
            "topic": "Сандық қатарлар",
        },
        {
            "text": "Тізбекті жалғастырыңыз: 2, 6, 18, 54, ...",
            "options": ["108", "162", "216", "270"],
            "correct_indices": [1],
            "topic": "Сандық қатарлар",
        },
        {
            "text": "Тізбекті жалғастырыңыз: 1, 3, 6, 10, 15, ...",
            "options": ["18", "20", "21", "25"],
            "correct_indices": [2],
            "topic": "Сандық қатарлар",
        },
        {
            "text": "Тізбекті жалғастырыңыз: 64, 32, 16, 8, ...",
            "options": ["2", "4", "6", "0"],
            "correct_indices": [1],
            "topic": "Сандық қатарлар",
        },
        {
            "text": "Тізбекті жалғастырыңыз: 1, 2, 4, 7, 11, ...",
            "options": ["14", "15", "16", "17"],
            "correct_indices": [2],
            "topic": "Сандық қатарлар",
        },
        {
            "text": "Тізбекті жалғастырыңыз: 0, 1, 1, 2, 3, 5, ...",
            "options": ["6", "7", "8", "9"],
            "correct_indices": [2],
            "topic": "Сандық қатарлар",
        },
        {
            "text": "Тізбекті жалғастырыңыз: 3, 5, 7, 9, ...",
            "options": ["10", "11", "12", "13"],
            "correct_indices": [1],
            "topic": "Сандық қатарлар",
        },
        {
            "text": "Тізбекті жалғастырыңыз: 1, 8, 27, 64, ...",
            "options": ["100", "125", "150", "216"],
            "correct_indices": [1],
            "topic": "Сандық қатарлар",
        },
        {
            "text": "Тізбекті жалғастырыңыз: 2, 3, 5, 7, 11, 13, ...",
            "options": ["15", "17", "19", "21"],
            "correct_indices": [1],
            "topic": "Сандық қатарлар",
        },
        {
            "text": "Тізбекті жалғастырыңыз: 10, 20, 40, 80, ...",
            "options": ["100", "120", "140", "160"],
            "correct_indices": [3],
            "topic": "Сандық қатарлар",
        },
        {
            "text": "Тізбектегі заңдылық: 1, 4, 9, 16, 25. Бұл қандай сандар?",
            "options": ["Жұп сандар", "Тақ сандар", "Квадраттар", "Кубтар"],
            "correct_indices": [2],
            "topic": "Сандық қатарлар",
        },
        {
            "text": "Тізбекті жалғастырыңыз: 100, 95, 90, 85, ...",
            "options": ["78", "80", "82", "84"],
            "correct_indices": [1],
            "topic": "Сандық қатарлар",
        },
        {
            "text": "Тізбекті жалғастырыңыз: 1, 2, 6, 24, ...",
            "options": ["48", "72", "96", "120"],
            "correct_indices": [3],
            "topic": "Сандық қатарлар",
        },
        {
            "text": "Fibonacci тізбегінің алғашқы 7 мүшесі: 0, 1, 1, 2, 3, 5, ?",
            "options": ["6", "7", "8", "10"],
            "correct_indices": [2],
            "topic": "Сандық қатарлар",
        },
        {
            "text": "Тізбекті жалғастырыңыз: 7, 14, 28, 56, ...",
            "options": ["84", "98", "112", "126"],
            "correct_indices": [2],
            "topic": "Сандық қатарлар",
        },
        # === ADDITIONAL ЫҚТИМАЛДЫҚ (10 more) ===
        {
            "text": "Монетаны лақтырғанда герб түсу ықтималдығы қандай?",
            "options": ["1/4", "1/3", "1/2", "1"],
            "correct_indices": [2],
            "topic": "Ықтималдық",
        },
        {
            "text": "Қапта 4 қызыл, 6 көк шар бар. Көк шар алу ықтималдығы?",
            "options": ["2/5", "3/5", "1/2", "4/10"],
            "correct_indices": [1],
            "topic": "Ықтималдық",
        },
        {
            "text": "Зар лақтырғанда жұп сан түсу ықтималдығы?",
            "options": ["1/6", "1/3", "1/2", "2/3"],
            "correct_indices": [2],
            "topic": "Ықтималдық",
        },
        {
            "text": "52 картадан валет алу ықтималдығы?",
            "options": ["1/52", "1/26", "1/13", "4/52"],
            "correct_indices": [2],
            "topic": "Ықтималдық",
        },
        {
            "text": "Ықтималдық 0-ден 1-ге дейінгі сан болуы керек. Бұл дұрыс па?",
            "options": ["Иә", "Жоқ", "Кейде", "Анықтау мүмкін емес"],
            "correct_indices": [0],
            "topic": "Ықтималдық",
        },
        {
            "text": "Мүмкін емес оқиғаның ықтималдығы қандай?",
            "options": ["0", "1", "0.5", "-1"],
            "correct_indices": [0],
            "topic": "Ықтималдық",
        },
        {
            "text": "Сөзсіз болатын оқиғаның ықтималдығы қандай?",
            "options": ["0", "0.5", "1", "2"],
            "correct_indices": [2],
            "topic": "Ықтималдық",
        },
        {
            "text": "10 билеттің 3-і ұтысты. Кездейсоқ билет алғанда ұтыс түсу ықтималдығы?",
            "options": ["0.2", "0.3", "0.5", "0.7"],
            "correct_indices": [1],
            "topic": "Ықтималдық",
        },
        {
            "text": "Зар лақтырғанда 7 түсу ықтималдығы?",
            "options": ["0", "1/6", "1/7", "1"],
            "correct_indices": [0],
            "topic": "Ықтималдық",
        },
        {
            "text": "Қапта 5 ақ, 5 қара шар. Бір шар алғанда ақ шар түсу ықтималдығы?",
            "options": ["0.25", "0.4", "0.5", "0.6"],
            "correct_indices": [2],
            "topic": "Ықтималдық",
        },
        # === ADDITIONAL КОМБИНАТОРИКА (10 more) ===
        {
            "text": "5! (5 факториал) неге тең?",
            "options": ["60", "100", "120", "150"],
            "correct_indices": [2],
            "topic": "Комбинаторика",
        },
        {
            "text": "4 түсті жалаушаны неше түрлі ретпен орналастыруға болады?",
            "options": ["12", "16", "20", "24"],
            "correct_indices": [3],
            "topic": "Комбинаторика",
        },
        {
            "text": "5 адамнан 3 адамды таңдау жолдарының саны?",
            "options": ["8", "10", "12", "15"],
            "correct_indices": [1],
            "topic": "Комбинаторика",
        },
        {
            "text": "2 әріптен (A, B) барлық мүмкін 2-орынды сөздер саны?",
            "options": ["2", "3", "4", "6"],
            "correct_indices": [2],
            "topic": "Комбинаторика",
        },
        {
            "text": "3 блюдодан тамақты таңдау: 4 бірінші, 3 екінші, 2 үшінші. Барлық жолдар?",
            "options": ["9", "18", "24", "36"],
            "correct_indices": [2],
            "topic": "Комбинаторика",
        },
        {
            "text": "6 адамнан бригадир таңдау жолдарының саны?",
            "options": ["5", "6", "7", "8"],
            "correct_indices": [1],
            "topic": "Комбинаторика",
        },
        {
            "text": "n! формуласында '!' не білдіреді?",
            "options": ["Қосу", "Алу", "Көбейту (факториал)", "Бөлу"],
            "correct_indices": [2],
            "topic": "Комбинаторика",
        },
        {
            "text": "0! неге тең?",
            "options": ["0", "1", "∞", "Анықталмаған"],
            "correct_indices": [1],
            "topic": "Комбинаторика",
        },
        {
            "text": "10 ойыншыдан 2 капитан таңдау жолдарының саны?",
            "options": ["20", "45", "90", "100"],
            "correct_indices": [1],
            "topic": "Комбинаторика",
        },
        {
            "text": "3 × 2 × 1 = ?",
            "options": ["3", "5", "6", "9"],
            "correct_indices": [2],
            "topic": "Комбинаторика",
        },
        # === ADDITIONAL МӘТІНДІ ТАЛДАУ / СЫНИ ОЙЛАУ (15 more) ===
        {
            "text": "Мәтінде 'Итжейде' туралы айтылса, бұл қандай тақырып?",
            "options": ["География", "Тарих", "Мәдениет/Дәстүр", "Математика"],
            "correct_indices": [2],
            "topic": "Мәтінді талдау",
        },
        {
            "text": "Мемлекеттік ту символдары туралы мәтін қандай салаға жатады?",
            "options": ["Экономика", "Саясат/Мемлекет", "Спорт", "Медицина"],
            "correct_indices": [1],
            "topic": "Мәтінді талдау",
        },
        {
            "text": "Мәтіннен тікелей табуға болатын ақпарат қалай аталады?",
            "options": ["Жанама ақпарат", "Ашық ақпарат", "Жасырын ақпарат", "Болжам"],
            "correct_indices": [1],
            "topic": "Мәтінді талдау",
        },
        {
            "text": "'Мәтінге сүйене отырып тұжырым жасау' не талап етеді?",
            "options": [
                "Мәтінді көшіру",
                "Логикалық ойлау және дәлелдеу",
                "Сандарды есептеу",
                "Аудару",
            ],
            "correct_indices": [1],
            "topic": "Сыни ойлау",
        },
        {
            "text": "Автордың негізгі ойын табу үшін не істеу керек?",
            "options": [
                "Тек бірінші абзацты оқу",
                "Бүкіл мәтінді талдау",
                "Тек соңғы сөйлемді оқу",
                "Тақырыпты қарау",
            ],
            "correct_indices": [1],
            "topic": "Мәтінді талдау",
        },
        {
            "text": "Екі мәтінді салыстырғанда 'стиль' дегеніміз не?",
            "options": [
                "Мәтіннің ұзындығы",
                "Жазу тәсілі мен тіл ерекшелігі",
                "Автордың жасы",
                "Беттер саны",
            ],
            "correct_indices": [1],
            "topic": "Мәтінді талдау",
        },
        {
            "text": "Академиялық мәтін мен көркем мәтіннің айырмасы неде?",
            "options": [
                "Тек ұзындығында",
                "Мақсаты мен стилінде",
                "Тек авторында",
                "Ешқандай айырма жоқ",
            ],
            "correct_indices": [1],
            "topic": "Мәтінді талдау",
        },
        {
            "text": "Мәтіннен берілмеген ақпаратты шығару қалай аталады?",
            "options": ["Цитата", "Қорытынды/Inference", "Аннотация", "Аударма"],
            "correct_indices": [1],
            "topic": "Сыни ойлау",
        },
        {
            "text": "Сыни оқу дегеніміз не?",
            "options": [
                "Тез оқу",
                "Ақпаратты талдай және бағалай отырып оқу",
                "Дауыстап оқу",
                "Жаттап оқу",
            ],
            "correct_indices": [1],
            "topic": "Сыни ойлау",
        },
        {
            "text": "Мәтіндегі қарама-қайшылықты анықтау қандай дағдыны қажет етеді?",
            "options": ["Жылдам оқу", "Сыни ойлау", "Жаттау", "Көшіру"],
            "correct_indices": [1],
            "topic": "Сыни ойлау",
        },
        {
            "text": "'Факт' пен 'пікірдің' айырмасы неде?",
            "options": [
                "Айырма жоқ",
                "Факт - дәлелденген ақпарат, пікір - субъективті көзқарас",
                "Пікір дәлелденген",
                "Факт субъективті",
            ],
            "correct_indices": [1],
            "topic": "Сыни ойлау",
        },
        {
            "text": "Мәтіннің мақсатын анықтау үшін не сұрау керек?",
            "options": [
                "Мәтін неше сөзден тұрады?",
                "Автор не айтқысы келеді?",
                "Мәтін қашан жазылды?",
                "Мәтін қай тілде?",
            ],
            "correct_indices": [1],
            "topic": "Мәтінді талдау",
        },
        {
            "text": "Мәтіндегі 'кілт сөздер' не үшін маңызды?",
            "options": [
                "Мәтінді әдемі етеді",
                "Негізгі ойды түсінуге көмектеседі",
                "Сөздер санын көбейтеді",
                "Грамматикаға қажет",
            ],
            "correct_indices": [1],
            "topic": "Мәтінді талдау",
        },
        {
            "text": "Графиктегі деректерді талдау кезінде бірінші не істеу керек?",
            "options": [
                "Түстерге қарау",
                "Осьтердегі белгілерді түсіну",
                "Графиктің өлшемін бағалау",
                "Бірден қорытынды жасау",
            ],
            "correct_indices": [1],
            "topic": "Кестелер мен графиктер",
        },
        {
            "text": "Кестедегі деректерді салыстыру кезінде қандай операция қолданылады?",
            "options": [
                "Тек қосу",
                "Салыстыру, анализ, тренд табу",
                "Тек бөлу",
                "Санамау",
            ],
            "correct_indices": [1],
            "topic": "Кестелер мен графиктер",
        },
    ],
    SubjectId.ALGO: [
        # Programming Basics (C++)
        {
            "text": "Nested loops (қабаттасқан циклдер) дегеніміз не?",
            "options": [
                "Бір цикл",
                "Цикл ішінде тағы бір цикл",
                "Шартты оператор",
                "Функция",
            ],
            "correct_indices": [1],
            "topic": "Программалау негіздері",
        },
        {
            "text": "C++ тіліндегі struct дегеніміз не?",
            "options": [
                "Функция",
                "Цикл түрі",
                "Әртүрлі типтегі деректерді бір объект ретінде сипаттау",
                "Массив",
            ],
            "correct_indices": [2],
            "topic": "Программалау негіздері",
        },
        {
            "text": "C++ тіліндегі int типі нені сақтайды?",
            "options": ["Бүтін сандар", "Ондық сандар", "Символдар", "Мәтіндер"],
            "correct_indices": [0],
            "topic": "Программалау негіздері",
        },
        {
            "text": "C++ тіліндегі double типі нені сақтайды?",
            "options": [
                "Бүтін сандар",
                "Ондық (нақты) сандар",
                "Символдар",
                "Логикалық мәндер",
            ],
            "correct_indices": [1],
            "topic": "Программалау негіздері",
        },
        {
            "text": "for, while, do-while — бұлар қандай құрылымдар?",
            "options": [
                "Шартты операторлар",
                "Циклдік құрылымдар",
                "Функциялар",
                "Массивтер",
            ],
            "correct_indices": [1],
            "topic": "Программалау негіздері",
        },
        {
            "text": "if-else операторы не үшін қолданылады?",
            "options": [
                "Цикл құру",
                "Шарт бойынша таңдау жасау",
                "Функция құру",
                "Массивті сұрыптау",
            ],
            "correct_indices": [1],
            "topic": "Программалау негіздері",
        },
        # Data Structures - Stack
        {
            "text": "Stack деректер құрылымы қандай принциппен жұмыс істейді?",
            "options": ["FIFO", "LIFO", "Random Access", "Sequential"],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "LIFO дегеніміз не?",
            "options": [
                "Бірінші кірген бірінші шығады",
                "Соңғы кірген бірінші шығады",
                "Кездейсоқ қатынас",
                "Сызықтық іздеу",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Stack-ке элемент қосу операциясы қалай аталады?",
            "options": ["Enqueue", "Push", "Insert", "Add"],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Stack-тен элемент алу операциясы қалай аталады?",
            "options": ["Dequeue", "Pop", "Remove", "Delete"],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        # Data Structures - Queue
        {
            "text": "Queue (кезек) деректер құрылымы қандай принциппен жұмыс істейді?",
            "options": ["LIFO", "FIFO", "Random Access", "Binary"],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "FIFO дегеніміз не?",
            "options": [
                "Соңғы кірген бірінші шығады",
                "Бірінші кірген бірінші шығады",
                "Кездейсоқ қатынас",
                "Сызықтық іздеу",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        # Data Structures - Linked Lists
        {
            "text": "Бірбағытты тізімде (Singly Linked List) әр түйін нені ұстайды?",
            "options": [
                "Тек мәліметті",
                "Мәлімет пен келесі түйінге сілтеме",
                "Мәлімет пен алдыңғы түйінге сілтеме",
                "Тек сілтемелер",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Екібағытты тізімде (Doubly Linked List) әр түйін нені ұстайды?",
            "options": [
                "Тек мәліметті",
                "Мәлімет пен келесі түйінге сілтеме",
                "Мәлімет + алдыңғы және келесі түйіндерге сілтемелер",
                "Тек индекс",
            ],
            "correct_indices": [2],
            "topic": "Деректер құрылымы",
        },
        # Data Structures - Trees
        {
            "text": "BST (Binary Search Tree) дегеніміз не?",
            "options": [
                "Сол жақта кіші, оң жақта үлкен элемент сақталатын ағаш",
                "Сол жақта үлкен, оң жақта кіші элемент",
                "Кездейсоқ орналасқан ағаш",
                "Толық толтырылған ағаш",
            ],
            "correct_indices": [0],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Бинарлық ағаштың биіктігі (height) дегеніміз не?",
            "options": [
                "Түйіндер саны",
                "Жапырақтар саны",
                "Тамырдан ең терең жапыраққа дейінгі қашықтық",
                "Қабырғалар саны",
            ],
            "correct_indices": [2],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "BST-де 50 санын іздеу қай бағытта жасалады, егер түбір = 30 болса?",
            "options": [
                "Сол жаққа",
                "Оң жаққа",
                "Кез келген жаққа",
                "Іздеу мүмкін емес",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        # Graph Algorithms - Shortest Path
        {
            "text": "Dijkstra алгоритмі не үшін қолданылады?",
            "options": [
                "Ең қысқа жолды табу",
                "Минималды қаңқа ағашы",
                "Сұрыптау",
                "Графты бояу",
            ],
            "correct_indices": [0],
            "topic": "Графтар",
        },
        {
            "text": "Dijkstra алгоритмі қандай графтарда жұмыс істейді?",
            "options": [
                "Теріс салмақты қабырғалар болмауы керек",
                "Тек бағытталған графтар",
                "Тек ағаштар",
                "Барлық графтар",
            ],
            "correct_indices": [0],
            "topic": "Графтар",
        },
        {
            "text": "Беллман-Форд алгоритмі Dijkstra-дан қандай жағдайда артық?",
            "options": [
                "Жылдамырақ",
                "Теріс салмақты қабырғаларды өңдей алады",
                "Аз жады қолданады",
                "Тек ағаштарда жұмыс істейді",
            ],
            "correct_indices": [1],
            "topic": "Графтар",
        },
        {
            "text": "Флойд-Уоршелл алгоритмі не табады?",
            "options": [
                "Бір төбеден ең қысқа жол",
                "Барлық төбе жұптары арасындағы ең қысқа жолдар",
                "Минималды қаңқа ағаш",
                "Графтың циклін",
            ],
            "correct_indices": [1],
            "topic": "Графтар",
        },
        # Graph Algorithms - MST
        {
            "text": "Minimum Spanning Tree (Тірек ағаш) дегеніміз не?",
            "options": [
                "Графтағы ең қысқа жол",
                "Графтың барлық төбелерін ең аз салмақпен байланыстыратын ағаш",
                "Ең терең ағаш",
                "Ең көп түйіні бар ағаш",
            ],
            "correct_indices": [1],
            "topic": "Графтар",
        },
        {
            "text": "Прим алгоритмі не құрады?",
            "options": [
                "Ең қысқа жол",
                "Минималды қаңқа ағаш (MST)",
                "Топологиялық сұрыптау",
                "BFS",
            ],
            "correct_indices": [1],
            "topic": "Графтар",
        },
        {
            "text": "Крускал алгоритмі қалай жұмыс істейді?",
            "options": [
                "Қабырғаларды салмағы бойынша сұрыптап, MST құрады",
                "Тереңдік бойынша іздейді",
                "Ендік бойынша іздейді",
                "Кездейсоқ қабырғаларды таңдайды",
            ],
            "correct_indices": [0],
            "topic": "Графтар",
        },
        # Big O Notation
        {
            "text": "O(1) күрделілігі нені білдіреді?",
            "options": [
                "Сызықтық уақыт",
                "Тұрақты уақыт",
                "Квадраттық уақыт",
                "Логарифмдік уақыт",
            ],
            "correct_indices": [1],
            "topic": "Big O",
        },
        {
            "text": "O(n) күрделілігі нені білдіреді?",
            "options": [
                "Тұрақты уақыт",
                "Сызықтық уақыт",
                "Квадраттық уақыт",
                "Логарифмдік уақыт",
            ],
            "correct_indices": [1],
            "topic": "Big O",
        },
        {
            "text": "O(log n) күрделілігі нені білдіреді?",
            "options": [
                "Сызықтық уақыт",
                "Квадраттық уақыт",
                "Логарифмдік уақыт",
                "Тұрақты уақыт",
            ],
            "correct_indices": [2],
            "topic": "Big O",
        },
        {
            "text": "O(n²) күрделілігі қандай алгоритмге тән?",
            "options": [
                "Binary Search",
                "Quick Sort (орташа)",
                "Bubble Sort",
                "Merge Sort",
            ],
            "correct_indices": [2],
            "topic": "Big O",
        },
        {
            "text": "O(n log n) күрделілігі қандай алгоритмге тән?",
            "options": ["Bubble Sort", "Selection Sort", "Merge Sort", "Linear Search"],
            "correct_indices": [2],
            "topic": "Big O",
        },
        {
            "text": "Binary Search алгоритмінің күрделілігі қандай?",
            "options": ["O(n)", "O(n²)", "O(log n)", "O(1)"],
            "correct_indices": [2],
            "topic": "Big O",
        },
        {
            "text": "Егер алгоритмде екі қабаттасқан цикл болса, күрделілігі қандай болады?",
            "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"],
            "correct_indices": [2],
            "topic": "Big O",
        },
        {
            "text": "Қай жылдамдық ең тиімді?",
            "options": ["O(n²)", "O(n)", "O(log n)", "O(n log n)"],
            "correct_indices": [2],
            "topic": "Big O",
        },
        # === ADDITIONAL ПРОГРАММАЛАУ НЕГІЗДЕРІ (15 more) ===
        {
            "text": "C++ тілінде 'char' типі нені сақтайды?",
            "options": ["Бүтін санды", "Символды", "Жолды", "Логикалық мәнді"],
            "correct_indices": [1],
            "topic": "Программалау негіздері",
        },
        {
            "text": "C++ тіліндегі 'bool' типі қандай мәндерді қабылдайды?",
            "options": ["0-255", "true/false", "Кез келген сан", "Символдар"],
            "correct_indices": [1],
            "topic": "Программалау негіздері",
        },
        {
            "text": "switch-case операторы не үшін қолданылады?",
            "options": [
                "Цикл құру",
                "Бірнеше мән бойынша таңдау",
                "Функция анықтау",
                "Массив құру",
            ],
            "correct_indices": [1],
            "topic": "Программалау негіздері",
        },
        {
            "text": "for циклінің құрылымы қандай?",
            "options": [
                "for(шарт)",
                "for(инициализация; шарт; өзгерту)",
                "for(әрекет)",
                "for(санау)",
            ],
            "correct_indices": [1],
            "topic": "Программалау негіздері",
        },
        {
            "text": "while циклі қашан тоқтайды?",
            "options": [
                "Әрқашан",
                "Шарт false болғанда",
                "Шарт true болғанда",
                "5 қайталаудан кейін",
            ],
            "correct_indices": [1],
            "topic": "Программалау негіздері",
        },
        {
            "text": "do-while циклі while-дан немен айырмашылығы?",
            "options": [
                "Жылдамырақ",
                "Кем дегенде 1 рет орындалады",
                "Ешқашан орындалмайды",
                "Айырмашылық жоқ",
            ],
            "correct_indices": [1],
            "topic": "Программалау негіздері",
        },
        {
            "text": "Массив дегеніміз не?",
            "options": [
                "Бір айнымалы",
                "Бір типті элементтер жиыны",
                "Функция",
                "Цикл түрі",
            ],
            "correct_indices": [1],
            "topic": "Программалау негіздері",
        },
        {
            "text": "Массивтің индексі қай саннан басталады (C++)?",
            "options": ["1", "0", "-1", "10"],
            "correct_indices": [1],
            "topic": "Программалау негіздері",
        },
        {
            "text": "Екі өлшемді массив дегеніміз не?",
            "options": ["Бір жолдық массив", "Кесте тәрізді массив", "Функция", "Цикл"],
            "correct_indices": [1],
            "topic": "Программалау негіздері",
        },
        {
            "text": "Функция не үшін қолданылады?",
            "options": [
                "Деректерді сақтау",
                "Кодты қайта пайдалануға болатын блоктарға бөлу",
                "Циклді құру",
                "Айнымалы жариялау",
            ],
            "correct_indices": [1],
            "topic": "Программалау негіздері",
        },
        {
            "text": "C++ тіліндегі 'return' кілт сөзі не істейді?",
            "options": [
                "Цикл тоқтатады",
                "Функциядан мән қайтарады",
                "Айнымалы жариялайды",
                "Шарт тексереді",
            ],
            "correct_indices": [1],
            "topic": "Программалау негіздері",
        },
        {
            "text": "'void' функциясы не дегенді білдіреді?",
            "options": [
                "Мән қайтарады",
                "Мән қайтармайды",
                "Бүтін сан қайтарады",
                "Жол қайтарады",
            ],
            "correct_indices": [1],
            "topic": "Программалау негіздері",
        },
        {
            "text": "Берілген код нәтижесі неге тең? int x = 5; x++; cout << x;",
            "options": ["4", "5", "6", "Қате"],
            "correct_indices": [2],
            "topic": "Программалау негіздері",
        },
        {
            "text": "Берілген код нәтижесі неге тең? int a = 10, b = 3; cout << a % b;",
            "options": ["0", "1", "3", "10"],
            "correct_indices": [1],
            "topic": "Программалау негіздері",
        },
        {
            "text": "C++ тіліндегі '==' операторы не істейді?",
            "options": ["Мән меншіктейді", "Теңдікті салыстырады", "Қосады", "Алады"],
            "correct_indices": [1],
            "topic": "Программалау негіздері",
        },
        # === ADDITIONAL ДЕРЕКТЕР ҚҰРЫЛЫМЫ - STACK/QUEUE (10 more) ===
        {
            "text": "Stack қай жағдайда қолданылады?",
            "options": [
                "Файлдарды сақтау",
                "Функция шақыруларын бақылау (call stack)",
                "Деректер базасы",
                "Графиктер",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Queue қай жағдайда қолданылады?",
            "options": [
                "Функция шақырулары",
                "Кезекте тұру (принтер тапсырмалары, т.б.)",
                "Рекурсия",
                "Бинарлық іздеу",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Queue-ге элемент қосу операциясы қалай аталады?",
            "options": ["Push", "Pop", "Enqueue", "Dequeue"],
            "correct_indices": [2],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Queue-ден элемент алу операциясы қалай аталады?",
            "options": ["Push", "Pop", "Enqueue", "Dequeue"],
            "correct_indices": [3],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Priority Queue дегеніміз не?",
            "options": [
                "Қарапайым кезек",
                "Приоритеті бойынша сұрыпталған кезек",
                "Stack түрі",
                "Массив",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Circular Queue дегеніміз не?",
            "options": [
                "Сызықтық кезек",
                "Соңы мен басы байланысқан циклдық кезек",
                "Стек",
                "Ағаш",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Stack толық болса (overflow) не болады?",
            "options": [
                "Жаңа элемент қосылады",
                "Қате шығады",
                "Ескі элемент жойылады",
                "Ештеңе болмайды",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Stack бос болса (underflow) ne болады?",
            "options": [
                "Элемент шығады",
                "Қате шығады",
                "Жаңа элемент қосылады",
                "Stack өседі",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Deque дегеніміз не?",
            "options": [
                "Бір жақты кезек",
                "Екі жақтан қолдану мүмкін кезек",
                "Стек түрі",
                "Ағаш түрі",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Stack және Queue-дің ортақ қасиеті не?",
            "options": [
                "Екеуі де LIFO",
                "Екеуі де сызықтық құрылым",
                "Екеуі де ағаш",
                "Екеуі де граф",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        # === ADDITIONAL ТІЗІМДЕР (LINKED LISTS) (10 more) ===
        {
            "text": "Linked List-тің массивтен артықшылығы не?",
            "options": [
                "Жылдам қатынас",
                "Динамикалық өлшем және тиімді қосу/жою",
                "Аз жады қолдану",
                "Сұрыптау қажет емес",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Linked List-тің кемшілігі не?",
            "options": [
                "Динамикалық өлшем",
                "Индекс арқылы жылдам қатынас жоқ",
                "Қосу оңай",
                "Жою оңай",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Linked List-тің басына элемент қосу күрделілігі қандай?",
            "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"],
            "correct_indices": [2],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Linked List-тің ортасынан элемент іздеу күрделілігі қандай?",
            "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
            "correct_indices": [2],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Circular Linked List дегеніміз не?",
            "options": [
                "Соңғы түйін NULL-ға сілтейді",
                "Соңғы түйін бірінші түйінге сілтейді",
                "Екі бағытты тізім",
                "Бос тізім",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Linked List-те Head дегеніміз не?",
            "options": [
                "Соңғы түйін",
                "Бірінші түйін",
                "Ортаңғы түйін",
                "Бос түйін",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Linked List-те Tail дегеніміз не?",
            "options": [
                "Бірінші түйін",
                "Соңғы түйін",
                "Ортаңғы түйін",
                "Head пен бірдей",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Linked List-те NULL не білдіреді?",
            "options": [
                "Келесі элемент бар",
                "Тізімнің соңы",
                "Қате",
                "Бос мән",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Doubly Linked List-те траверс қалай жүзеге асады?",
            "options": [
                "Тек алға",
                "Тек артқа",
                "Алға және артқа",
                "Кездейсоқ",
            ],
            "correct_indices": [2],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Linked List vs Array: қайсысында индекс арқылы қатынас жылдамырақ?",
            "options": ["Linked List", "Array", "Бірдей", "Салыстыруға болмайды"],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        # === ADDITIONAL АҒАШТАР (TREES) (15 more) ===
        {
            "text": "Бинарлық ағаштағы әр түйіннің максимум неше балалығы болады?",
            "options": ["1", "2", "3", "Шексіз"],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "BST-де 20 санын қосу: түбір=30, сол бала=15. 20 қайда орналасады?",
            "options": [
                "30-дың оң балаларына",
                "15-тің оң балаларына",
                "Түбірге",
                "15-тің сол балаларына",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Ағаштың 'жапырақ' (leaf) түйіні дегеніміз не?",
            "options": [
                "Түбір",
                "Балалары жоқ түйін",
                "Ең терең түйін",
                "Ортаңғы түйін",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "In-order traversal қандай ретте элементтерді қайтарады (BST)?",
            "options": [
                "Кездейсоқ",
                "Кіші -> үлкен (сұрыпталған)",
                "Үлкен -> кіші",
                "Түбірден бастап",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Pre-order traversal қандай ретпен жүреді?",
            "options": [
                "Сол -> Түбір -> Оң",
                "Түбір -> Сол -> Оң",
                "Сол -> Оң -> Түбір",
                "Оң -> Сол -> Түбір",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Post-order traversal қандай ретпен жүреді?",
            "options": [
                "Сол -> Түбір -> Оң",
                "Түбір -> Сол -> Оң",
                "Сол -> Оң -> Түбір",
                "Оң -> Түбір -> Сол",
            ],
            "correct_indices": [2],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "BST-де іздеу операциясының орташа күрделілігі қандай?",
            "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Толық бинарлық ағаш (Complete Binary Tree) дегеніміз не?",
            "options": [
                "Барлық деңгейлер толық, соңғы деңгейде солдан толтырылған",
                "Тек сол балалары бар",
                "Барлық жапырақтар бірдей деңгейде",
                "Кездейсоқ толтырылған",
            ],
            "correct_indices": [0],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Heap деректер құрылымы қандай ағаш түрі?",
            "options": ["BST", "Complete Binary Tree", "AVL Tree", "Red-Black Tree"],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Max-Heap-те түбір элементі қандай?",
            "options": ["Ең кіші", "Ең үлкен", "Орташа", "Кездейсоқ"],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Min-Heap-те түбір элементі қандай?",
            "options": ["Ең үлкен", "Ең кіші", "Орташа", "Кездейсоқ"],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "AVL ағашы дегеніміз не?",
            "options": [
                "Теңдестірілмеген BST",
                "Өзін-өзі теңдестіретін BST",
                "Қарапайым ағаш",
                "Толық ағаш",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Ағаштың деңгейі (level) қалай есептеледі?",
            "options": [
                "Түбірден бастап, 0-ден",
                "Жапырақтардан бастап",
                "Биіктікпен бірдей",
                "Түйіндер санымен",
            ],
            "correct_indices": [0],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "n түйінді толық бинарлық ағаштың биіктігі қандай?",
            "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        {
            "text": "Trie (Prefix Tree) не үшін қолданылады?",
            "options": [
                "Сандарды сұрыптау",
                "Сөздерді сақтау және іздеу",
                "Графтарды сақтау",
                "Стек операциялары",
            ],
            "correct_indices": [1],
            "topic": "Деректер құрылымы",
        },
        # === ADDITIONAL ГРАФТАР АЛГОРИТМДЕРІ (15 more) ===
        {
            "text": "BFS (Breadth-First Search) дегеніміз не?",
            "options": [
                "Тереңдік бойынша іздеу",
                "Ендік (деңгей) бойынша іздеу",
                "Екілік іздеу",
                "Сызықтық іздеу",
            ],
            "correct_indices": [1],
            "topic": "Графтар",
        },
        {
            "text": "DFS (Depth-First Search) дегеніміз не?",
            "options": [
                "Ендік бойынша іздеу",
                "Тереңдік бойынша іздеу",
                "Екілік іздеу",
                "Сызықтық іздеу",
            ],
            "correct_indices": [1],
            "topic": "Графтар",
        },
        {
            "text": "BFS қандай деректер құрылымын қолданады?",
            "options": ["Stack", "Queue", "Heap", "Tree"],
            "correct_indices": [1],
            "topic": "Графтар",
        },
        {
            "text": "DFS қандай деректер құрылымын қолданады?",
            "options": ["Queue", "Stack (немесе рекурсия)", "Heap", "Array"],
            "correct_indices": [1],
            "topic": "Графтар",
        },
        {
            "text": "Бағытталған граф (Directed Graph) дегеніміз не?",
            "options": [
                "Қабырғалардың бағыты жоқ",
                "Қабырғалардың бағыты бар",
                "Циклі жоқ граф",
                "Толық граф",
            ],
            "correct_indices": [1],
            "topic": "Графтар",
        },
        {
            "text": "Бағытталмаған граф (Undirected Graph) дегеніміз не?",
            "options": [
                "Қабырғалардың бағыты бар",
                "Қабырғалар екі жақтан байланысқан",
                "Циклі бар граф",
                "Ағаш",
            ],
            "correct_indices": [1],
            "topic": "Графтар",
        },
        {
            "text": "Графтың циклі (cycle) дегеніміз не?",
            "options": [
                "Бастапқы төбе жоқ",
                "Бір төбеден бастап, сол төбеге оралатын жол",
                "Ең қысқа жол",
                "MST",
            ],
            "correct_indices": [1],
            "topic": "Графтар",
        },
        {
            "text": "DAG дегеніміз не?",
            "options": [
                "Циклі бар бағытталған граф",
                "Циклсіз бағытталған граф",
                "Бағытталмаған граф",
                "Толық граф",
            ],
            "correct_indices": [1],
            "topic": "Графтар",
        },
        {
            "text": "Топологиялық сұрыптау қандай графтарда мүмкін?",
            "options": [
                "Циклі бар графтар",
                "DAG (циклсіз бағытталған граф)",
                "Бағытталмаған графтар",
                "Барлық графтар",
            ],
            "correct_indices": [1],
            "topic": "Графтар",
        },
        {
            "text": "Прим және Крускал алгоритмдерінің ортақ мақсаты не?",
            "options": [
                "Ең қысқа жол табу",
                "MST (минималды қаңқа ағаш) құру",
                "Топологиялық сұрыптау",
                "Циклды анықтау",
            ],
            "correct_indices": [1],
            "topic": "Графтар",
        },
        {
            "text": "Графты adjacency matrix арқылы сақтау қандай жады қолданады?",
            "options": ["O(V)", "O(E)", "O(V²)", "O(V+E)"],
            "correct_indices": [2],
            "topic": "Графтар",
        },
        {
            "text": "Графты adjacency list арқылы сақтау қандай жады қолданады?",
            "options": ["O(V²)", "O(V + E)", "O(E²)", "O(1)"],
            "correct_indices": [1],
            "topic": "Графтар",
        },
        {
            "text": "Dijkstra алгоритмінің уақыт күрделілігі қандай (priority queue)?",
            "options": ["O(V)", "O(V²)", "O((V+E) log V)", "O(E)"],
            "correct_indices": [2],
            "topic": "Графтар",
        },
        {
            "text": "BFS/DFS уақыт күрделілігі қандай?",
            "options": ["O(V)", "O(E)", "O(V + E)", "O(V²)"],
            "correct_indices": [2],
            "topic": "Графтар",
        },
        {
            "text": "Графтағы қосылған компоненттер (connected components) не?",
            "options": [
                "Бір төбе",
                "Бір-бірімен байланысқан төбелер топтары",
                "Циклдер",
                "Қабырғалар",
            ],
            "correct_indices": [1],
            "topic": "Графтар",
        },
        # === ADDITIONAL BIG O NOTATION (15 more) ===
        {
            "text": "O(2^n) күрделілігі қандай алгоритмге тән?",
            "options": [
                "Сызықтық іздеу",
                "Фибоначчи рекурсиясы",
                "Bubble Sort",
                "Binary Search",
            ],
            "correct_indices": [1],
            "topic": "Big O",
        },
        {
            "text": "O(n!) күрделілігі қандай есептерде кездеседі?",
            "options": ["Сұрыптау", "Іздеу", "Permutation (орынауыстыру)", "Қосу"],
            "correct_indices": [2],
            "topic": "Big O",
        },
        {
            "text": "Space Complexity дегеніміз не?",
            "options": [
                "Алгоритм жылдамдығы",
                "Алгоритм қолданатын жады",
                "Код ұзындығы",
                "Циклдер саны",
            ],
            "correct_indices": [1],
            "topic": "Big O",
        },
        {
            "text": "Time Complexity дегеніміз не?",
            "options": [
                "Алгоритм қолданатын жады",
                "Алгоритмнің орындалу уақыты",
                "Код жолдар саны",
                "Айнымалылар саны",
            ],
            "correct_indices": [1],
            "topic": "Big O",
        },
        {
            "text": "Best Case, Average Case, Worst Case дегеніміз не?",
            "options": [
                "Код түрлері",
                "Алгоритмнің әртүрлі жағдайлардағы күрделілігі",
                "Деректер типтері",
                "Циклдер түрлері",
            ],
            "correct_indices": [1],
            "topic": "Big O",
        },
        {
            "text": "Quick Sort-тың орташа күрделілігі қандай?",
            "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"],
            "correct_indices": [1],
            "topic": "Big O",
        },
        {
            "text": "Quick Sort-тың ең нашар күрделілігі қандай?",
            "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"],
            "correct_indices": [2],
            "topic": "Big O",
        },
        {
            "text": "Insertion Sort-тың ең жақсы күрделілігі қандай?",
            "options": ["O(n²)", "O(n log n)", "O(n)", "O(1)"],
            "correct_indices": [2],
            "topic": "Big O",
        },
        {
            "text": "Hash Table-дегі іздеу операциясының орташа күрделілігі?",
            "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"],
            "correct_indices": [2],
            "topic": "Big O",
        },
        {
            "text": "Heap Sort күрделілігі қандай?",
            "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"],
            "correct_indices": [1],
            "topic": "Big O",
        },
        {
            "text": "Сызықтық іздеу (Linear Search) күрделілігі?",
            "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
            "correct_indices": [2],
            "topic": "Big O",
        },
        {
            "text": "Массивке элемент қосу (соңына) күрделілігі?",
            "options": ["O(1) амортизацияланған", "O(n)", "O(log n)", "O(n²)"],
            "correct_indices": [0],
            "topic": "Big O",
        },
        {
            "text": "O(n³) күрделілігі қандай алгоритмде кездеседі?",
            "options": [
                "Binary Search",
                "3 қабаттасқан цикл",
                "Merge Sort",
                "Queue операциялары",
            ],
            "correct_indices": [1],
            "topic": "Big O",
        },
        {
            "text": "Амортизацияланған талдау (amortized analysis) нені көрсетеді?",
            "options": [
                "Ең нашар жағдай",
                "Көптеген операциялардың орташа құнын",
                "Ең жақсы жағдай",
                "Жады қолдануы",
            ],
            "correct_indices": [1],
            "topic": "Big O",
        },
        {
            "text": "Рекурсивті алгоритмдер көбінесе қандай қосымша жады қолданады?",
            "options": ["Heap", "Call Stack", "Queue", "Array"],
            "correct_indices": [1],
            "topic": "Big O",
        },
        # === ADDITIONAL СҰРЫПТАУ АЛГОРИТМДЕРІ (10 more) ===
        {
            "text": "Bubble Sort қалай жұмыс істейді?",
            "options": [
                "Элементтерді қосады",
                "Көрші элементтерді салыстырып, орнын ауыстырады",
                "Бөліп алгоритмін қолданады",
                "Кездейсоқ сұрыптайды",
            ],
            "correct_indices": [1],
            "topic": "Сұрыптау",
        },
        {
            "text": "Selection Sort қалай жұмыс істейді?",
            "options": [
                "Ең кіші элементті тауып, алдыға қояды",
                "Көрші элементтерді салыстырады",
                "Рекурсияны қолданады",
                "Бөліп алу принципі",
            ],
            "correct_indices": [0],
            "topic": "Сұрыптау",
        },
        {
            "text": "Merge Sort қандай стратегияны қолданады?",
            "options": [
                "Greedy",
                "Divide and Conquer",
                "Dynamic Programming",
                "Backtracking",
            ],
            "correct_indices": [1],
            "topic": "Сұрыптау",
        },
        {
            "text": "Merge Sort тұрақты (stable) сұрыптау ма?",
            "options": ["Иә", "Жоқ", "Кейде", "Белгісіз"],
            "correct_indices": [0],
            "topic": "Сұрыптау",
        },
        {
            "text": "Quick Sort қандай стратегияны қолданады?",
            "options": [
                "Greedy",
                "Divide and Conquer",
                "Dynamic Programming",
                "Brute Force",
            ],
            "correct_indices": [1],
            "topic": "Сұрыптау",
        },
        {
            "text": "Quick Sort-та pivot дегеніміз не?",
            "options": [
                "Бірінші элемент",
                "Сұрыптау үшін таңдалған салыстыру элементі",
                "Соңғы элемент",
                "Ортаңғы мән",
            ],
            "correct_indices": [1],
            "topic": "Сұрыптау",
        },
        {
            "text": "Counting Sort қандай деректерде тиімді?",
            "options": [
                "Кез келген деректер",
                "Шектеулі диапазондағы бүтін сандар",
                "Жолдар",
                "Нақты сандар",
            ],
            "correct_indices": [1],
            "topic": "Сұрыптау",
        },
        {
            "text": "Radix Sort қандай принципті қолданады?",
            "options": [
                "Салыстыру",
                "Разрядтар бойынша сұрыптау",
                "Бөліп алу",
                "Рекурсия",
            ],
            "correct_indices": [1],
            "topic": "Сұрыптау",
        },
        {
            "text": "In-place сұрыптау дегеніміз не?",
            "options": [
                "Қосымша жадыны көп қолданатын",
                "O(1) қосымша жадымен сұрыптау",
                "Сырттан сұрыптау",
                "Параллель сұрыптау",
            ],
            "correct_indices": [1],
            "topic": "Сұрыптау",
        },
        {
            "text": "Қай сұрыптау алгоритмі O(n) күрделілікке ие бола алады?",
            "options": [
                "Quick Sort",
                "Merge Sort",
                "Counting Sort (арнайы шарттарда)",
                "Bubble Sort",
            ],
            "correct_indices": [2],
            "topic": "Сұрыптау",
        },
    ],
    SubjectId.DB: [
        # ER-Modeling Section
        {
            "text": "ER-диаграммасындағы 'E' әрпі нені білдіреді?",
            "options": ["Error", "Entity", "Element", "Edge"],
            "correct_indices": [1],
            "topic": "ER-модельдеу",
        },
        {
            "text": "ER-диаграммасындағы 'R' әрпі нені білдіреді?",
            "options": ["Record", "Row", "Relationship", "Reference"],
            "correct_indices": [2],
            "topic": "ER-модельдеу",
        },
        {
            "text": "Бір мұғалім — көп студент байланысы қандай түрге жатады?",
            "options": ["1:1", "1:M", "M:N", "M:1"],
            "correct_indices": [1],
            "topic": "ER-модельдеу",
        },
        {
            "text": "Көп студент — көп пән байланысы қандай түрге жатады?",
            "options": ["1:1", "1:M", "M:N", "N:1"],
            "correct_indices": [2],
            "topic": "ER-модельдеу",
        },
        {
            "text": "Бір адам — бір паспорт байланысы қандай түрге жатады?",
            "options": ["1:1", "1:M", "M:N", "M:1"],
            "correct_indices": [0],
            "topic": "ER-модельдеу",
        },
        {
            "text": "Кілттік атрибуттың қызметі не?",
            "options": [
                "Деректерді сұрыптау",
                "Объектіні бірегей анықтау",
                "Байланыс орнату",
                "Типті анықтау",
            ],
            "correct_indices": [1],
            "topic": "ER-модельдеу",
        },
        # Normalization Section
        {
            "text": "Нормализация дегеніміз не?",
            "options": [
                "Деректерді шифрлау",
                "Артық деректерді азайту процесі",
                "Деректерді сақтау",
                "Деректерді жою",
            ],
            "correct_indices": [1],
            "topic": "Нормализация",
        },
        {
            "text": "1NF қандай шартты талап етеді?",
            "options": [
                "Барлық атрибуттар атомарлы болуы керек",
                "Foreign Key болуы керек",
                "Индекстер болуы керек",
                "Транзакциялар болуы керек",
            ],
            "correct_indices": [0],
            "topic": "Нормализация",
        },
        {
            "text": "Денормализация не үшін қолданылады?",
            "options": [
                "Қауіпсіздікті арттыру",
                "Өнімділікті арттыру үшін",
                "Деректерді жою",
                "Кестелерді бөлу",
            ],
            "correct_indices": [1],
            "topic": "Нормализация",
        },
        {
            "text": "X → Y жазуы нені білдіреді?",
            "options": [
                "X Y-ға тең емес",
                "Y мәні X-ке функционалды тәуелді",
                "X пен Y тәуелсіз",
                "X бойынша сұрыптау",
            ],
            "correct_indices": [1],
            "topic": "Нормализация",
        },
        # Keys Section
        {
            "text": "Primary Key қандай қызмет атқарады?",
            "options": [
                "Деректерді шифрлау",
                "Кестедегі жазбаны бірегей анықтау",
                "Сұраныс жылдамдығын арттыру",
                "Деректерді жою",
            ],
            "correct_indices": [1],
            "topic": "Кілттер",
        },
        {
            "text": "Foreign Key қандай қызмет атқарады?",
            "options": [
                "Кестедегі жазбаны анықтау",
                "Басқа кестемен байланыс орнату",
                "Деректерді шифрлау",
                "Индекс құру",
            ],
            "correct_indices": [1],
            "topic": "Кілттер",
        },
        # SQL Section
        {
            "text": "SQL-де деректерді топтастыру үшін қандай оператор қолданылады?",
            "options": ["ORDER BY", "SORT BY", "GROUP BY", "AGGREGATE BY"],
            "correct_indices": [2],
            "topic": "SQL",
        },
        {
            "text": "SQL-де деректерді кему ретімен сұрыптау қандай кілтсөзбен жасалады?",
            "options": ["ASC", "DESC", "DOWN", "REVERSE"],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "SELECT ID FROM Students ORDER BY GPA DESC LIMIT 3; — бұл сұраныс не қайтарады?",
            "options": [
                "Барлық студенттер",
                "GPA бойынша ең төменгі 3 студент",
                "GPA бойынша ең жоғары 3 студент",
                "Студенттер саны",
            ],
            "correct_indices": [2],
            "topic": "SQL",
        },
        {
            "text": "COUNT() функциясы не істейді?",
            "options": [
                "Қосынды есептейді",
                "Орташа мәнді табады",
                "Жазбалар санын есептейді",
                "Максимумды табады",
            ],
            "correct_indices": [2],
            "topic": "SQL",
        },
        {
            "text": "AVG() функциясы не істейді?",
            "options": [
                "Жазбалар санын есептейді",
                "Орташа мәнді табады",
                "Максимумды табады",
                "Қосындыны табады",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "UNION операторының қызметі не?",
            "options": [
                "Кестелерді біріктіру",
                "Нәтижелерді біріктіру",
                "Деректерді жою",
                "Индекс құру",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "INTERSECT операторы не қайтарады?",
            "options": [
                "Барлық нәтижелер",
                "Ортақ бөлікті",
                "Айырмашылықты",
                "Бірінші кестені",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "INNER JOIN қандай жазбаларды қайтарады?",
            "options": [
                "Барлық жазбалар",
                "Тек сәйкес келетін жазбалар",
                "Тек сол жақ кестенің жазбалары",
                "Тек оң жақ кестенің жазбалары",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "LEFT JOIN қандай жазбаларды қайтарады?",
            "options": [
                "Тек сәйкес келетін жазбалар",
                "Сол жақ кестенің барлық жазбалары + сәйкестіктер",
                "Тек оң жақ кестенің жазбалары",
                "Барлық жазбалар",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        # DBMS Architecture Section
        {
            "text": "Клиент-сервер архитектурасы неше деңгейлі?",
            "options": ["1 деңгейлі", "2 деңгейлі", "3 деңгейлі", "4 деңгейлі"],
            "correct_indices": [1],
            "topic": "Архитектура",
        },
        {
            "text": "3 деңгейлі архитектурада қандай қабаттар бар? (Бірнеше жауап)",
            "options": ["UI", "Логика", "Дерекқор", "Желі", "Аппаратура"],
            "correct_indices": [0, 1, 2],
            "topic": "Архитектура",
        },
        # Integrity Section
        {
            "text": "Домендік тұтастық нені қамтамасыз етеді?",
            "options": [
                "Типі мен диапазонның дұрыстығын",
                "Байланыстардың дұрыстығын",
                "Транзакциялардың дұрыстығын",
                "Индекстердің дұрыстығын",
            ],
            "correct_indices": [0],
            "topic": "Тұтастық",
        },
        {
            "text": "Сілтемелік тұтастық нені қамтамасыз етеді?",
            "options": [
                "Типтердің дұрыстығын",
                "Foreign Key байланысының дұрыстығын",
                "Индекстердің дұрыстығын",
                "Шифрлаудың дұрыстығын",
            ],
            "correct_indices": [1],
            "topic": "Тұтастық",
        },
        # ACID Section
        {
            "text": "ACID қасиеттеріне не жатады? (Бірнеше жауап)",
            "options": [
                "Atomicity",
                "Consistency",
                "Isolation",
                "Durability",
                "Accuracy",
            ],
            "correct_indices": [0, 1, 2, 3],
            "topic": "Транзакциялар",
        },
        {
            "text": "Atomicity дегеніміз не?",
            "options": [
                "Деректердің дұрыстығы",
                "Транзакция толық орындалады немесе орындалмайды",
                "Транзакциялар бір-біріне әсер етпейді",
                "Нәтиже сақталады",
            ],
            "correct_indices": [1],
            "topic": "Транзакциялар",
        },
        {
            "text": "Isolation дегеніміз не?",
            "options": [
                "Толық орындалу",
                "Дерекқордың дұрыс күйде қалуы",
                "Транзакциялар бір-біріне әсер етпеуі",
                "Нәтиженің сақталуы",
            ],
            "correct_indices": [2],
            "topic": "Транзакциялар",
        },
        {
            "text": "Durability дегеніміз не?",
            "options": [
                "Толық орындалу",
                "Дерекқордың дұрыстығы",
                "Транзакциялардың оқшаулануы",
                "Нәтиженің сақталып қалуы",
            ],
            "correct_indices": [3],
            "topic": "Транзакциялар",
        },
        # Relational Model
        {
            "text": "Реляциялық деректер моделінде кесте қалай аталады?",
            "options": ["Object", "Relation", "Entity", "Set"],
            "correct_indices": [1],
            "topic": "Реляциялық модель",
        },
        {
            "text": "Реляциялық моделдегі жол (row) қалай аталады?",
            "options": ["Tuple (кортеж)", "Attribute", "Domain", "Relation"],
            "correct_indices": [0],
            "topic": "Реляциялық модель",
        },
        {
            "text": "Реляциялық моделдегі баған (column) қалай аталады?",
            "options": ["Tuple", "Attribute (атрибут)", "Domain", "Relation"],
            "correct_indices": [1],
            "topic": "Реляциялық модель",
        },
        # === ADDITIONAL ER-МОДЕЛЬДЕУ (15 more) ===
        {
            "text": "ER-диаграммада субъект (entity) қандай фигурамен белгіленеді?",
            "options": ["Шеңбер", "Төртбұрыш", "Ромб", "Үшбұрыш"],
            "correct_indices": [1],
            "topic": "ER-модельдеу",
        },
        {
            "text": "ER-диаграммада байланыс (relationship) қандай фигурамен белгіленеді?",
            "options": ["Төртбұрыш", "Шеңбер", "Ромб", "Эллипс"],
            "correct_indices": [2],
            "topic": "ER-модельдеу",
        },
        {
            "text": "ER-диаграммада атрибут қандай фигурамен белгіленеді?",
            "options": ["Төртбұрыш", "Ромб", "Эллипс (овал)", "Үшбұрыш"],
            "correct_indices": [2],
            "topic": "ER-модельдеу",
        },
        {
            "text": "Жай атрибут дегеніміз не?",
            "options": [
                "Бірнеше бөлікке бөлінетін",
                "Бөлінбейтін, атомарлы мән",
                "Бірнеше мәні бар",
                "Туынды атрибут",
            ],
            "correct_indices": [1],
            "topic": "ER-модельдеу",
        },
        {
            "text": "Күрделі (composite) атрибут дегеніміз не?",
            "options": [
                "Бөлінбейтін мән",
                "Бірнеше бөлікке бөлінетін атрибут",
                "Бірнеше мәні бар атрибут",
                "Есептелетін атрибут",
            ],
            "correct_indices": [1],
            "topic": "ER-модельдеу",
        },
        {
            "text": "Көп мәнді (multivalued) атрибутқа мысал келтіріңіз:",
            "options": [
                "Туған күні",
                "Телефон нөмірлері (бірнеше болуы мүмкін)",
                "Жынысы",
                "ИИН",
            ],
            "correct_indices": [1],
            "topic": "ER-модельдеу",
        },
        {
            "text": "Туынды (derived) атрибут дегеніміз не?",
            "options": [
                "Тікелей сақталатын мән",
                "Басқа атрибуттардан есептелетін мән",
                "Кілттік атрибут",
                "Көп мәнді атрибут",
            ],
            "correct_indices": [1],
            "topic": "ER-модельдеу",
        },
        {
            "text": "Туынды атрибутқа мысал:",
            "options": [
                "Туған күні",
                "Жасы (туған күннен есептеледі)",
                "Аты",
                "ИИН",
            ],
            "correct_indices": [1],
            "topic": "ER-модельдеу",
        },
        {
            "text": "Әлсіз субъект (weak entity) дегеніміз не?",
            "options": [
                "Өз кілті бар субъект",
                "Басқа субъектке тәуелді, жеке кілті жоқ субъект",
                "Байланыссыз субъект",
                "Атрибутсыз субъект",
            ],
            "correct_indices": [1],
            "topic": "ER-модельдеу",
        },
        {
            "text": "Мысал: Бөлме (Room) → Ғимарат (Building). Бөлме қандай субъект?",
            "options": ["Күшті субъект", "Әлсіз субъект", "Байланыс", "Атрибут"],
            "correct_indices": [1],
            "topic": "ER-модельдеу",
        },
        {
            "text": "Толық қатысу (total participation) дегеніміз не?",
            "options": [
                "Субъектінің бір бөлігі қатысады",
                "Субъектінің барлық даналары байланысқа қатысуы керек",
                "Байланыс міндетті емес",
                "Байланыс жоқ",
            ],
            "correct_indices": [1],
            "topic": "ER-модельдеу",
        },
        {
            "text": "Жартылай қатысу (partial participation) дегеніміз не?",
            "options": [
                "Барлық даналар қатысады",
                "Субъектінің бір бөлігі ғана байланысқа қатысады",
                "Байланыс жоқ",
                "Субъект жоқ",
            ],
            "correct_indices": [1],
            "topic": "ER-модельдеу",
        },
        {
            "text": "Рекурсивті байланыс дегеніміз не?",
            "options": [
                "Үш субъект арасындағы байланыс",
                "Субъект өзімен-өзі байланысады",
                "Екі кесте арасындағы байланыс",
                "Кілтсіз байланыс",
            ],
            "correct_indices": [1],
            "topic": "ER-модельдеу",
        },
        {
            "text": "Рекурсивті байланысқа мысал:",
            "options": [
                "Студент — Пән",
                "Қызметкер — Басшысы (өзі де қызметкер)",
                "Кітап — Автор",
                "Тапсырыс — Клиент",
            ],
            "correct_indices": [1],
            "topic": "ER-модельдеу",
        },
        {
            "text": "Cardinality (кардиналдылық) нені көрсетеді?",
            "options": [
                "Атрибуттар санын",
                "Байланыстағы субъект даналарының арақатынасын",
                "Кестелер санын",
                "Бағандар санын",
            ],
            "correct_indices": [1],
            "topic": "ER-модельдеу",
        },
        # === ADDITIONAL НОРМАЛИЗАЦИЯ (15 more) ===
        {
            "text": "2NF шарты қандай?",
            "options": [
                "1NF + көп мәнді атрибуттар жоқ",
                "1NF + жартылай функционалдық тәуелділік жоқ",
                "Транзитивті тәуелділік жоқ",
                "BCNF + атомарлы мәндер",
            ],
            "correct_indices": [1],
            "topic": "Нормализация",
        },
        {
            "text": "3NF шарты қандай?",
            "options": [
                "Атомарлы мәндер",
                "Жартылай тәуелділік жоқ",
                "2NF + транзитивті тәуелділік жоқ",
                "BCNF",
            ],
            "correct_indices": [2],
            "topic": "Нормализация",
        },
        {
            "text": "BCNF (Бойс-Кодд) формасының ерекшелігі не?",
            "options": [
                "Тек атомарлы мәндер",
                "Әрбір детерминант кандидат кілт болуы керек",
                "Транзитивті тәуелділік бар",
                "Көп мәнді атрибуттар бар",
            ],
            "correct_indices": [1],
            "topic": "Нормализация",
        },
        {
            "text": "Жартылай функционалдық тәуелділік дегеніміз не?",
            "options": [
                "Атрибут барлық кілтке тәуелді",
                "Атрибут құрама кілттің бір бөлігіне тәуелді",
                "Транзитивті тәуелділік",
                "Кілтсіз тәуелділік",
            ],
            "correct_indices": [1],
            "topic": "Нормализация",
        },
        {
            "text": "Транзитивті тәуелділік дегеніміз не?",
            "options": [
                "A → B, ал B → C болса, A → C",
                "Тікелей тәуелділік",
                "Жартылай тәуелділік",
                "Кілтке тәуелділік",
            ],
            "correct_indices": [0],
            "topic": "Нормализация",
        },
        {
            "text": "Кандидат кілт дегеніміз не?",
            "options": [
                "Кез келген атрибут",
                "Жазбаны бірегей анықтай алатын минималды атрибуттар жиыны",
                "Foreign Key",
                "Индекс",
            ],
            "correct_indices": [1],
            "topic": "Нормализация",
        },
        {
            "text": "Суперкілт дегеніміз не?",
            "options": [
                "Минималды кілт",
                "Жазбаны бірегей анықтайтын кез келген атрибуттар жиыны",
                "Foreign Key",
                "Атомарлы атрибут",
            ],
            "correct_indices": [1],
            "topic": "Нормализация",
        },
        {
            "text": "Атомарлы мән дегеніміз не?",
            "options": [
                "Бөлуге болатын мән",
                "Бөлуге болмайтын ең қарапайым мән",
                "Көп мәнді атрибут",
                "Күрделі атрибут",
            ],
            "correct_indices": [1],
            "topic": "Нормализация",
        },
        {
            "text": "1NF-ті бұзатын мысал қандай?",
            "options": [
                "Әр ұяшықта бір мән",
                "Бір ұяшықта бірнеше телефон нөмірі",
                "Primary Key бар",
                "Foreign Key бар",
            ],
            "correct_indices": [1],
            "topic": "Нормализация",
        },
        {
            "text": "Нормализацияның негізгі мақсаты не?",
            "options": [
                "Деректерді шифрлау",
                "Артық деректер мен аномалияларды азайту",
                "Сұраныс жылдамдығын арттыру",
                "Кестелерді көбейту",
            ],
            "correct_indices": [1],
            "topic": "Нормализация",
        },
        {
            "text": "Кірістіру аномалиясы (insertion anomaly) дегеніміз не?",
            "options": [
                "Деректі жаңарту қиын",
                "Қосымша ақпаратсыз жаңа дерек қосу мүмкін емес",
                "Деректі жою қиын",
                "Іздеу қиын",
            ],
            "correct_indices": [1],
            "topic": "Нормализация",
        },
        {
            "text": "Жаңарту аномалиясы (update anomaly) дегеніміз не?",
            "options": [
                "Бір деректі өзгерту үшін көп жерде өзгерту керек",
                "Дерек қосу мүмкін емес",
                "Дерек жою мүмкін емес",
                "Іздеу баяу",
            ],
            "correct_indices": [0],
            "topic": "Нормализация",
        },
        {
            "text": "Жою аномалиясы (deletion anomaly) дегеніміз не?",
            "options": [
                "Дерек жою кезінде қажетті ақпарат жоғалады",
                "Дерек қосу қиын",
                "Дерек жаңарту қиын",
                "Іздеу нәтижесі қате",
            ],
            "correct_indices": [0],
            "topic": "Нормализация",
        },
        {
            "text": "4NF қандай тәуелділікті жояды?",
            "options": [
                "Функционалдық тәуелділік",
                "Көп мәнді тәуелділік",
                "Транзитивті тәуелділік",
                "Жартылай тәуелділік",
            ],
            "correct_indices": [1],
            "topic": "Нормализация",
        },
        {
            "text": "Денормализацияның кемшілігі не?",
            "options": [
                "Жылдамдық артады",
                "Артық деректер мен аномалиялар пайда болады",
                "Кестелер азаяды",
                "Индекс қажет емес",
            ],
            "correct_indices": [1],
            "topic": "Нормализация",
        },
        # === ADDITIONAL КІЛТТЕР (10 more) ===
        {
            "text": "Composite Key (құрама кілт) дегеніміз не?",
            "options": [
                "Бір атрибуттан тұратын кілт",
                "Екі немесе одан көп атрибуттан тұратын кілт",
                "Foreign Key",
                "Индекс",
            ],
            "correct_indices": [1],
            "topic": "Кілттер",
        },
        {
            "text": "Alternate Key дегеніміз не?",
            "options": [
                "Primary Key болып таңдалмаған кандидат кілт",
                "Foreign Key",
                "Composite Key",
                "Суперкілт",
            ],
            "correct_indices": [0],
            "topic": "Кілттер",
        },
        {
            "text": "Surrogate Key дегеніміз не?",
            "options": [
                "Бизнес мәні бар кілт",
                "Жүйе автоматты құратын мәнсіз бірегей кілт",
                "Foreign Key",
                "Composite Key",
            ],
            "correct_indices": [1],
            "topic": "Кілттер",
        },
        {
            "text": "Natural Key дегеніміз не?",
            "options": [
                "Жүйе құратын кілт",
                "Нақты мәні бар, бизнес логикадан алынған кілт",
                "Foreign Key",
                "Индекс",
            ],
            "correct_indices": [1],
            "topic": "Кілттер",
        },
        {
            "text": "Natural Key мысалы:",
            "options": ["Auto-increment ID", "ИИН", "UUID", "Sequence"],
            "correct_indices": [1],
            "topic": "Кілттер",
        },
        {
            "text": "Primary Key NULL бола ала ма?",
            "options": ["Иә", "Жоқ, әрқашан NOT NULL", "Кейде", "Белгісіз"],
            "correct_indices": [1],
            "topic": "Кілттер",
        },
        {
            "text": "Foreign Key NULL бола ала ма?",
            "options": [
                "Ешқашан жоқ",
                "Иә, егер байланыс міндетті болмаса",
                "Әрқашан NULL",
                "Белгісіз",
            ],
            "correct_indices": [1],
            "topic": "Кілттер",
        },
        {
            "text": "ON DELETE CASCADE не істейді?",
            "options": [
                "Жоюды болдырмайды",
                "Ата-аналық жазба жойылғанда байланысты жазбаларды да жояды",
                "NULL қояды",
                "Ештеңе істемейді",
            ],
            "correct_indices": [1],
            "topic": "Кілттер",
        },
        {
            "text": "ON DELETE SET NULL не істейді?",
            "options": [
                "Жазбаларды жояды",
                "Ата-аналық жазба жойылғанда FK-ға NULL қояды",
                "Ештеңе істемейді",
                "Қатені қайтарады",
            ],
            "correct_indices": [1],
            "topic": "Кілттер",
        },
        {
            "text": "Unique Key мен Primary Key айырмашылығы не?",
            "options": [
                "Айырмашылық жоқ",
                "Unique Key NULL болуы мүмкін, бірақ PK мүмкін емес",
                "PK NULL болуы мүмкін",
                "Unique Key бірегей емес",
            ],
            "correct_indices": [1],
            "topic": "Кілттер",
        },
        # === ADDITIONAL SQL (25 more) ===
        {
            "text": "SELECT * FROM students; — бұл сұраныс не істейді?",
            "options": [
                "Бір бағанды қайтарады",
                "Барлық бағандарды қайтарады",
                "Студенттерді жояды",
                "Кесте құрады",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "WHERE шарты не үшін қолданылады?",
            "options": [
                "Деректерді сұрыптау",
                "Деректерді фильтрлеу",
                "Деректерді топтастыру",
                "Деректерді біріктіру",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "HAVING шарты WHERE-ден немен ерекшеленеді?",
            "options": [
                "Айырмашылық жоқ",
                "HAVING агрегаттық функциялармен қолданылады, WHERE жоқ",
                "WHERE жылдамырақ",
                "HAVING барлық жазбаларды қайтарады",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "SUM() функциясы не істейді?",
            "options": [
                "Санын есептейді",
                "Қосындысын табады",
                "Орташасын табады",
                "Максимумды табады",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "MAX() функциясы не істейді?",
            "options": [
                "Минимумды табады",
                "Қосындысын табады",
                "Максималды мәнді табады",
                "Орташаны табады",
            ],
            "correct_indices": [2],
            "topic": "SQL",
        },
        {
            "text": "MIN() функциясы не істейді?",
            "options": [
                "Максималды мәнді табады",
                "Ең кіші мәнді табады",
                "Қосындысын табады",
                "Санын табады",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "DISTINCT кілтсөзі не істейді?",
            "options": [
                "Барлық жазбаларды қайтарады",
                "Қайталанатын мәндерді жояды (бірегейлерін қайтарады)",
                "Сұрыптайды",
                "Топтайды",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "ORDER BY ... ASC нені білдіреді?",
            "options": [
                "Кему ретімен сұрыптау",
                "Өсу ретімен сұрыптау",
                "Кездейсоқ реттеу",
                "Топтастыру",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "RIGHT JOIN қандай жазбаларды қайтарады?",
            "options": [
                "Тек сәйкестіктер",
                "Сол жақтың барлығы + сәйкестіктер",
                "Оң жақтың барлығы + сәйкестіктер",
                "Барлық жазбалар",
            ],
            "correct_indices": [2],
            "topic": "SQL",
        },
        {
            "text": "FULL OUTER JOIN қандай жазбаларды қайтарады?",
            "options": [
                "Тек сәйкестер",
                "Сол жақтың барлығы",
                "Оң жақтың барлығы",
                "Екі кестенің барлық жазбалары + сәйкестіктер",
            ],
            "correct_indices": [3],
            "topic": "SQL",
        },
        {
            "text": "CROSS JOIN не қайтарады?",
            "options": [
                "Тек сәйкестер",
                "Декарт көбейтіндісі (барлық мүмкін жұптар)",
                "Бос нәтиже",
                "Бір жазба",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "INSERT INTO командасы не істейді?",
            "options": [
                "Деректі жаңартады",
                "Жаңа жазба қосады",
                "Деректі жояды",
                "Кесте құрады",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "UPDATE командасы не істейді?",
            "options": [
                "Жаңа жазба қосады",
                "Бар жазбаны жаңартады",
                "Жазбаны жояды",
                "Кестені жояды",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "DELETE FROM командасы не істейді?",
            "options": [
                "Кестені толық жояды",
                "Белгілі жазбаларды жояды",
                "Жазба қосады",
                "Кесте құрады",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "TRUNCATE TABLE командасы не істейді?",
            "options": [
                "Бір жазбаны жояды",
                "Кестедегі барлық жазбаларды тез жояды",
                "Кестенің құрылымын жояды",
                "Жазба қосады",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "CREATE TABLE командасы не істейді?",
            "options": [
                "Кестені жояды",
                "Жаңа кесте құрады",
                "Деректер қосады",
                "Деректерді жаңартады",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "DROP TABLE командасы не істейді?",
            "options": [
                "Деректерді жояды",
                "Кестенің өзін толық жояды",
                "Кесте құрады",
                "Деректерді жаңартады",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "ALTER TABLE командасы не істейді?",
            "options": [
                "Кесте жояды",
                "Кесте құрылымын өзгертеді (баған қосу, жою)",
                "Деректер қосады",
                "Деректер жояды",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "LIKE операторы не үшін қолданылады?",
            "options": [
                "Сандарды салыстыру",
                "Үлгі бойынша жолды іздеу",
                "Деректерді сұрыптау",
                "Деректерді топтау",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "LIKE операторындағы '%' символы не білдіреді?",
            "options": [
                "Нақты бір символ",
                "Кез келген саны символдар",
                "Бос мән",
                "Сан",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "LIKE операторындағы '_' символы не білдіреді?",
            "options": [
                "Кез келген саны символдар",
                "Тек бір символ",
                "Бос мән",
                "Кез келген сан",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "IN операторы не істейді?",
            "options": [
                "Диапазонды тексереді",
                "Мәннің тізімде бар-жоғын тексереді",
                "NULL тексереді",
                "Деректерді біріктіреді",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "BETWEEN операторы не істейді?",
            "options": [
                "Тізімде бар-жоғын тексереді",
                "Мәннің диапазонда екенін тексереді",
                "NULL тексереді",
                "Деректерді біріктіреді",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "IS NULL операторы не істейді?",
            "options": [
                "Мәннің нөлге тең екенін тексереді",
                "Мәннің NULL екенін тексереді",
                "Мәннің бос жол екенін тексереді",
                "Сандарды салыстырады",
            ],
            "correct_indices": [1],
            "topic": "SQL",
        },
        {
            "text": "EXCEPT операторы не қайтарады?",
            "options": [
                "Барлық нәтижелерді біріктіреді",
                "Ортақ бөлікті қайтарады",
                "Бірінші жиыннан екіншісін алып тастағандағы айырмашылықты",
                "NULL мәндерді",
            ],
            "correct_indices": [2],
            "topic": "SQL",
        },
        # === ADDITIONAL ACID & ТРАНЗАКЦИЯЛАР (10 more) ===
        {
            "text": "Consistency (ACID) дегеніміз не?",
            "options": [
                "Толық орындалу",
                "Дерекқор транзакциядан кейін дұрыс күйде қалады",
                "Оқшаулау",
                "Тұрақтылық",
            ],
            "correct_indices": [1],
            "topic": "Транзакциялар",
        },
        {
            "text": "COMMIT командасы не істейді?",
            "options": [
                "Транзакцияны болдырмайды",
                "Транзакциядағы өзгерістерді тұрақты сақтайды",
                "Транзакцияны бастайды",
                "Деректерді жояды",
            ],
            "correct_indices": [1],
            "topic": "Транзакциялар",
        },
        {
            "text": "ROLLBACK командасы не істейді?",
            "options": [
                "Өзгерістерді сақтайды",
                "Транзакцияны болдырмайды, өзгерістерді қайтарады",
                "Транзакцияны бастайды",
                "Деректер қосады",
            ],
            "correct_indices": [1],
            "topic": "Транзакциялар",
        },
        {
            "text": "Dirty Read дегеніміз не?",
            "options": [
                "Commit болған деректі оқу",
                "Басқа транзакцияның commit болмаған деректін оқу",
                "Қате оқу",
                "Тез оқу",
            ],
            "correct_indices": [1],
            "topic": "Транзакциялар",
        },
        {
            "text": "Phantom Read дегеніміз не?",
            "options": [
                "Бір дерек екі рет өзгерген",
                "Екі оқу арасында басқа транзакция жаңа жазба қосқан",
                "Деректі табу мүмкін емес",
                "Деректі жою",
            ],
            "correct_indices": [1],
            "topic": "Транзакциялар",
        },
        {
            "text": "READ COMMITTED изоляция деңгейі нені қамтамасыз етеді?",
            "options": [
                "Ешқандай қорғаныс жоқ",
                "Dirty Read болмайды",
                "Phantom Read болмайды",
                "Толық оқшаулау",
            ],
            "correct_indices": [1],
            "topic": "Транзакциялар",
        },
        {
            "text": "SERIALIZABLE изоляция деңгейі нені қамтамасыз етеді?",
            "options": [
                "Ең төменгі қорғаныс",
                "Dirty Read ғана алдын алады",
                "Ең жоғары изоляция, барлық проблемаларды болдырмайды",
                "Оқшаулау жоқ",
            ],
            "correct_indices": [2],
            "topic": "Транзакциялар",
        },
        {
            "text": "Deadlock дегеніміз не?",
            "options": [
                "Транзакция сәтті аяқталды",
                "Екі транзакция бір-бірінің құлпын күтіп тұрып қалу",
                "Деректерді жылдам оқу",
                "Индекс құру",
            ],
            "correct_indices": [1],
            "topic": "Транзакциялар",
        },
        {
            "text": "SAVEPOINT не істейді?",
            "options": [
                "Транзакцияны аяқтайды",
                "Транзакция ішінде бақылау нүктесін құрады",
                "Деректерді жояды",
                "Кестені құрады",
            ],
            "correct_indices": [1],
            "topic": "Транзакциялар",
        },
        {
            "text": "Lost Update дегеніміз не?",
            "options": [
                "Дерек табылмады",
                "Бір транзакцияның өзгертуі екіншісімен қайта жазылды",
                "Дерек жойылды",
                "Жаңа дерек қосылды",
            ],
            "correct_indices": [1],
            "topic": "Транзакциялар",
        },
        # === ADDITIONAL АРХИТЕКТУРА & ТҰТАСТЫҚ (10 more) ===
        {
            "text": "Файл-сервер архитектурасының кемшілігі не?",
            "options": [
                "Жылдам жұмыс істейді",
                "Желі жүктемесі үлкен, қауіпсіздік төмен",
                "Қорғаныс жоғары",
                "Бөлек логика қабаты бар",
            ],
            "correct_indices": [1],
            "topic": "Архитектура",
        },
        {
            "text": "Клиент-сервер архитектурасының артықшылығы не?",
            "options": [
                "Барлық логика клиентте",
                "Сервер деректер мен логиканы басқарады",
                "Желі қажет емес",
                "Бір компьютер жеткілікті",
            ],
            "correct_indices": [1],
            "topic": "Архитектура",
        },
        {
            "text": "3-tier архитектурадағы 'Business Logic' қабаты не істейді?",
            "options": [
                "Деректерді сақтайды",
                "Қолданба логикасын орындайды",
                "Пайдаланушы интерфейсін көрсетеді",
                "Желіні басқарады",
            ],
            "correct_indices": [1],
            "topic": "Архитектура",
        },
        {
            "text": "Семантикалық тұтастық дегеніміз не?",
            "options": [
                "Типтердің дұрыстығы",
                "Байланыстардың дұрыстығы",
                "Деректердің бизнес логикаға сәйкестігі",
                "Кілттердің дұрыстығы",
            ],
            "correct_indices": [2],
            "topic": "Тұтастық",
        },
        {
            "text": "CHECK constraint не істейді?",
            "options": [
                "Primary Key құрады",
                "Мәнге шектеу қояды (мыс: age > 0)",
                "Foreign Key орнатады",
                "Индекс құрады",
            ],
            "correct_indices": [1],
            "topic": "Тұтастық",
        },
        {
            "text": "NOT NULL constraint не істейді?",
            "options": [
                "Мәннің бос болуын талап етеді",
                "Мәннің NULL болмауын талап етеді",
                "Мәнді автоматты толтырады",
                "Индекс құрады",
            ],
            "correct_indices": [1],
            "topic": "Тұтастық",
        },
        {
            "text": "UNIQUE constraint не істейді?",
            "options": [
                "NULL мәнге рұқсат береді",
                "Бағандағы мәндердің бірегейлігін қамтамасыз етеді",
                "Primary Key орнатады",
                "Деректерді шифрлайды",
            ],
            "correct_indices": [1],
            "topic": "Тұтастық",
        },
        {
            "text": "DEFAULT constraint не істейді?",
            "options": [
                "Мәнді жояды",
                "Мән берілмесе әдепкі мән қояды",
                "Мәнді шифрлайды",
                "Индекс құрады",
            ],
            "correct_indices": [1],
            "topic": "Тұтастық",
        },
        {
            "text": "Индекс (Index) не үшін қолданылады?",
            "options": [
                "Деректерді шифрлау",
                "Іздеу жылдамдығын арттыру",
                "Деректерді жою",
                "Кесте құру",
            ],
            "correct_indices": [1],
            "topic": "Архитектура",
        },
        {
            "text": "Индекстің кемшілігі не?",
            "options": [
                "Іздеу баяулайды",
                "Жазу операциялары баяулайды, қосымша жады керек",
                "Деректер жойылады",
                "Кемшілігі жоқ",
            ],
            "correct_indices": [1],
            "topic": "Архитектура",
        },
    ],
}


def seed():
    print("🚀 Базаны статикалық сұрақтармен толтыру басталуда...")

    # Delete existing database file to avoid corruption issues
    db_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "magistracy_prep.db"
    )
    if os.path.exists(db_path):
        try:
            os.remove(db_path)
            print(f"✅ Ескі дерекқор файлы жойылды: {db_path}")
        except Exception as e:
            print(f"⚠️ Дерекқор файлын жою қатесі: {e}")

    # Create fresh tables
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        # Create Subjects
        subject_map = {
            SubjectId.ENGLISH: "Шет тілі (Ағылшын)",
            SubjectId.TGO: "Оқу дайындығын анықтау (ОДАТ)",
            SubjectId.ALGO: "Алгоритмдер және деректер құрылымы",
            SubjectId.DB: "Дерекқор базасы (SQL)",
        }

        for sub_id, sub_name in subject_map.items():
            db_sub = DBSubject(id=sub_id.value, name=sub_name)
            db.add(db_sub)
            db.commit()

            # Add Questions
            questions = STATIC_QUESTIONS.get(sub_id, [])
            for q_data in questions:
                q_id = str(uuid.uuid4())
                q_type = (
                    QuestionType.MULTIPLE
                    if sub_id == SubjectId.DB and len(q_data["correct_indices"]) > 1
                    else QuestionType.SINGLE
                )

                db_q = DBQuestion(
                    id=q_id,
                    subject_id=sub_id.value,
                    text=q_data["text"],
                    type=q_type,
                    topic=q_data.get("topic", "General"),
                    reading_passage=q_data.get("reading_passage"),
                )
                db.add(db_q)
                db.flush()

                # Add Options
                correct_ids = []
                for i, opt_text in enumerate(q_data["options"]):
                    opt_id = str(uuid.uuid4())
                    db_opt = DBOption(id=opt_id, question_id=q_id, text=opt_text)
                    db.add(db_opt)
                    if i in q_data["correct_indices"]:
                        correct_ids.append(opt_id)

                db_q.correct_option_ids = ",".join(correct_ids)

            db.commit()
            print(f"✅ {sub_name} бойынша сұрақтар қосылды.")

        print("\n🎉 Сәтті! База толықтай статикалық деректермен толтырылды.")
        print("Енді нейросетке (AI) мүлдем сұраныс жіберілмейді.")

    except Exception as e:
        print(f"❌ Қате: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed()
