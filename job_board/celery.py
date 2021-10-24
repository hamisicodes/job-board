from __future__ import absolute_import

import os
import django
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_board.settings')
django.setup()

app = Celery('job_board',
             broker=os.environ.get('CLOUDAMQP_URL'),
             include=['job_board.tasks'])

app.conf.beat_schedule = {
    'reset-post-upvotes-count': {
        'task': 'job_board.tasks.reset_upvotes',
        'schedule': crontab(hour=0, minute=0)  # everyday at midnight
    },

    # todo:Remove from production
    'test-task': {
        'task': 'job_board.tasks.test_task',
        'schedule': crontab(minute='*/5')
    }
}

if __name__ == '__main__':
    app.start()
