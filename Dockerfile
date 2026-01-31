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

# Create startup script with SH (not bash!)
RUN printf '#!/bin/sh\n\
echo "🚀 [STARTUP] Container started"\n\
echo "📍 [STARTUP] PORT=$PORT"\n\
echo "📍 [STARTUP] Python: $(python --version)"\n\
ls -la /app/backend/ || echo "backend folder missing"\n\
echo "🔥 [STARTUP] Starting uvicorn..."\n\
exec uvicorn backend.main:app --host 0.0.0.0 --port $PORT\n\
' > /app/start.sh && chmod +x /app/start.sh

# Use SH to run the startup script
CMD ["/bin/sh", "/app/start.sh"]
