#!/usr/bin/env bash

pytest_arguments="$1"

# Wait for the database container to be ready
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  echo >&2 "Postgres is unavailable - sleeping"
  sleep 1
done

echo >&2 "Postgres is up - continuing"

pytest "$pytest_arguments"
