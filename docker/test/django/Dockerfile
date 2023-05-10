FROM python:3.10-slim AS builder

RUN pip install --user pipenv

# Tell pipenv to create venv in the current directory
ENV PIPENV_VENV_IN_PROJECT=1

# Pipfile contains requests
ADD Pipfile.lock Pipfile /app/

WORKDIR /app

ENV PIPENV_HOME=/root/.local
ENV PATH="$PIPENV_HOME/bin:$PATH"
RUN pipenv sync


FROM python:3.10-slim AS runtime

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -v /app/.venv
COPY --from=builder /app/.venv/ /app/.venv/
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Create a non-root user with a specified user ID and group ID
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Switch to the newly created user
USER appuser
