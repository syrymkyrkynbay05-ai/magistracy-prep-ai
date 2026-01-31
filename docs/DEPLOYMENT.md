# 🚀 Railway Деплой Нұсқаулығы

Бұл құжатта жобаны Railway платформасына деплой жасау қадамдары сипатталған.

---

## 📋 Дайындық

### 1. GitHub-қа жүктеу

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/Azamaperdeev05/magistracy-prep-ai.git
git push -u origin main
```

---

## 🔧 Railway-да орнату

### 1-қадам: Railway-ға кіру

1. [Railway.app](https://railway.app) сайтына өтіңіз
2. GitHub аккаунтыңызбен кіріңіз
3. "New Project" батырмасын басыңыз

---

### 2-қадам: Backend сервисін жасау

1. **"Deploy from GitHub repo"** таңдаңыз
2. `magistracy-prep-ai` репозиторийін таңдаңыз
3. **Root Directory** өрісіне `backend` жазыңыз
4. **Settings** бөлімінде:
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Watch Paths**: `backend/**`

5. **Variables** бөлімінде қосыңыз:
   ```
   PORT=8000
   ```

6. **Deploy** батырмасын басыңыз

7. Сервис іске қосылғаннан кейін **Settings → Domains** бөлімінен URL алыңыз  
   Мысалы: `https://magistracy-prep-ai-backend.up.railway.app`

---

### 3-қадам: Frontend сервисін жасау

1. Жобаға жаңа сервис қосыңыз: **"+ New"** → **"GitHub Repo"**
2. Сол репозиторийді таңдаңыз
3. **Root Directory** бос қалдырыңыз (түбір)
4. **Settings** бөлімінде:
   - **Build Command**: `npm run build`
   - **Start Command**: `npx serve dist -s -l $PORT`

5. **Variables** бөлімінде қосыңыз:
   ```
   VITE_API_URL=https://your-backend-url.up.railway.app
   ```

6. **Deploy** батырмасын басыңыз

---

## ⚙️ Конфигурация файлдары

### `railway.toml` (Backend)

```toml
[build]
builder = "NIXPACKS"

[deploy]
startCommand = "cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT"
restartPolicyType = "ON_FAILURE"
restartPolicyMaxRetries = 10
```

### `nixpacks.toml` (Backend)

```toml
[phases.setup]
nixPkgs = ["python311", "python311Packages.pip"]

[phases.install]
cmds = ["cd backend && pip install -r requirements.txt"]

[start]
cmd = "cd backend && python seed_db.py && uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"
```

---

## 🔗 API URL-ін жаңарту

Frontend-те API URL-ін жаңарту үшін `services/apiService.ts` файлын өзгертіңіз:

```typescript
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const generateQuestionsForSubject = async (
  subjectId: SubjectId, 
  count: number = 5 
): Promise<Question[]> => {
  const response = await fetch(`${API_BASE_URL}/generate`, {
    // ...
  });
};
```

---

## 🐛 Жиі кездесетін мәселелер

### 1. "Module not found" қатесі

**Шешім:** `requirements.txt` файлында барлық dependencies бар екенін тексеріңіз.

### 2. CORS қатесі

**Шешім:** `backend/main.py` файлында CORS middleware дұрыс орнатылғанын тексеріңіз:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Production-да нақты URL қойыңыз
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 3. Database қатесі

**Шешім:** `seed_db.py` іске қосылғанын тексеріңіз. Start command-қа қосыңыз:

```bash
python seed_db.py && uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

## 📊 Мониторинг

Railway-да:
1. **Observability** бөлімінен логтарды көріңіз
2. **Metrics** бөлімінен CPU/Memory қолданылуын тексеріңіз
3. **Deployments** бөлімінен деплой тарихын көріңіз

---

## 🔄 Автоматты деплой

GitHub-қа push жасаған сайын Railway автоматты түрде қайта деплой жасайды.

Өшіру үшін:
1. **Settings** → **Deploys**
2. **Auto Deploy** → **Off**

---

## ✅ Тексеру

Деплой сәтті болса:

1. Backend: `https://your-backend-url.up.railway.app/` → `{"message": "Magistracy Prep AI API is running with SQLite"}`
2. Frontend: `https://your-frontend-url.up.railway.app/` → Басты бет көрінуі керек

---

**Сәтті деплой! 🎉**
