# Sales Backend

## Overview

This project is a backend system developed using the Django framework.
It provides centralized APIs for managing various business functions such as inventory management and sales management.

## Features

- Inventory management: Keep track of your products and stock levels.
- Sales management: Manage sales activities, quotes, and payments.

## Requirements

- Python 3.10
- Django 4.1.3
- poetry 1.3
- Other dependencies managed by poetry
- postgres 15

## Installation

For development purpose, I recommend use docker and docker compose to run this project.

1. Clone the repository: `git clone git@github.com:ghc92/backend_store.git`
2. Change into the project directory: `backend_store`
3. Copy environment variables `cp docker/local/local.env.example docker/local/local.env`
4. Build images: `docker-compose -f local.yml build`
5. Run the development server: `docker-compose -f local.yml up`
6. Stop the development server: `docker-compose -f local.yml down`

## Usage

Access the Rest API examples by postman.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/4301102-77a0c2c4-a762-4ef3-a9d7-1cf12a97676a?action=collection%2Ffork&collection-url=entityId%3D4301102-77a0c2c4-a762-4ef3-a9d7-1cf12a97676a%26entityType%3Dcollection%26workspaceId%3D4f258398-fb8a-4d05-ba0b-27079cf2a680#?env%5Bsales%20backend%20environment%5D=W3sia2V5IjoidG9rZW4iLCJ2YWx1ZSI6ImV5SjBlWEFpT2lKS1YxUWlMQ0poYkdjaU9pSlNVekkxTmlKOS5leUowYjJ0bGJsOTBlWEJsSWpvaVlXTmpaWE56SWl3aVpYaHdJam94TmpBek9EQTJPRFl4TENKcWRHa2lPaUptTldRek56UXlaR1JsWVdZME9EVXlZVGN5TVRWaE5URXlNVEl6WXpjeE1TSXNJblZ6WlhKZmFXUWlPaklzSW5WelpYSnVZVzFsSWpvaVoyVnliV0Z1SW4wLlBnOGZDV01Iek9sbERMazc5NDJZYUdJc1oyWnAtd1ZZN2RWZnljWHNvU1laMkRUcHAxbGxMcWpGSzF0RWZfYWdUNy1uS05oUWVtamM0MXpvZXNRdGkyN0Q4ekpPb0VaRDVaNnhHSEFwbXpNMnRjdmsxelNfMm5iejNlcFJiMkJwOVljLU0weDdhbmF6M1NZeDlOSlg5b2NodUNIWVZxckcxdTBqYkZheGw5N1VFWmFKRk1tSzB3V25naURYRHFtOUJncEs4blczcTR2SFN6VE1LaUxaWUIzbUNzeFY3Y0w2U1VZWjR4cm1ITWI3SFpDTUxQako1T29TN0Q0alNDRmdJdzhiTlJHVFd3NUtQQnRZWEtndjNZTEN4RkxCRHNHRVJFSHFrZWpNSndXaUVvSnhNWktIQUFVY1djd2ZnWGJLcGdhbjMxWHN4MkNJTlotQ0NSR0JsSllsSXE2Wlg0YUgxbWlwYzFHeDZ6MEFBYTVVTWNYU3duWWw2SkdYREtPSnRLTHUxM0M5WXNQZFpRVWgtN3RDZDFyZEs1SXRrV3hNelg1UG9uaTJDSUlkSTVCV1VzQzEzVWFmUU8xVlFSN1QyVk1GSGMybmk5eEZLMzZmNUhtazJITWZsbjh4a2ZPVi03Y1g2QjJyOWtLNVF1TE14eURvTGlnMVFGWm9fZXdLeUp4V2txZmdQdFFIOHlIQ25KV1hhRFJlR0VKeXE0Z1A3QW1YNFhHLTktcFNYSE5ZU2dmNWFrOFNNZ0g3Z29qTndQbXFMdWFQQ1BwLWJsbXQ5SFhJdXFCVU1jeTB0NzlUZHVUX091ZXF6bUprNVVEXzJqbkFKN09yUVlMbnNsWDZNNTRfRFF1OHhoZlNBUGdNMmlTMXZHU1RpZEdDdHp4Z0hsZF9xSGRHcHhjIiwiZW5hYmxlZCI6dHJ1ZX0seyJrZXkiOiJiYXNlVXJsIiwidmFsdWUiOiJodHRwOi8vMTI3LjAuMC4xOjgwODAiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9XQ==)

## Testing

To run the tests, you need to prepare your own docker-compose configuration file only if you use this method. 

1. Build images: `docker-compose -f test.yml build`
2. Run tests: `docker-compose -f test.yml run --rm app ./scripts/sh/wait-for-postgres.sh db poetry run pytest -svv`
3. Stop test: `docker-compose -f test.yml down --remove-orphans -v`

You can create Bash aliases for steps 2,3 and 4. Copy the following code into your Bash configuration:

````bash
alias test-build="docker-compose -f test.yml build"
alias test="docker-compose -f test.yml run --rm app ./scripts/sh/wait-for-postgres.sh db poetry run pytest "
alias test-stop="docker-compose -f test.yml down --remove-orphans -v"
````

## Some extra commands that you can need in the future.

````bash
# enter bash in docker container
docker-compose run --service-ports app bash

# poetry commands
poetry add package-name
poetry add --group dev package-name

# run python commands
poetry run python manage.py migrate

# generate *.po translation files
poetry run python manage.py makemessages -a

mkdir ./apps/auth
pipenv run python manage.py startapp auth ./apps/auth
pipenv install --dev package
````

Populate development db

````bash
poetry run python manage.py runscript seed_db
````

## Contribute
We welcome contributions to this project. If you have an idea for a new feature or have found a bug, please open an issue or submit a pull request.

## License
This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for more information.