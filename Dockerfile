FROM python:3.11-slim

WORKDIR /app

# Install Node.js for frontend build
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy backend requirements and install
COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy frontend package files and install
COPY package*.json ./
RUN npm install

# Copy all source code
COPY . .

# Build frontend
RUN npm run build

# Initialize database at build time
RUN cd backend && python seed_db.py

# Default port (Railway will override with $PORT)
ENV PORT=8000

# Create startup script with logging
RUN echo '#!/bin/bash\n\
echo "🚀 [STARTUP] Container started at $(date)"\n\
echo "📍 [STARTUP] PORT=$PORT"\n\
echo "📍 [STARTUP] Working directory: $(pwd)"\n\
echo "📍 [STARTUP] Python version: $(python --version)"\n\
echo "📍 [STARTUP] Files in /app/backend:"\n\
ls -la /app/backend/\n\
echo "📍 [STARTUP] Checking if main.py exists..."\n\
if [ -f "/app/backend/main.py" ]; then\n\
    echo "✅ [STARTUP] main.py found"\n\
else\n\
    echo "❌ [STARTUP] main.py NOT FOUND"\n\
fi\n\
echo "🔥 [STARTUP] Starting uvicorn on port $PORT..."\n\
exec uvicorn backend.main:app --host 0.0.0.0 --port $PORT\n\
' > /app/start.sh && chmod +x /app/start.sh

# Use the startup script
CMD ["/bin/bash", "/app/start.sh"]
