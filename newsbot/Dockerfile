# Dockerfile for NewsBot Backend
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install pytest and extensions for testing
RUN pip install --no-cache-dir pytest pytest-cov pytest-asyncio pytest-mock

COPY . .

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
