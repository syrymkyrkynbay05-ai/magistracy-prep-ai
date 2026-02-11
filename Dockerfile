# 1. Build Frontend
FROM node:20-slim AS frontend-builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# 2. Run Backend
FROM python:3.11-slim
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy backend requirements and install
COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy all project files
COPY . .

# Copy built frontend from stage 1
COPY --from=frontend-builder /app/dist ./dist

# Set environment variables
ENV PYTHONPATH=/app/backend
ENV PORT=8000

# Initialize DB and start
CMD ["sh", "-c", "python3 backend/seed_db.py && python3 backend/main.py"]
