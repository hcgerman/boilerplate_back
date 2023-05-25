#!/usr/bin/env bash

#-svv is pytest options
docker-compose -f test.yml run --rm app "-svv"
docker-compose -f test.yml down --remove-orphans -v