# Backend

This directory contains the FastAPI backend, Celery workers, database models, cache, and all core business logic for News2TG.

## Structure
- `main.py`: FastAPI entrypoint
- `api/`: API route definitions
- `services/`: Business logic (parsing, summarization, indexing, telegram, etc.)
- `templates/`: Jinja2 templates for message formatting
- `celery_worker.py`: Celery worker entrypoint
- `celery_beat.py`: Celery beat scheduler
- `db/`: SQLAlchemy models and session
- `migrations/`: Alembic migrations
- `cache/`: Redis caching utilities

## How to Use
- Run FastAPI: `uvicorn backend.main:app --reload`
- Start Celery: `celery -A backend.celery_worker worker --loglevel=info`
- Start Celery Beat: `celery -A backend.celery_worker beat --loglevel=info`
- Run migrations: `alembic -c backend/migrations/alembic.ini upgrade head`

---
Edit or add new services in `services/` as needed.
