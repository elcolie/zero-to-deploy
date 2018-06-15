#!/usr/bin/env bash

echo "pycon2018> waiting postgres initialization timeout at 120s"
dockerize -wait tcp://postgres:5432 -timeout 120s

echo "pycon2018> migrate"
python manage.py migrate

echo "Elcolie> collectstatic"
python manage.py collectstatic --noinput

echo "Elcolie> gunicorn"
gunicorn -c gunicorn.compose.py poinkbackend.config.wsgi:application
