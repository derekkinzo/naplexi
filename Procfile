release: python manage.py migrate
web: python manage.py collectstatic --no-input; gunicorn naplexi.wsgi --log-file - --log-level debug

