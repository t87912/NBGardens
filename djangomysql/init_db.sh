#!/bin/sh

python manage.py runserver

echo "------ Create database tables ------"
python manage.py migrate --noinput

echo "------ starting gunicorn &nbsp;------"
gunicorn nbgardensdjango.wsgi --workers 2
