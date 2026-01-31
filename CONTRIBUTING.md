# Үлес қосу нұсқаулығы

Жобаға үлес қосқыңыз келсе, бұл нұсқаулықты оқыңыз! 🎉

---

## 🚀 Қалай бастау керек

### 1. Fork жасаңыз

GitHub-та репозиторийдің "Fork" батырмасын басыңыз.

### 2. Клондаңыз

```bash
git clone https://github.com/Azamaperdeev05/magistracy-prep-ai.git
cd magistracy-prep-ai
```

### 3. Орнатыңыз

```bash
# Frontend
npm install

# Backend
cd backend
pip install -r requirements.txt
python seed_db.py
```

### 4. Branch жасаңыз

```bash
git checkout -b feature/amazing-feature
```

---

## 📝 Commit хабарламалары

Біз [Conventional Commits](https://www.conventionalcommits.org/) стандартын қолданамыз:

```
<type>(<scope>): <description>
```

### Types:
- `feat`: Жаңа функция
- `fix`: Қате түзету
- `docs`: Құжаттама
- `style`: Форматтау (код өзгермейді)
- `refactor`: Рефакторинг
- `test`: Тесттер
- `chore`: Техникалық жұмыс

### Мысалдар:

```bash
git commit -m "feat(questions): add 50 new English questions"
git commit -m "fix(test): resolve timer not stopping issue"
git commit -m "docs(readme): update installation guide"
```

---

## 🔍 Pull Request

### PR ашу алдында:

1. Код жұмыс істейтінін тексеріңіз:
   ```bash
   npm run dev      # Frontend
   python main.py   # Backend
   ```

2. Lint қателерін тексеріңіз:
   ```bash
   npm run lint
   ```

3. Сипаттама жазыңыз:
   - Не өзгертілді?
   - Неге өзгертілді?
   - Қалай тестілеу керек?

---

## 💡 Үлес қосу идеялары

### Сұрақтар қосу

`backend/seed_db.py` файлына жаңа сұрақтар қосуға болады:

```python
{
    "text": "Сұрақ мәтіні?",
    "options": ["A", "B", "C", "D"],
    "correct_indices": [0],  # Дұрыс жауап индексі
    "topic": "Тақырып атауы",
}
```

### Жаңа функциялар

- Dark mode
- Таймер
- Leaderboard
- Статистика dashboard
- Mobile app (React Native)

### Құжаттама

- README аудармалары (EN, RU)
- Video tutorials
- API мысалдары

---

## 🐛 Қате таптыңыз ба?

1. [Issues](https://github.com/yourusername/magistracy-prep-ai/issues) бөлімін тексеріңіз
2. Жаңа Issue ашыңыз:
   - Қате сипаттамасы
   - Қайталау қадамдары
   - Күтілген нәтиже
   - Нақты нәтиже
   - Скриншоттар

---

## 📞 Байланыс

Сұрақтарыңыз болса:
- Issue ашыңыз
- Email: azamat@example.com

---

Рахмет! 🙏
