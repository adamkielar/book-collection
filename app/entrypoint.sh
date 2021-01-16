#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z "$SQL_HOST $SQL_PORT"; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate
uwsgi --http :8000 --master --processes 4 --threads 2 --module app.wsgi --chmod-socket=664 --uid user
exec "$@"