from models import SubjectDefinition, SubjectId, QuestionType, SubCategory

english_definition = SubjectDefinition(
    id=SubjectId.ENGLISH,
    name="Шет тілі (Ағылшын)",
    defaultQuestionType=QuestionType.SINGLE,
    promptContext="""
    Generate questions strictly following the Kazakhstan Master's KT format for English.
    Divide the questions into 3 specific blocks:

    1. LISTENING (Simulated):
       - Since audio cannot be played, provide a "Transcript" text (approx 100-150 words) in the 'codeSnippet' field.
       - Topics: Famous people (e.g., Akio Morita, Steve Jobs), Leadership qualities, Company principles.
       - Question types: Specific data (Who? What? When?), identifying the Speaker's main idea, completing sentences based on the transcript.

    2. LEXICO-GRAMMATICAL TEST:
       - Grammar Focus: 
         * Conditionals (If sentences: "If I were...", "If you had known...").
         * Tenses (Present/Past/Future Perfect & Continuous).
         * Modal Verbs (could, can, should, would).
       - Vocabulary Focus:
         * Synonyms/Antonyms (e.g., improve = boost, founded = established).
         * Academic Vocabulary (terms related to business, education, technology, e.g., 'start-up', 'globalization').
         * Prefixes & Suffixes (un-, in-, im-, dis-).

    3. READING:
       - Provide an academic or scientific text passage (approx 150-200 words) in the 'codeSnippet' field.
       - Topics: Effect of music on the brain, Role of IT in education, Ecology/Environment.
       - Question types: Main Idea, True/False statements, Finding vocabulary meaning in context.
    """,
    questionTypeInstruction="All questions are Single Choice (1 correct answer). For Listening and Reading sections, YOU MUST provide the text in the 'codeSnippet' field.",
    subCategories=[
        SubCategory(
            name="Listening (Тыңдалым)",
            description="Transcript comprehension: Famous people, Leadership.",
        ),
        SubCategory(
            name="Grammar & Vocabulary",
            description="Conditionals, Tenses, Synonyms, Academic Vocab.",
        ),
        SubCategory(
            name="Reading (Оқылым)",
            description="Academic texts: Music & Brain, IT, Ecology.",
        ),
    ],
)

tgo_definition = SubjectDefinition(
    id=SubjectId.TGO,
    name="Оқу дайындығын анықтау (ОДАТ)",
    defaultQuestionType=QuestionType.SINGLE,
    promptContext="""
    Generate questions strictly following the Official TGO (ODAT) structure for Master's preparation.
    There are TWO main blocks. You must generate questions for both:

    1. ANALYTICAL THINKING (Аналитикалық ойлау):
       - Focus: Logic, Mathematical reasoning, Problem solving.
       - Question types: 
         * Logical sequences and series (Numbers, Shapes).
         * Mathematical logic (Work, Speed, Percentages, Proportions).
         * Data Interpretation (Analyzing tables, diagrams, charts).
         * "Quantity Comparison": Column A vs Column B.

    2. CRITICAL THINKING (Сыни ойлау):
       - Focus: Reading comprehension, Argument analysis.
       - Provide a short text passage (3-5 sentences) in 'codeSnippet' for context.
       - Question types:
         * Identifying the main idea.
         * determining the author's position/tone.
         * Deriving valid conclusions from the text.
         * Strengthening or weakening an argument.
    """,
    questionTypeInstruction="All questions are Single Choice (1 correct answer). For Critical Thinking questions, provide the reading passage in 'codeSnippet'.",
    subCategories=[
        SubCategory(
            name="Аналитикалық ойлау",
            description="Математикалық логика, Заңдылықтар, Кестелер, Салыстыру.",
        ),
        SubCategory(
            name="Сыни ойлау",
            description="Мәтінді талдау, Негізгі ой, Логикалық қорытынды.",
        ),
    ],
)

