FROM python:3.10

WORKDIR /code

COPY pyproject.toml poetry.lock /code/

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

COPY . /code

RUN poetry run prisma generate

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]