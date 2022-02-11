# Build stage

FROM python:3.10-buster AS build

# Install specific version of poetry (v 1.1.12)
ENV POETRY_VERSION=1.1.12
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/* \
    && curl -sSL https://install.python-poetry.org | python3 -

ENV PATH /root/.local/bin:$PATH

# Install dependencies
WORKDIR /app

COPY pyproject.toml poetry.lock ./
# TODO ? Do we need these scripts for build?
COPY scripts ./scripts

# Used --copies option to copy the dependecies to build destination
# Used --no-dev option of poetry since we do not need to run pytest 
RUN python -m venv --copies /app/venv \
    && . /app/venv/bin/activate  \
    && poetry install --no-dev  \
    && poetry cache clear pypi --all -n

# Runtime stage
FROM python:3.10-slim-buster as prod

COPY --from=build /app/venv /app/venv/
ENV PATH /app/venv/bin:$PATH


WORKDIR /app
# Only copy the app not the tests
COPY . ./

HEALTHCHECK --start-period=30s CMD python -c \
    "import requests; requests.get('http://localhost:8000/health/', timeout=2)"

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]