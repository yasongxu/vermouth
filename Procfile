web: gunicorn config.wsgi:application
worker: celery worker --app=vermouth.taskapp --loglevel=info
