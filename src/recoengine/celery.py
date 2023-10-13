import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recoengine.settings')

app = Celery('recoengine')

app.config_from_object("django.conf:settings", namespace='CELERY')

# Use autodiscover_tasks to discover tasks from installed apps
app.autodiscover_tasks(['recoengine'], related_name='tasks')

app.conf.beat_schedule = {
    "run_product_rating_avg_every_30": {
        'task': 'task_calculate_product_ratings',
        'schedule': 60 * 20,
        'kwargs': {"all": True}
    }
}
