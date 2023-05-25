# Backend

## Overview

This project is a backend system developed using the Django framework.
It provides authentication based on JSON Web Token.

## Features

- Login
- Refresh Access Token
- Logout
- Verify Refresh Token

## Requirements

- Python 3.10
- Django 4.2
- Pipenv
- postgres 15

## Installation

For development purpose, I recommend use docker and docker compose to run this project.

1. Clone the repository: `git clone git@github.com:hcgerman/boilerplate_back.git`
2. Change into the project directory: `boilerplate_back`
3. Copy environment variables `cp docker/local/local.env.example docker/local/local.env`
4. Generate private and public keys `scripts/sh/keypair.sh`
5. Copy generated keys `mv private.pem public.pem docker/local/`
6. Build images: `docker-compose -f local.yml build`
7. Run the development server: `docker-compose -f local.yml up`
8. Stop the development server: `docker-compose -f local.yml down`

## Usage

Access the Rest API examples by postman.

_**_For this project you can use `security` collection_**_

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/4301102-77a0c2c4-a762-4ef3-a9d7-1cf12a97676a?action=collection%2Ffork&collection-url=entityId%3D4301102-77a0c2c4-a762-4ef3-a9d7-1cf12a97676a%26entityType%3Dcollection%26workspaceId%3D4f258398-fb8a-4d05-ba0b-27079cf2a680#?env%5Bsales%20backend%20environment%5D=W3sia2V5IjoidG9rZW4iLCJ2YWx1ZSI6ImV5SjBlWEFpT2lKS1YxUWlMQ0poYkdjaU9pSlNVekkxTmlKOS5leUowYjJ0bGJsOTBlWEJsSWpvaVlXTmpaWE56SWl3aVpYaHdJam94TmpBek9EQTJPRFl4TENKcWRHa2lPaUptTldRek56UXlaR1JsWVdZME9EVXlZVGN5TVRWaE5URXlNVEl6WXpjeE1TSXNJblZ6WlhKZmFXUWlPaklzSW5WelpYSnVZVzFsSWpvaVoyVnliV0Z1SW4wLlBnOGZDV01Iek9sbERMazc5NDJZYUdJc1oyWnAtd1ZZN2RWZnljWHNvU1laMkRUcHAxbGxMcWpGSzF0RWZfYWdUNy1uS05oUWVtamM0MXpvZXNRdGkyN0Q4ekpPb0VaRDVaNnhHSEFwbXpNMnRjdmsxelNfMm5iejNlcFJiMkJwOVljLU0weDdhbmF6M1NZeDlOSlg5b2NodUNIWVZxckcxdTBqYkZheGw5N1VFWmFKRk1tSzB3V25naURYRHFtOUJncEs4blczcTR2SFN6VE1LaUxaWUIzbUNzeFY3Y0w2U1VZWjR4cm1ITWI3SFpDTUxQako1T29TN0Q0alNDRmdJdzhiTlJHVFd3NUtQQnRZWEtndjNZTEN4RkxCRHNHRVJFSHFrZWpNSndXaUVvSnhNWktIQUFVY1djd2ZnWGJLcGdhbjMxWHN4MkNJTlotQ0NSR0JsSllsSXE2Wlg0YUgxbWlwYzFHeDZ6MEFBYTVVTWNYU3duWWw2SkdYREtPSnRLTHUxM0M5WXNQZFpRVWgtN3RDZDFyZEs1SXRrV3hNelg1UG9uaTJDSUlkSTVCV1VzQzEzVWFmUU8xVlFSN1QyVk1GSGMybmk5eEZLMzZmNUhtazJITWZsbjh4a2ZPVi03Y1g2QjJyOWtLNVF1TE14eURvTGlnMVFGWm9fZXdLeUp4V2txZmdQdFFIOHlIQ25KV1hhRFJlR0VKeXE0Z1A3QW1YNFhHLTktcFNYSE5ZU2dmNWFrOFNNZ0g3Z29qTndQbXFMdWFQQ1BwLWJsbXQ5SFhJdXFCVU1jeTB0NzlUZHVUX091ZXF6bUprNVVEXzJqbkFKN09yUVlMbnNsWDZNNTRfRFF1OHhoZlNBUGdNMmlTMXZHU1RpZEdDdHp4Z0hsZF9xSGRHcHhjIiwiZW5hYmxlZCI6dHJ1ZX0seyJrZXkiOiJiYXNlVXJsIiwidmFsdWUiOiJodHRwOi8vMTI3LjAuMC4xOjgwODAiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9XQ==)

## Testing

To run the tests, you need to prepare your own docker-compose configuration file only if you use this method. 

1. Build images: `docker-compose -f test.yml build`
2. Run tests: `./run-test.sh`

## Some extra commands you might need in the future.

````bash
# enter bash in docker container
docker-compose run --service-ports app bash

# pipenv commands

# install a package
pipenv install package
# install a package as dev dependency
pipenv install --dev package

# run python commands
pipenv run python somepythonfile.py

python manage.py migrate
# generate *.po translation files
python manage.py makemessages -a

# create a new app in /apps directory
# for example inventory app
mkdir ./apps/inventory
python manage.py startapp inventory ./apps/inventory
````

Populate development db

````bash
python manage.py runscript seed_db
````

## Authors

- [@hcgerman](https://github.com/hcgerman)


## License
This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for more information.