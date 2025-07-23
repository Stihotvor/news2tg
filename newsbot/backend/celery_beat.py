# Celery beat entrypoint
from backend.celery_worker import celery_app
from celery.schedules import crontab

# Example periodic task: fetch_news every 15 minutes
celery_app.conf.beat_schedule = {
    'fetch-news-every-15-minutes': {
        'task': 'backend.celery_worker.dummy_task',  # Replace with actual fetch_news task later
        'schedule': crontab(minute='*/15'),
        'args': (1, 2),  # Example args for dummy_task
    },
}

if __name__ == "__main__":
    celery_app.start(argv=["celery", "-A", "backend.celery_worker", "beat", "--loglevel=info"])
