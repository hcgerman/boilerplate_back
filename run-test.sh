#!/usr/bin/env bash
#-svv is pytest options
#db is the postgres service name
docker-compose -f test.yml run --rm app "-svv" "db"
docker-compose -f test.yml down --remove-orphans -v