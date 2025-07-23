# News2TG

A modular, production-ready news parsing, summarization, and delivery platform using FastAPI, Celery, LangChain, Gemini, ChromaDB, PostgreSQL, Redis, NiceGUI, and Telegram.

## Features
- Parse news from RSS feeds or APIs (LangChain, LlamaIndex, Google PSE)
- Summarize and classify news with Gemini via LangChain
- Index news in ChromaDB vector store
- FastAPI backend and NiceGUI admin panel
- PostgreSQL for persistent storage
- Celery + Redis for background/scheduled tasks
- Telegram delivery with Jinja2 templating
- Redis caching for LLM/API calls
- Docker Compose deployment

## Getting Started

### Prerequisites
- Docker & Docker Compose
- Python 3.11+ (for local development)

### Quick Start (Docker Compose)
1. Clone the repo:
   ```bash
   git clone https://github.com/Stihotvor/news2tg.git
   cd news2tg/news2tg/newsbot
   ```
2. Fill in `.env` with your secrets (see `.env` template).
3. Build and start all services:
   ```bash
   docker compose up --build
   ```
4. Run Alembic migrations:
   ```bash
   docker compose run --rm backend alembic -c backend/migrations/alembic.ini upgrade head
   ```
5. Visit:
   - FastAPI: http://localhost:8000
   - NiceGUI: http://localhost:8081 (if mapped)
   - Adminer: http://localhost:8080

### Local Development
- Install dependencies: `pip install -r requirements.txt`
- Run backend: `uvicorn backend.main:app --reload`
- Run frontend: `python frontend/main.py`
- Start Celery: `celery -A backend.celery_worker worker --loglevel=info`
- Start Celery Beat: `celery -A backend.celery_worker beat --loglevel=info`

### Testing
- Run all tests: `pytest tests/`
- Run with coverage: `pytest --cov=backend --cov=frontend tests/`
- Async tests are supported (see pytest-asyncio)
- Use `pytest-mock` for mocking

## Contributing
- Fork the repo and create a feature branch
- Add/modify code and tests
- Submit a pull request with a clear description

## Reporting Bugs
- Open an issue on GitHub with steps to reproduce, expected/actual behavior, and logs if possible.

## Project Structure
- `backend/` - FastAPI, Celery, services, DB, cache, templates
- `frontend/` - NiceGUI admin panel
- `docker-compose.yml` - Multi-service orchestration
- `requirements.txt` - Python dependencies
- `tests/` - Unit tests

---
MIT License
