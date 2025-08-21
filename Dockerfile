FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential libpq-dev curl gcc g++ python3-dev && \
    rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry --version
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

COPY . .

WORKDIR /app

EXPOSE 8000
