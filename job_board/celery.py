import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_board.settings')

app = Celery('job_board',
             broker='pyamqp://guest@localhost//',
             backend='rpc://',
             include=['job_board.tasks'])

app.conf.beat_schedule = {
    'reset-post-upvotes-count': {
        'task': "job_board.tasks.reset_upvotes",
        'schedule': crontab(hour='24',
                            minute=0,
                            )
    }
}
