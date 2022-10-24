FROM python:3.10-slim

RUN apt-get update && apt-get install -y git

WORKDIR /opt/app

COPY ./app/pyproject.toml ./app/poetry.lock .

RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install

COPY ./pyproject.toml ./poetry.lock .

RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install

COPY . .

CMD ["poetry", "run", "python", "-m", "disagreement"]
