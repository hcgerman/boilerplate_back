FROM python:3.10-slim

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

RUN pip install --user pipenv

ADD Pipfile.lock Pipfile /app/

ENV PIPENV_HOME=/root/.local
ENV PATH="$PIPENV_HOME/bin:$PATH"

RUN apt-get update --fix-missing && apt-get install -y --no-install-recommends \
    postgresql-client

WORKDIR /app

RUN pipenv sync --dev --system
