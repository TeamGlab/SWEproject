release: python UFSailWebsite/manage.py migrate
web: gunicorn --chdir UFSailWebsite UFSailWebsite.wsgi --log-file -
