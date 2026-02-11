# Reading Comprehension Texts and Questions
# Based on Spetsifikatsiya-a_ylshyn-tili-_kaz_.md specification
# Each text has 8 questions with A, B, C difficulty levels

READING_TEXTS = [
    # ============ ТАҚЫРЫП 1: АДАМ, ҚОҒАМ ЖӘНЕ РУХАНИ ҚҰНДЫЛЫҚ ============
    # Text 1: Family and Marriage (A1-A2 level)
    {
        "id": "reading_family_values",
        "title": "Family Values in Modern Society",
        "level": "A1-A2",
        "topic": "reading",
        "passage": """FAMILY VALUES IN MODERN SOCIETY

The concept of family has evolved significantly over the past few decades. In many countries, the traditional family structure of two parents and their children is no longer the only norm. Today, we see single-parent families, blended families, and multi-generational households living together.

Despite these changes, certain family values remain constant across cultures. Love, respect, and support for one another continue to be the foundation of strong families. Parents still prioritize their children's education and well-being. Grandparents often play an important role in passing down traditions and wisdom to younger generations.

In Kazakhstan, family ties are particularly strong. Many young adults live with their parents until marriage, and it's common for extended family members to gather for holidays and celebrations. The concept of "ағайын" (kinship) extends beyond immediate family to include distant relatives who support each other in times of need.

Modern families face new challenges too. Busy work schedules can limit quality time together. Technology, while connecting us globally, sometimes creates distance within homes. Finding balance between career ambitions and family responsibilities has become a key concern for many couples.""",
        "questions": [
            {
                "text": "According to the passage, what remains constant in families despite structural changes?",
                "options": [
                    "Work schedules",
                    "Technology use",
                    "Love, respect, and support",
                    "Living arrangements",
                ],
                "correct": 2,
                "difficulty": "A",
            },
            {
                "text": "What does 'ағайын' refer to in Kazakh culture?",
                "options": [
                    "Immediate family only",
                    "Extended kinship relations",
                    "Neighbors",
                    "Colleagues",
                ],
                "correct": 1,
                "difficulty": "A",
            },
            {
                "text": "According to the text, when do many Kazakh young adults move out of their parents' home?",
                "options": [
                    "After university",
                    "After finding a job",
                    "After marriage",
                    "At age 18",
                ],
                "correct": 2,
                "difficulty": "B",
            },
            {
                "text": "What role do grandparents typically play in families?",
                "options": [
                    "Financial support only",
                    "Passing down traditions and wisdom",
                    "Cooking meals",
                    "Babysitting",
                ],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "What challenge does technology create within families?",
                "options": [
                    "It's too expensive",
                    "It creates distance despite connecting globally",
                    "Children don't know how to use it",
                    "Parents ban it completely",
                ],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "Which family structure is described as 'no longer the only norm'?",
                "options": [
                    "Single-parent families",
                    "Two parents with children",
                    "Multi-generational households",
                    "Blended families",
                ],
                "correct": 1,
                "difficulty": "C",
            },
            {
                "text": "What main concern do modern couples face according to the passage?",
                "options": [
                    "Finding affordable housing",
                    "Balancing career and family",
                    "Learning new technology",
                    "Moving to different countries",
                ],
                "correct": 1,
                "difficulty": "C",
            },
            {
                "text": "The word 'blended' in the context of families most likely means:",
                "options": [
                    "Mixed from different previous marriages",
                    "Living in apartments",
                    "Having many children",
                    "Speaking multiple languages",
                ],
                "correct": 0,
                "difficulty": "C",
            },
        ],
    },
    # Text 2: Career and Profession (A2-B1 level)
    {
        "id": "reading_career_choices",
        "title": "Choosing the Right Career Path",
        "level": "A2-B1",
        "topic": "reading",
        "passage": """CHOOSING THE RIGHT CAREER PATH

Selecting a career is one of the most important decisions a person makes in their lifetime. This choice affects not only financial stability but also personal happiness and life satisfaction. Career counselors suggest considering several factors when making this crucial decision.

First, self-assessment is essential. Understanding your strengths, weaknesses, interests, and values helps narrow down suitable career options. Someone who enjoys working with numbers might thrive in accounting or finance, while a creative individual might excel in design or marketing.

Second, research the job market. Some professions are in high demand, offering better salaries and job security. In Kazakhstan, IT specialists, engineers, and healthcare professionals are particularly sought after. However, passion should not be sacrificed entirely for job prospects.

Third, consider the required education and training. Some careers require many years of study, while others offer faster entry through vocational training or apprenticeships. Weighing the time and financial investment against potential returns is practical.

Finally, work-life balance matters. Some careers demand long hours and frequent travel, while others offer more flexibility. Understanding your priorities—whether it's spending time with family or advancing quickly in your field—helps align career choices with personal goals.

Many successful people have changed careers multiple times throughout their lives. The key is continuous learning and staying adaptable in an ever-changing job market.""",
        "questions": [
            {
                "text": "What is the main topic of this passage?",
                "options": [
                    "Education systems",
                    "Career selection factors",
                    "Salary negotiations",
                    "Job interviews",
                ],
                "correct": 1,
                "difficulty": "A",
            },
            {
                "text": "According to the text, what does self-assessment help with?",
                "options": [
                    "Getting higher salaries",
                    "Narrowing down career options",
                    "Finding employers",
                    "Writing resumes",
                ],
                "correct": 1,
                "difficulty": "A",
            },
            {
                "text": "Which professions are mentioned as high-demand in Kazakhstan?",
                "options": [
                    "Teachers and artists",
                    "IT specialists, engineers, healthcare",
                    "Lawyers and politicians",
                    "Athletes and musicians",
                ],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "What does the author say about changing careers?",
                "options": [
                    "It's a sign of failure",
                    "Many successful people do it",
                    "It should be avoided",
                    "Only young people should do it",
                ],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "According to the passage, what should be balanced with job prospects?",
                "options": ["Location", "Passion", "Age", "Family size"],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "The phrase 'work-life balance' in the text refers to:",
                "options": [
                    "Equal pay for equal work",
                    "Harmony between job and personal time",
                    "Working from home",
                    "Taking vacations",
                ],
                "correct": 1,
                "difficulty": "C",
            },
            {
                "text": "Why does the author mention vocational training?",
                "options": [
                    "It's better than university",
                    "It offers faster career entry",
                    "It's free of charge",
                    "It's mandatory in Kazakhstan",
                ],
                "correct": 1,
                "difficulty": "C",
            },
            {
                "text": "What key quality does the author recommend for the changing job market?",
                "options": ["Stubbornness", "Adaptability", "Wealth", "Connections"],
                "correct": 1,
                "difficulty": "C",
            },
        ],
    },
    # Text 3: Travel and Tourism in Kazakhstan (A2-B1 level)
    {
        "id": "reading_kazakhstan_tourism",
        "title": "Discovering Kazakhstan's Hidden Treasures",
        "level": "A2-B1",
        "topic": "reading",
        "passage": """DISCOVERING KAZAKHSTAN'S HIDDEN TREASURES

Kazakhstan, the world's ninth-largest country, offers incredible diversity for travelers. From the modern skyline of Nur-Sultan to the ancient Silk Road cities, there is something for every type of tourist.

Nature lovers are drawn to the stunning Charyn Canyon, often compared to the Grand Canyon in the United States. The colorful rock formations, shaped over millions of years, create a breathtaking landscape. Another natural wonder is Lake Kolsai, a series of three alpine lakes surrounded by Tien Shan spruce forests.

History enthusiasts can explore Turkestan, home to the magnificent Mausoleum of Khoja Ahmed Yasawi, a UNESCO World Heritage Site. This 14th-century structure showcases the architectural mastery of the Timurid era. The ancient city of Otrar, once a major trading hub on the Silk Road, reveals archaeological treasures from centuries past.

Adventure seekers find paradise in the Altai Mountains, perfect for hiking, horse riding, and winter sports. The vast steppes offer unique experiences like eagle hunting with the Kazakh nomads—a tradition preserved for thousands of years.

The hospitality industry in Kazakhstan has grown significantly. Modern hotels, traditional yurt camps, and homestay programs cater to different preferences and budgets. The national airline, Air Astana, connects major cities and international destinations.

Local cuisine adds to the travel experience. Beshbarmak, the national dish, and kumys, fermented mare's milk, give visitors a taste of nomadic traditions.""",
        "questions": [
            {
                "text": "What is Kazakhstan's world ranking by land area?",
                "options": ["Fifth", "Seventh", "Ninth", "Eleventh"],
                "correct": 2,
                "difficulty": "A",
            },
            {
                "text": "What natural formation is Charyn Canyon compared to?",
                "options": [
                    "Niagara Falls",
                    "Mount Everest",
                    "Grand Canyon",
                    "Amazon River",
                ],
                "correct": 2,
                "difficulty": "A",
            },
            {
                "text": "What UNESCO site is located in Turkestan?",
                "options": [
                    "Charyn Canyon",
                    "Lake Kolsai",
                    "Mausoleum of Khoja Ahmed Yasawi",
                    "Altai Mountains",
                ],
                "correct": 2,
                "difficulty": "B",
            },
            {
                "text": "What traditional activity can visitors experience with Kazakh nomads?",
                "options": ["Fishing", "Eagle hunting", "Pottery making", "Weaving"],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "What is beshbarmak?",
                "options": [
                    "A traditional dance",
                    "The national dish",
                    "A type of yurt",
                    "A musical instrument",
                ],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "According to the passage, what surrounds Lake Kolsai?",
                "options": [
                    "Desert sand",
                    "Modern buildings",
                    "Tien Shan spruce forests",
                    "Rice fields",
                ],
                "correct": 2,
                "difficulty": "C",
            },
            {
                "text": "What was Otrar's historical significance?",
                "options": [
                    "Capital city",
                    "Major Silk Road trading hub",
                    "Religious center",
                    "Military base",
                ],
                "correct": 1,
                "difficulty": "C",
            },
            {
                "text": "What accommodation types are mentioned for tourists?",
                "options": [
                    "Only luxury hotels",
                    "Hotels, yurt camps, homestays",
                    "Cruise ships",
                    "Tents only",
                ],
                "correct": 1,
                "difficulty": "C",
            },
        ],
    },
    # ============ ТАҚЫРЫП 2: БІЛІМ ЖӘНЕ ҒЫЛЫМ ============
    # Text 4: University Life (B1 level)
    {
        "id": "reading_university_life",
        "title": "Student Life at Modern Universities",
        "level": "B1",
        "topic": "reading",
        "passage": """STUDENT LIFE AT MODERN UNIVERSITIES

University education has transformed dramatically in recent years. Today's students have access to resources and opportunities that previous generations could only dream of. However, they also face unique challenges in an increasingly competitive academic environment.

The traditional lecture hall experience is being supplemented—and sometimes replaced—by online learning platforms. Students can now access course materials, participate in virtual discussions, and submit assignments from anywhere in the world. This flexibility benefits those who work part-time jobs or have family responsibilities.

Beyond academics, universities offer numerous opportunities for personal development. Student clubs and organizations cover everything from debate societies to volunteer groups. Many universities encourage international exchange programs, allowing students to spend a semester abroad and gain cross-cultural experiences.

Career preparation begins early in the university journey. Internship programs connect students with potential employers, providing valuable real-world experience. Career services offices help with resume writing, interview skills, and job placement. Networking events bring together students, alumni, and industry professionals.

Mental health support has become a priority on campuses worldwide. Universities now offer counseling services, stress management workshops, and wellness programs. Recognizing that academic pressure can affect well-being, institutions are creating more supportive environments.

Despite rising tuition costs in many countries, higher education remains a valuable investment. Graduates with bachelor's degrees typically earn significantly more over their lifetimes than those without. Scholarships, grants, and student loan programs help make university accessible to students from diverse economic backgrounds.""",
        "questions": [
            {
                "text": "What is replacing the traditional lecture hall experience?",
                "options": [
                    "Private tutoring",
                    "Online learning platforms",
                    "Textbook reading",
                    "Group projects only",
                ],
                "correct": 1,
                "difficulty": "A",
            },
            {
                "text": "What benefit does online learning provide according to the text?",
                "options": [
                    "Lower tuition",
                    "Flexibility for working students",
                    "Easier exams",
                    "Fewer assignments",
                ],
                "correct": 1,
                "difficulty": "A",
            },
            {
                "text": "What do internship programs help students gain?",
                "options": [
                    "Higher grades",
                    "Real-world experience",
                    "More free time",
                    "Weekend work",
                ],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "What has become a priority at universities regarding students?",
                "options": [
                    "Sports achievements",
                    "Mental health support",
                    "Political activities",
                    "Religious education",
                ],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "According to the passage, what do exchange programs offer?",
                "options": [
                    "Free tuition",
                    "Cross-cultural experiences",
                    "Guaranteed jobs",
                    "Language certificates",
                ],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "What helps make university accessible to diverse economic backgrounds?",
                "options": [
                    "Campus housing",
                    "Scholarships, grants, and loans",
                    "Part-time jobs",
                    "Family support",
                ],
                "correct": 1,
                "difficulty": "C",
            },
            {
                "text": "What does the text suggest about graduates with bachelor's degrees?",
                "options": [
                    "They work fewer hours",
                    "They earn significantly more over time",
                    "They are happier",
                    "They travel more",
                ],
                "correct": 1,
                "difficulty": "C",
            },
            {
                "text": "The word 'supplemented' in the context of lecture halls means:",
                "options": [
                    "Completely replaced",
                    "Added to or enhanced",
                    "Removed",
                    "Criticized",
                ],
                "correct": 1,
                "difficulty": "C",
            },
        ],
    },
    # Text 5: Famous Scientists (B1-B2 level)
    {
        "id": "reading_scientists",
        "title": "Pioneers of Science: Changing the World",
        "level": "B1-B2",
        "topic": "reading",
        "passage": """PIONEERS OF SCIENCE: CHANGING THE WORLD

Throughout history, brilliant minds have pushed the boundaries of human knowledge, forever changing how we understand and interact with our world. Their discoveries have improved lives, solved mysteries, and opened doors to new possibilities.

Marie Curie, born in Poland in 1867, became the first woman to win a Nobel Prize—and the only person to win Nobel Prizes in two different sciences: Physics and Chemistry. Her research on radioactivity laid the foundation for modern cancer treatment. Despite facing gender discrimination in academia, she persevered and became a role model for women in science.

Albert Einstein revolutionized physics with his theory of relativity, fundamentally changing our understanding of space, time, and energy. His famous equation, E=mc², demonstrated the relationship between mass and energy. Beyond his scientific work, Einstein was an advocate for peace and civil rights.

In the modern era, Stephen Hawking continued to inspire with his work on black holes and cosmology. Despite being diagnosed with ALS at 21 and given only a few years to live, he defied expectations and continued his research for over 50 years. His book "A Brief History of Time" made complex physics accessible to general readers.

Kazakhstan has also produced notable scientists. Kanysh Satpayev, a geologist, made significant contributions to the study of mineral resources and became the first president of the Academy of Sciences of Kazakhstan. Today, Kazakh researchers are making advances in areas from space technology to renewable energy.

The legacy of these pioneers reminds us that curiosity, perseverance, and courage can change the world.""",
        "questions": [
            {
                "text": "How many Nobel Prizes did Marie Curie win?",
                "options": ["One", "Two", "Three", "Four"],
                "correct": 1,
                "difficulty": "A",
            },
            {
                "text": "What is Marie Curie's research field famous for helping treat?",
                "options": ["Heart disease", "Cancer", "Diabetes", "Mental illness"],
                "correct": 1,
                "difficulty": "A",
            },
            {
                "text": "What does Einstein's equation E=mc² demonstrate?",
                "options": [
                    "Speed of light",
                    "Relationship between mass and energy",
                    "Gravity",
                    "Temperature",
                ],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "What condition was Stephen Hawking diagnosed with?",
                "options": ["Cancer", "Diabetes", "ALS", "Heart disease"],
                "correct": 2,
                "difficulty": "B",
            },
            {
                "text": "What was Kanysh Satpayev's scientific field?",
                "options": ["Physics", "Chemistry", "Geology", "Biology"],
                "correct": 2,
                "difficulty": "B",
            },
            {
                "text": "What book made complex physics accessible to general readers?",
                "options": [
                    "Theory of Relativity",
                    "A Brief History of Time",
                    "The Universe",
                    "Physics for Beginners",
                ],
                "correct": 1,
                "difficulty": "C",
            },
            {
                "text": "According to the passage, what challenges did Marie Curie face?",
                "options": [
                    "Financial problems",
                    "Gender discrimination",
                    "Health issues",
                    "Language barriers",
                ],
                "correct": 1,
                "difficulty": "C",
            },
            {
                "text": "What areas are mentioned as current focus of Kazakh researchers?",
                "options": [
                    "Fashion and art",
                    "Space technology and renewable energy",
                    "Agriculture only",
                    "Traditional medicine",
                ],
                "correct": 1,
                "difficulty": "C",
            },
        ],
    },
    # Text 6: Environmental Issues (B1-B2 level)
    {
        "id": "reading_environment",
        "title": "Environmental Challenges of Our Time",
        "level": "B1-B2",
        "topic": "reading",
        "passage": """ENVIRONMENTAL CHALLENGES OF OUR TIME

The natural environment faces unprecedented challenges in the 21st century. Climate change, pollution, and biodiversity loss threaten the delicate balance of ecosystems that support all life on Earth. Scientists and policymakers worldwide are working to address these issues before irreversible damage occurs.

Climate change is perhaps the most pressing environmental concern. Rising global temperatures are causing ice caps to melt, sea levels to rise, and weather patterns to become more extreme. The Intergovernmental Panel on Climate Change (IPCC) warns that immediate action is necessary to limit warming to 1.5 degrees Celsius above pre-industrial levels.

Central Asia, including Kazakhstan, faces unique environmental challenges. The shrinking of the Aral Sea, once one of the world's largest lakes, stands as a stark reminder of environmental degradation. Decades of water diversion for irrigation caused the sea to lose 90% of its volume. Efforts are now underway to restore at least the northern section.

Air pollution affects major cities worldwide. In densely populated urban areas, vehicle emissions, industrial activity, and power generation contribute to poor air quality. This has direct health consequences, causing respiratory diseases and reducing life expectancy in severely affected areas.

Solutions require both individual and collective action. Renewable energy sources like solar and wind power are becoming more affordable and widespread. Individuals can make a difference by reducing consumption, recycling, and choosing sustainable products. Governments are implementing policies to encourage green technologies and protect natural habitats.

Education plays a crucial role in environmental protection. When people understand the connections between their actions and environmental outcomes, they are more likely to make sustainable choices.""",
        "questions": [
            {
                "text": "What are the three main environmental challenges mentioned?",
                "options": [
                    "Poverty, disease, war",
                    "Climate change, pollution, biodiversity loss",
                    "Overpopulation, famine, drought",
                    "Deforestation only",
                ],
                "correct": 1,
                "difficulty": "A",
            },
            {
                "text": "What international body is mentioned regarding climate change?",
                "options": [
                    "United Nations",
                    "World Health Organization",
                    "IPCC",
                    "World Bank",
                ],
                "correct": 2,
                "difficulty": "A",
            },
            {
                "text": "What percentage of its volume did the Aral Sea lose?",
                "options": ["50%", "70%", "90%", "100%"],
                "correct": 2,
                "difficulty": "B",
            },
            {
                "text": "What are becoming more affordable according to the text?",
                "options": [
                    "Electric cars",
                    "Renewable energy sources",
                    "Organic food",
                    "Public transportation",
                ],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "What health consequences are linked to air pollution?",
                "options": [
                    "Obesity",
                    "Respiratory diseases",
                    "Vision problems",
                    "Skin conditions",
                ],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "Why did the Aral Sea shrink?",
                "options": [
                    "Climate change",
                    "Water diversion for irrigation",
                    "Industrial pollution",
                    "Natural evaporation",
                ],
                "correct": 1,
                "difficulty": "C",
            },
            {
                "text": "What temperature limit does the IPCC recommend?",
                "options": [
                    "1.5°C above pre-industrial levels",
                    "2.0°C",
                    "0.5°C",
                    "3.0°C",
                ],
                "correct": 0,
                "difficulty": "C",
            },
            {
                "text": "According to the passage, what role does education play?",
                "options": [
                    "No significant role",
                    "Crucial role in environmental protection",
                    "Only for scientists",
                    "Limited impact",
                ],
                "correct": 1,
                "difficulty": "C",
            },
        ],
    },
    # ============ ТАҚЫРЫП 3: ҚАЗАҚСТАН ЖӘНЕ АҒЫЛШЫН ТІЛДІ МЕМЛЕКЕТТЕР ============
    # Text 7: British Culture and Traditions (B1 level)
    {
        "id": "reading_british_culture",
        "title": "British Traditions and Cultural Heritage",
        "level": "B1",
        "topic": "reading",
        "passage": """BRITISH TRADITIONS AND CULTURAL HERITAGE

The United Kingdom has a rich cultural heritage that blends ancient traditions with modern life. From royal ceremonies to afternoon tea, British customs reflect centuries of history while continuing to evolve.

The British monarchy remains central to national identity. Royal events like coronations, weddings, and the annual Trooping the Colour ceremony draw millions of viewers worldwide. While the monarch's political power is limited, the royal family plays an important symbolic and diplomatic role representing the nation.

Tea culture is perhaps the most recognizable British tradition. The custom of afternoon tea began in the 1840s when the Duchess of Bedford requested a light snack between lunch and dinner. Today, the British consume over 60 billion cups of tea annually. Tea rooms offering scones, sandwiches, and cakes remain popular throughout the country.

Sports also form a significant part of British culture. Football, rugby, and cricket originated in Britain and spread globally through the British Empire. Wimbledon, the oldest tennis championship in the world, has been held since 1877. The passion for sports is evident in packed stadiums and enthusiastic pub gatherings during major matches.

Literature and theater contribute to Britain's cultural influence. Shakespeare's plays are performed worldwide over 400 years after they were written. The West End in London rivals Broadway as a center for theater arts. British authors from Jane Austen to J.K. Rowling have captivated readers across generations.

Modern Britain is multicultural, with immigrants from former colonies and other nations contributing to a diverse society. This diversity is reflected in cuisine, music, and arts, making contemporary British culture a unique blend of old and new.""",
        "questions": [
            {
                "text": "When did the tradition of afternoon tea begin?",
                "options": ["1740s", "1840s", "1940s", "1640s"],
                "correct": 1,
                "difficulty": "A",
            },
            {
                "text": "How many cups of tea do the British consume annually?",
                "options": ["30 billion", "60 billion", "90 billion", "120 billion"],
                "correct": 1,
                "difficulty": "A",
            },
            {
                "text": "Which sports originated in Britain according to the text?",
                "options": [
                    "Basketball and baseball",
                    "Football, rugby, and cricket",
                    "Tennis and golf only",
                    "Hockey and swimming",
                ],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "When did Wimbledon first take place?",
                "options": ["1857", "1867", "1877", "1887"],
                "correct": 2,
                "difficulty": "B",
            },
            {
                "text": "Who started the afternoon tea tradition?",
                "options": [
                    "Queen Victoria",
                    "Duchess of Bedford",
                    "King George",
                    "Princess Diana",
                ],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "What is the West End known for?",
                "options": ["Shopping", "Theater arts", "Sports venues", "Museums"],
                "correct": 1,
                "difficulty": "C",
            },
            {
                "text": "According to the passage, what role does the royal family play now?",
                "options": [
                    "Absolute political power",
                    "Symbolic and diplomatic role",
                    "No role at all",
                    "Military command",
                ],
                "correct": 1,
                "difficulty": "C",
            },
            {
                "text": "What makes contemporary British culture described as 'unique'?",
                "options": [
                    "Only traditional elements",
                    "Blend of old and new with diversity",
                    "Foreign influence only",
                    "Rejection of tradition",
                ],
                "correct": 1,
                "difficulty": "C",
            },
        ],
    },
    # Text 8: American Education System (B1-B2 level)
    {
        "id": "reading_american_education",
        "title": "The American Education System",
        "level": "B1-B2",
        "topic": "reading",
        "passage": """THE AMERICAN EDUCATION SYSTEM

The United States has one of the world's most diverse and decentralized education systems. Unlike many countries with national curricula, American education is primarily managed at the state and local levels, resulting in significant variation across regions.

Education in America is divided into several stages. Elementary school covers kindergarten through fifth or sixth grade (ages 5-11). Middle school, also called junior high, spans grades 6-8 (ages 11-14). High school encompasses grades 9-12 (ages 14-18). Students typically graduate around age 18 with a high school diploma.

Higher education in America is highly regarded globally. The country is home to many of the world's top-ranked universities, including Harvard, Stanford, and MIT. American universities attract students from every corner of the globe, contributing to a diverse campus environment. The flexibility of the American system allows students to explore various subjects before declaring a major.

Community colleges offer an affordable pathway to higher education. Students can complete two years of general education courses before transferring to four-year universities. This option is popular among students seeking to reduce costs or those who need additional academic preparation.

Extracurricular activities play a significant role in American schools. Sports teams, music programs, debate clubs, and volunteer organizations help develop students' skills outside the classroom. College admissions often consider these activities alongside academic performance.

Challenges remain in American education. Achievement gaps between different socioeconomic groups persist. School funding varies significantly between wealthy and poor districts. Despite these issues, the American system continues to produce innovators, researchers, and leaders in many fields.""",
        "questions": [
            {
                "text": "How is American education managed?",
                "options": [
                    "Centrally by federal government",
                    "At state and local levels",
                    "By private organizations only",
                    "By international bodies",
                ],
                "correct": 1,
                "difficulty": "A",
            },
            {
                "text": "At what age do American students typically graduate high school?",
                "options": ["16", "17", "18", "19"],
                "correct": 2,
                "difficulty": "A",
            },
            {
                "text": "What do community colleges offer?",
                "options": [
                    "Four-year degrees",
                    "Affordable pathway to higher education",
                    "Only vocational training",
                    "Graduate programs",
                ],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "What role do extracurricular activities play in American schools?",
                "options": [
                    "No role",
                    "Only for entertainment",
                    "Help develop skills and affect admissions",
                    "Mandatory for graduation",
                ],
                "correct": 2,
                "difficulty": "B",
            },
            {
                "text": "Which universities are mentioned as top-ranked?",
                "options": [
                    "Oxford, Cambridge",
                    "Harvard, Stanford, MIT",
                    "Yale, Princeton",
                    "Berkeley, UCLA",
                ],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "What flexibility does the American university system offer?",
                "options": [
                    "No homework required",
                    "Explore subjects before declaring major",
                    "Free tuition",
                    "Online-only options",
                ],
                "correct": 1,
                "difficulty": "C",
            },
            {
                "text": "What challenge is mentioned regarding education funding?",
                "options": [
                    "Too much funding overall",
                    "Variation between wealthy and poor districts",
                    "No government support",
                    "International interference",
                ],
                "correct": 1,
                "difficulty": "C",
            },
            {
                "text": "What grade levels does high school cover?",
                "options": ["6-8", "9-12", "7-10", "10-12"],
                "correct": 1,
                "difficulty": "C",
            },
        ],
    },
    # Text 9: Literature and Famous Authors (B2 level)
    {
        "id": "reading_literature",
        "title": "Great Authors Who Shaped Literature",
        "level": "B2",
        "topic": "reading",
        "passage": """GREAT AUTHORS WHO SHAPED LITERATURE

Literature has the power to transport readers across time and space, revealing universal truths about the human experience. Throughout history, certain authors have created works so profound that they continue to resonate centuries after being written.

William Shakespeare, often called the greatest writer in the English language, revolutionized drama and poetry in the 16th and 17th centuries. His 37 plays and 154 sonnets explore themes of love, jealousy, ambition, and mortality. Phrases from his works—"to be or not to be," "star-crossed lovers"—have become part of everyday English.

Jane Austen, writing in early 19th-century England, created novels that combined sharp social commentary with romantic plots. Works like "Pride and Prejudice" and "Emma" examined class, marriage, and women's limited options in Georgian society. Her wit and psychological insight continue to attract readers and inspire film adaptations.

Fyodor Dostoevsky, a Russian master, delved into the depths of human psychology. "Crime and Punishment" and "The Brothers Karamazov" explore moral dilemmas, religious faith, and the nature of evil. His influence extends beyond literature to philosophy and psychology.

The 20th century brought diverse voices to world literature. Gabriel García Márquez introduced magical realism through "One Hundred Years of Solitude," blending fantastical elements with Latin American history. Toni Morrison, the first African American woman to win the Nobel Prize in Literature, explored the African American experience with poetic power in novels like "Beloved."

Literature continues to evolve, with new voices emerging from around the world. Kazakh literature, from Abai Kunanbayev's poetry to modern novelists, contributes unique perspectives to the global literary conversation.""",
        "questions": [
            {
                "text": "How many plays did Shakespeare write?",
                "options": ["27", "37", "47", "57"],
                "correct": 1,
                "difficulty": "A",
            },
            {
                "text": "Which author is described as the greatest writer in English?",
                "options": ["Jane Austen", "Dostoevsky", "Shakespeare", "Morrison"],
                "correct": 2,
                "difficulty": "A",
            },
            {
                "text": "What themes did Jane Austen explore in her novels?",
                "options": [
                    "War and politics",
                    "Class, marriage, women's options",
                    "Science fiction",
                    "Adventure and travel",
                ],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "What literary style is Gabriel García Márquez known for?",
                "options": ["Realism", "Magical realism", "Gothic horror", "Satire"],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "Who was the first African American woman to win the Nobel Prize in Literature?",
                "options": [
                    "Jane Austen",
                    "Maya Angelou",
                    "Toni Morrison",
                    "Alice Walker",
                ],
                "correct": 2,
                "difficulty": "B",
            },
            {
                "text": "What did Dostoevsky's works explore?",
                "options": [
                    "Nature and landscapes",
                    "Moral dilemmas and psychology",
                    "Comedy and humor",
                    "Science and technology",
                ],
                "correct": 1,
                "difficulty": "C",
            },
            {
                "text": "Which Kazakh poet is mentioned in the passage?",
                "options": [
                    "Mukhtar Auezov",
                    "Abai Kunanbayev",
                    "Olzhas Suleimenov",
                    "Zhambyl Zhabayev",
                ],
                "correct": 1,
                "difficulty": "C",
            },
            {
                "text": "The phrase 'star-crossed lovers' comes from which author?",
                "options": [
                    "Jane Austen",
                    "Gabriel García Márquez",
                    "Shakespeare",
                    "Dostoevsky",
                ],
                "correct": 2,
                "difficulty": "C",
            },
        ],
    },
    # Text 10: Healthy Lifestyle (A2 level)
    {
        "id": "reading_healthy_lifestyle",
        "title": "Building a Healthy Lifestyle",
        "level": "A2",
        "topic": "reading",
        "passage": """BUILDING A HEALTHY LIFESTYLE

Living a healthy life is more than just avoiding illness. It means taking care of your body and mind every day through good habits and positive choices. Experts recommend focusing on several key areas to achieve overall well-being.

Regular physical activity is essential for good health. The World Health Organization recommends at least 150 minutes of moderate exercise per week for adults. This can include walking, cycling, swimming, or playing sports. Exercise strengthens the heart, improves mood, and helps maintain a healthy weight.

Nutrition plays an equally important role. A balanced diet should include plenty of fruits, vegetables, whole grains, and lean proteins. Limiting sugar, salt, and processed foods can reduce the risk of many diseases. Drinking enough water—about 2 liters per day—keeps the body hydrated and functioning properly.

Sleep is often overlooked but crucial for health. Adults need 7-9 hours of quality sleep each night. Good sleep habits include keeping a regular schedule, avoiding screens before bed, and creating a comfortable sleeping environment. Poor sleep can affect mood, concentration, and immune function.

Mental health deserves as much attention as physical health. Managing stress through relaxation techniques, hobbies, and social connections supports emotional well-being. If feelings of anxiety or depression persist, seeking professional help is important.

Breaking bad habits like smoking and excessive alcohol consumption significantly improves health outcomes. While changing habits can be difficult, the long-term benefits are worth the effort. Small, consistent changes over time lead to lasting improvements in health and quality of life.""",
        "questions": [
            {
                "text": "How many minutes of exercise per week does WHO recommend?",
                "options": ["100 minutes", "150 minutes", "200 minutes", "250 minutes"],
                "correct": 1,
                "difficulty": "A",
            },
            {
                "text": "How much water should you drink daily according to the text?",
                "options": ["1 liter", "2 liters", "3 liters", "4 liters"],
                "correct": 1,
                "difficulty": "A",
            },
            {
                "text": "How many hours of sleep do adults need?",
                "options": ["5-6 hours", "6-7 hours", "7-9 hours", "10-12 hours"],
                "correct": 2,
                "difficulty": "B",
            },
            {
                "text": "What should be limited in a healthy diet?",
                "options": [
                    "Vegetables",
                    "Water",
                    "Sugar, salt, processed foods",
                    "Fruits",
                ],
                "correct": 2,
                "difficulty": "B",
            },
            {
                "text": "What can help manage stress according to the passage?",
                "options": [
                    "Working longer hours",
                    "Relaxation techniques and hobbies",
                    "Avoiding social contact",
                    "Eating more food",
                ],
                "correct": 1,
                "difficulty": "B",
            },
            {
                "text": "What should you avoid before bed for good sleep?",
                "options": ["Reading books", "Drinking water", "Screens", "Relaxation"],
                "correct": 2,
                "difficulty": "C",
            },
            {
                "text": "What type of changes does the text recommend for improving health?",
                "options": [
                    "Dramatic sudden changes",
                    "Small, consistent changes over time",
                    "No changes needed",
                    "Only medical intervention",
                ],
                "correct": 1,
                "difficulty": "C",
            },
            {
                "text": "According to the passage, what can poor sleep affect?",
                "options": [
                    "Only physical health",
                    "Mood, concentration, immune function",
                    "Appetite only",
                    "Nothing significant",
                ],
                "correct": 1,
                "difficulty": "C",
            },
        ],
    },
]
