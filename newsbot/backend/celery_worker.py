# Celery worker entrypoint
import os
from celery import Celery

celery_app = Celery(
    'newsbot',
    broker=os.getenv('CELERY_BROKER_URL', 'redis://redis:6379/0'),
    backend=os.getenv('CELERY_RESULT_BACKEND', 'redis://redis:6379/0')
)

celery_app.conf.update(
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    timezone='UTC',
    enable_utc=True,
)

@celery_app.task
def dummy_task(x, y):
    """A simple dummy task for testing."""
    return x + y
