FROM python:3.9-slim as builder

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

ENV POETRY_VIRTUALENVS_IN_PROJECT=true

RUN pip install poetry && poetry install --without root,dev --no-interaction --no-ansi

#

FROM python:3.9-slim

WORKDIR /app

COPY . .
COPY --from=builder /app/.venv ./.venv

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
