# 🎓 MagisCore (КТ Симулятор)

<div align="center">

<img src="public/logo no bg, white.svg" alt="MagisCore Logo" width="120">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![React](https://img.shields.io/badge/React-19.2-61DAFB?logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi)
![TypeScript](https://img.shields.io/badge/TypeScript-5.8-3178C6?logo=typescript)

**Қазақстан магистратурасына түсуге дайындалуға арналған MagisCore интерактивті тест платформасы**

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
- **4 пән бойынша 800 сапалы сұрақ**:
  - 🌐 Шет тілі (Ағылшын) - 418 сұрақ (Listening аудио)
  - 🧠 Оқу дайындығын анықтау (ОДАТ) - 100 сұрақ
  - 💻 Алгоритмдер және деректер құрылымы - 142 сұрақ
  - 🗄️ Дерекқорлар (SQL) - 140 сұрақ

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

**Бірден іске қосу (Backend + Frontend):**
```bash
python start.py
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
│   ├── AuthScreen.tsx       # Авторизация (Login/Register/OTP)
│   ├── WelcomeScreen.tsx    # Басты бет (MagisCore бренді)
│   ├── TestScreen.tsx       # Тест тапсыру процесі
│   ├── HistoryScreen.tsx    # Тест нәтижелерінің тарихы
│   ├── ResultScreen.tsx     # Нәтижелерді талдау және сақтау
│   └── SyllabusScreen.tsx   # Пәндер бағдарламасы
│
├── 📂 resources/            # Ресурстар мен оқу материалдары
│   ├── 📂 Markdown/         # Пәндердің MD силлабустары
│   └── 📂 shettili/         # Ағылшын тілі материалдары
│
├── 📂 docs/                 # Жүйелік құжаттама
│   ├── PROJECT_STATS.md     # Жоба статистикасы
│   ├── DATABASE.md          # Деректер базасының схемасы
│   ├── SYSTEM_LOGIC.md      # Жүйе архитектурасы мен логикасы
│   └── PROJECT_STRUCTURE.md # Папкалар иерархиясы
│
├── App.tsx                  # Негізгі React компоненті
├── start.py                 # Жобаны іске қосу скрипті
├── types.ts                 # TypeScript типтері
├── constants.ts             # Глобалды константалар
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
