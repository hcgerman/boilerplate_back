#!/usr/bin/env bash

pytest_arguments="$1"
db_host="$2"

# Wait for the database container to be ready
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$db_host" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  echo >&2 "Postgres is unavailable - sleeping"
  sleep 1
done

echo >&2 "Postgres is up - continuing"

pytest "$pytest_arguments"
