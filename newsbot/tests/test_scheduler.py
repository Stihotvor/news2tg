from backend.celery_worker import celery_app

def test_dummy_task():
    result = celery_app.tasks['backend.celery_worker.dummy_task'].apply(args=(2, 3))
    assert result.result == 5