algo_definition = SubjectDefinition(
    id=SubjectId.ALGO,
    name="Алгоритмдер және деректер құрылымы",
    defaultQuestionType=QuestionType.SINGLE,
    promptContext="""
    This is the most technical block (M094 specialization).
    Generate Single Choice questions covering these 4 specific levels:

    1. PROGRAMMING BASICS (C++):
       - Provide C++ code snippets in 'codeSnippet'.
       - Focus: Nested loops (processing 2D arrays), if-else/switch logic, Structs.
       - Logic scenarios: Choosing the right loop (while vs do-while) for tasks like calculating averages.

    2. ABSTRACT DATA TYPES (ADT):
       - Stack: LIFO principle.
       - Queue: FIFO principle, connection to singly linked lists.
       - Lists: Difference between Singly and Doubly linked lists.
       - Trees: Binary Search Trees (BST), calculating height, search paths.

    3. GRAPH ALGORITHMS (Theory & Application):
       - Shortest Path: 
         * Dijkstra (non-negative weights).
         * Bellman-Ford (handles negative weights).
         * Floyd-Warshall (all-pairs shortest path).
       - Minimum Spanning Trees (MST): Prim's and Kruskal's algorithms.

    4. ALGORITHM COMPLEXITY (Big O):
       - Calculate Time Complexity for provided code snippets.
       - Standard notations: O(1), O(log n), O(n), O(n log n), O(n^2).
       - Example logic to test: A loop O(n) containing an operation O(log n) results in O(n log n).
    """,
    questionTypeInstruction="Strictly Single Choice questions. Use C++ for code snippets.",
    subCategories=[
        SubCategory(
            name="Программалау негіздері (C++)",
            description="Циклдер (nested), Шартты операторлар, Struct, Массивтер.",
        ),
        SubCategory(
            name="Деректердің абстрактілі типтері",
            description="Stack (LIFO), Queue (FIFO), Тізімдер, BST ағаштары.",
        ),
        SubCategory(
            name="Графтар алгоритмі",
            description="Дейкстра, Беллман-Форд, Флойд-Уоршелл, Прим, Крускал.",
        ),
        SubCategory(
            name="Алгоритм тиімділігі",
            description="Big O нотациясы, уақытша күрделілікті есептеу.",
        ),
    ],
)

db_definition = SubjectDefinition(
    id=SubjectId.DB,
    name="Дерекқор базасы (SQL)",
    defaultQuestionType=QuestionType.MULTIPLE,
    promptContext="""
    This is a Profile subject. Generate MULTIPLE CHOICE questions (with 1 or more correct answers) covering these 4 blocks:

    1. DESIGN & ER-MODELING:
       - ER Diagrams: Concepts of Entity (Subject), Relationship, Attributes.
       - Questions like "What does 'E' stand for in ER?" or identifying 1:1, 1:M, M:N relationships.
       - Keys: Primary Key, Foreign Key definition.

    2. RELATIONAL MODEL & NORMALIZATION:
       - Normalization Levels: 1NF, 2NF, 3NF, BCNF requirements.
       - Functional Dependency: Understanding notation like X -> Y.
       - Questions about why we normalize (e.g., to reduce redundancy) or conditions for 3NF.

    3. SQL (PRACTICAL):
       - MUST include SQL code snippets in 'codeSnippet'.
       - SELECT, ORDER BY (ASC/DESC), LIMIT.
       - Aggregates: SUM, AVG, COUNT, MAX, MIN with GROUP BY and HAVING.
       - Set Operations: UNION, INTERSECT, EXCEPT.
       - Joins: Inner vs Left Join logic.

    4. DBMS ARCHITECTURE & INTEGRITY:
       - Architecture types: File-server, Client-server (2-tier), 3-tier.
       - Integrity Constraints: Domain, Referential, Semantic.
       - Transactions: ACID properties (Atomicity, Consistency, Isolation, Durability).
    """,
    questionTypeInstruction="Generate MULTIPLE CHOICE questions. There can be 1, 2, or 3 correct answers out of the options. Mark all correct indices.",
    subCategories=[
        SubCategory(
            name="ER-модельдеу және Жобалау",
            description="Entity, Relationship, Кілттер, Байланыс түрлері.",
        ),
        SubCategory(
            name="Реляциялық модель және Нормализация",
            description="1NF-BCNF, Функционалдық тәуелділік.",
        ),
        SubCategory(
            name="SQL (Практика)", description="SELECT, JOIN, GROUP BY, HAVING, UNION."
        ),
        SubCategory(
            name="Архитектура және Тұтастық",
            description="Client-Server, ACID, Integrity constraints.",
        ),
    ],
)

SUBJECT_DEFINITIONS = {
    SubjectId.ENGLISH: english_definition,
    SubjectId.TGO: tgo_definition,
    SubjectId.ALGO: algo_definition,
    SubjectId.DB: db_definition,
}


def get_subject_definition(subject_id: SubjectId) -> SubjectDefinition:
    return SUBJECT_DEFINITIONS.get(subject_id)
