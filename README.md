# 🎓 Магистратураға Дайындық (КТ Симулятор)

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![React](https://img.shields.io/badge/React-19.2-61DAFB?logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi)
![TypeScript](https://img.shields.io/badge/TypeScript-5.8-3178C6?logo=typescript)

**Қазақстан магистратурасына түсуге дайындалуға арналған интерактивті тест платформасы**

[Demo](#demo) • [Мүмкіндіктер](#-мүмкіндіктер) • [Орнату](#-орнату) • [Деплой](#-деплой)

</div>

---

## 📸 Demo

<div align="center">
  <img src="docs/screenshots/welcome.png" alt="Басты бет" width="45%">
  <img src="docs/screenshots/test.png" alt="Тест беті" width="45%">
</div>

---

## ✨ Мүмкіндіктер

### 📚 Толық КТ Симуляциясы
- **4 пән бойынша 500+ сұрақ**:
  - 🌐 Шет тілі (Ағылшын) - 50 сұрақ
  - 🧠 Оқу дайындығын анықтау (ОДАТ) - 30 сұрақ
  - 💻 Алгоритмдер және деректер құрылымы - 30 сұрақ
  - 🗄️ Дерекқорлар (SQL) - 20 сұрақ

### 🛡️ Анти-чит жүйесі
- Мәтінді көшіруді бұғаттау (Ctrl+C)
- Оң жақ батырманы өшіру
- Браузер аудармашысын болдырмау
- Бетті жаңартудан қорғау

### 📊 Кеңейтілген аналитика
- Тақырып бойынша әлсіз жақтарды анықтау
- Деңгейлер бойынша сұрыптау (оңай → қиын)
- Толық нәтиже талдауы

### 🎓 Сертификат
- 60%+ нәтижеге сертификат жүктеу мүмкіндігі
- Аты-жөні және нәтижесі көрсетіледі

### 📖 Оқу бағдарламасы
- Әр пәннің толық силлабусы
- Markdown форматында құжаттама

---

## 🛠️ Технологиялар

### Frontend
| Технология | Сипаттама |
|------------|-----------|
| React 19 | UI кітапханасы |
| TypeScript | Типтелген JavaScript |
| Vite | Құрастыру құралы |
| TailwindCSS | Стиль кітапханасы |
| React Router | Маршрутизация |
| Lucide React | Иконкалар |

### Backend
| Технология | Сипаттама |
|------------|-----------|
| FastAPI | Python веб-фреймворк |
| SQLAlchemy | ORM |
| SQLite | Дерекқор |
| Uvicorn | ASGI сервер |

---

## 🚀 Орнату

### Қажеттіліктер
- Node.js 18+
- Python 3.10+
- npm немесе yarn

### 1. Репозиторийді клондау
```bash
git clone https://github.com/yourusername/magistracy-prep-ai.git
cd magistracy-prep-ai
```

### 2. Frontend орнату
```bash
npm install
```

### 3. Backend орнату
```bash
cd backend
pip install -r requirements.txt
```

### 4. Дерекқорды толтыру
```bash
cd backend
python seed_db.py
```

### 5. Іске қосу

**Backend (1-ші терминал):**
```bash
cd backend
python main.py
```

**Frontend (2-ші терминал):**
```bash
npm run dev
```

Сайт: http://localhost:3000

---

## 🌐 Деплой

### Railway-ға деплой

1. [Railway](https://railway.app) сайтына кіріңіз
2. "New Project" → "Deploy from GitHub repo" таңдаңыз
3. Репозиторийді таңдаңыз
4. Екі сервис жасаңыз:
   - **Backend**: `backend` папкасынан
   - **Frontend**: түбірден

Толық нұсқаулық: [DEPLOYMENT.md](./docs/DEPLOYMENT.md)

---

## 📁 Жоба құрылымы

```
magistracy-prep-ai/
├── 📂 backend/              # FastAPI backend
│   ├── main.py              # API endpoints
│   ├── models.py            # SQLAlchemy & Pydantic models
│   ├── database.py          # DB connection
│   ├── seed_db.py           # Сұрақтар базасы
│   └── requirements.txt     # Python dependencies
│
├── 📂 components/           # React компоненттері
│   ├── WelcomeScreen.tsx    # Басты бет
│   ├── TestScreen.tsx       # Тест беті
│   ├── ResultScreen.tsx     # Нәтижелер
│   ├── SyllabusScreen.tsx   # Бағдарлама
│   └── modals/              # Модалдар
│
├── 📂 Markdown/             # Оқу материалдары
│   ├── Ағылшын.md
│   ├── ОДАТ.md
│   ├── Алгоритмдер.md
│   └── Дерекқорлар.md
│
├── 📂 docs/                 # Құжаттама
│   ├── DEPLOYMENT.md
│   └── API.md
│
├── App.tsx                  # Main React component
├── types.ts                 # TypeScript типтері
├── constants.ts             # Константалар
└── index.html               # HTML entry point
```

---

## 🤝 Үлес қосу

1. Fork жасаңыз
2. Feature branch жасаңыз (`git checkout -b feature/amazing-feature`)
3. Commit жасаңыз (`git commit -m 'Add amazing feature'`)
4. Push жасаңыз (`git push origin feature/amazing-feature`)
5. Pull Request ашыңыз

---

## 📄 Лицензия

MIT лицензиясы бойынша таратылады. Толығырақ [LICENSE](LICENSE) файлында.

---

## 👨‍💻 Автор

**Пердеев Азамат**

- GitHub: [@Azamaperdeev05](https://github.com/Azamaperdeev05)

---

<div align="center">

**⭐ Егер жоба ұнаса, жұлдызша қойыңыз!**

</div>
