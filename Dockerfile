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

# Default port
ENV PORT=8000

# Direct CMD with shell - no script file needed
CMD sh -c "echo '� Starting uvicorn on port:' $PORT && uvicorn backend.main:app --host 0.0.0.0 --port $PORT"
