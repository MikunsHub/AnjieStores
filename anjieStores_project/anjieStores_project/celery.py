"""
https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html
"""
import os

from celery import Celery
from celery.schedules import crontab

from django.conf import settings

# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anjieStores_project.settings')

# you can change the name here
app = Celery("anjieStores_project")
app.conf.enable_utc = False

app.conf.update(timezone='Africa/Lagos')

# read config from Django settings, the CELERY namespace would make celery
# config keys has `CELERY` prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# discover and load tasks.py in django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    "check-stock-every-second": {
        'task': 'inventory.tasks.check_stock_cron',
        'schedule': crontab(minute='*/1'),
        
    }
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))





# @app.task
# def divide(x, y):
#     import time
#     time.sleep(5)
#     return x / y

# @app.task
# def add(x, y):
#     print("worker working")
#     return x + y