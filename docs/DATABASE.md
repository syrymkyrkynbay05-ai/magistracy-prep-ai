# Деректер базасының құрылымы (Database Schema)

MagisCore деректерді сақтау үшін **SQLite** базасын қолданады.
 SQLAlchemy ORM арқылы басқарылады.

## 🗄 Кестелер (Tables)

### 1. `users` (Пайдаланушылар)
Пайдаланушы мәліметтері мен қауіпсіздік ақпараты.
- `id` (Integer): Бастапқы кілт.
- `email` (String): Пайдаланушының поштасы (unique).
- `full_name` (String): Аты-жөні.
- `hashed_password` (String): PBKDF2-SHA256 арқылы шифрланған пароль.
- `otp_code` (String): Парольді қалпына келтіруге арналған код.
- `otp_expires_at` (DateTime): Кодтың жарамдылық уақыты.
- `created_at` (DateTime): Тіркелген уақыты.

### 2. `questions` (Сұрақтар)
Тест сұрақтарының негізгі қоймасы.
- `id` (String): Сұрақ коды.
- `subject_id` (String): Пән коды (english, tgo, algo, db).
- `text` (Text): Сұрақ мәтіні.
- `type` (Enum): Сұрақ түрі (single, multiple).
- `topic` (String): Тақырыбы (мысалы: listening, grammar).
- `difficulty` (String): Қиындық деңгейі.
- `hint` (Text): Түсіндірме/Көмекші мәтін.
- `reading_passage` (Text): Оқылым мәтіні немесе Аудио сілтемесі (`AUDIO:...`).

### 3. `options` (Жауап нұсқалары)
Әр сұрақтың жауап нұсқалары.
- `id` (String): Жауап идентификаторы.
- `question_id` (ForeignKey): Сұраққа сілтеме.
- `text` (Text): Жауап мәтіні.

### 4. `test_results` (Тест нәтижелері)
Пайдаланушылардың прогресін сақтау.
- `id` (Integer): Бастапқы кілт.
- `user_id` (ForeignKey): Пайдаланушыға сілтеме.
- `total_score` (Integer): Жалпы жиналған ұпай.
- `max_score` (Integer): Мүмкін болған ең жоғары ұпай.
- `subject_scores` (JSON): Пәндер бойынша бөлінген ұпайлар.
- `correct_count` (Integer): Дұрыс жауаптар саны.
- `total_questions` (Integer): Тесттегі сұрақтар саны.
- `created_at` (DateTime): Тест аяқталған уақыт.

## 🔗 Байланыстар (Relationships)
- **User -> TestResults:** 1-ге көп (Бір пайдаланушыда көп нәтиже).
- **Question -> Options:** 1-ге көп (Бір сұрақта көп жауап).
