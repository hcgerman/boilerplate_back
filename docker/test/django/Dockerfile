FROM python:3.10-slim

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

RUN pip install --user pipenv
ENV PIPENV_HOME=/root/.local
ENV PATH="$PIPENV_HOME/bin:$PATH"

RUN mkdir -v /temp
COPY Pipfile* /temp
RUN cd /temp && pipenv requirements --dev > requirements.txt
RUN pip install -r /temp/requirements.txt

RUN apt-get update --fix-missing && apt-get install -y --no-install-recommends \
    postgresql-client

WORKDIR /app
COPY . .

ENTRYPOINT ["scripts/sh/run_test.sh"]
CMD ["-svv"]