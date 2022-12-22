FROM python:3.9-slim

RUN pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

ENV POETRY_VIRTUALENVS_CREATE=false

RUN poetry install --no-dev --no-root --no-interaction --no-ansi

COPY . /app

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
