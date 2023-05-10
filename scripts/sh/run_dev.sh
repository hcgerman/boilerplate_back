#!/usr/bin/env bash

db_host="$1"

# Wait for the database container to be ready
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$db_host" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing"

python manage.py migrate
python manage.py runscript seed_db
python manage.py runserver_plus 0.0.0.0:8000