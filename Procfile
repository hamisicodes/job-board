web gunicorn job_board.wsgi --log-file -
worker: celery -A job_board worker -l info
beat: celery -A job_board beat --loglevel=info 
