# 📡 API Құжаттамасы

Бұл құжатта Magistracy Prep AI backend API сипатталған.

---

## 🔗 Base URL

- **Development:** `http://localhost:8000`
- **Production:** `https://your-backend-url.up.railway.app`

---

## 📖 Endpoints

### 1. Health Check

```
GET /
```

**Response:**
```json
{
  "message": "Magistracy Prep AI API is running with SQLite"
}
```

---

### 2. Сұрақтар генерациялау

```
POST /generate
```

**Request Body:**
```json
{
  "subject_id": "english",  // english, tgo, algo, db
  "count": 10               // сұрақ саны
}
```

**Response:**
```json
[
  {
    "id": "q-english-001",
    "subjectId": "english",
    "text": "Choose the correct form of the verb...",
    "codeSnippet": null,
    "options": [
      { "id": "opt-1", "text": "was" },
      { "id": "opt-2", "text": "were" },
      { "id": "opt-3", "text": "is" },
      { "id": "opt-4", "text": "are" }
    ],
    "correctOptionIds": ["opt-2"],
    "type": "SINGLE",
    "topic": "Grammar",
    "difficulty": "easy",
    "hint": "Subject-verb agreement rule applies here."
  }
]
```

---

### 3. Оқу бағдарламасын алу

```
GET /syllabus/{subject_id}
```

**Parameters:**
- `subject_id`: `english`, `tgo`, `algo`, `db`, `info`

**Response:**
```json
{
  "content": "# Ағылшын тілі\n\n## Grammar\n- Tenses\n- Articles\n..."
}
```

---

### 4. Нәтижелерді есептеу

```
POST /calculate
```

**Request Body:**
```json
{
  "questions": [...],  // Question[] массиві
  "answers": {
    "q-1": ["opt-2"],
    "q-2": ["opt-1", "opt-3"]
  }
}
```

**Response:**
```json
{
  "totalScore": 85,
  "maxScore": 100,
  "subjectScores": {
    "english": { "score": 45, "max": 50 },
    "tgo": { "score": 25, "max": 30 },
    "algo": { "score": 10, "max": 15 },
    "db": { "score": 5, "max": 5 }
  },
  "correctCount": 85,
  "totalQuestions": 100
}
```

---

## 📊 Деректер модельдері

### SubjectId (enum)
```
english | tgo | algo | db
```

### QuestionType (enum)
```
SINGLE | MULTIPLE
```

### Difficulty (enum)
```
easy | medium | hard
```

### Question
```typescript
interface Question {
  id: string;
  subjectId: SubjectId;
  text: string;
  codeSnippet?: string;
  options: Option[];
  correctOptionIds: string[];
  type: QuestionType;
  topic: string;
  difficulty?: Difficulty;
  hint?: string;
}
```

### Option
```typescript
interface Option {
  id: string;
  text: string;
}
```

---

## 🔒 CORS

API барлық origin-дерге рұқсат берілген (development үшін):

```python
allow_origins=["*"]
```

Production үшін нақты домендерді көрсетіңіз:

```python
allow_origins=["https://your-frontend-url.up.railway.app"]
```

---

## 🧪 API тестілеу

### cURL арқылы:

```bash
# Health check
curl http://localhost:8000/

# Сұрақтар алу
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"subject_id": "english", "count": 5}'

# Бағдарлама алу
curl http://localhost:8000/syllabus/algo
```

### Python арқылы:

```python
import requests

# Сұрақтар алу
response = requests.post(
    "http://localhost:8000/generate",
    json={"subject_id": "english", "count": 5}
)
questions = response.json()
print(questions)
```

---

## 📈 Rate Limiting

Қазіргі уақытта rate limiting жоқ. Production-да қосу ұсынылады.

---

## 🐛 Қате кодтары

| Код | Сипаттама |
|-----|-----------|
| 200 | Сәтті |
| 404 | Ресурс табылмады |
| 422 | Валидация қатесі |
| 500 | Сервер қатесі |

---

## 📝 Swagger UI

Интерактивті API құжаттамасы:

```
http://localhost:8000/docs
```

ReDoc:

```
http://localhost:8000/redoc
```
