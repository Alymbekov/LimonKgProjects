import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'limon_project.settings')

app = Celery('limon_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-spam-email-2-min': {
        'task': 'users.tasks.spam_email',
        'schedule': crontab(minute='*/5'),
    },
}
