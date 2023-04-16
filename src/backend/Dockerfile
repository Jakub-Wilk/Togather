FROM python:3.11

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.3.2

RUN groupadd --gid 1000 python && useradd --uid 1000 --gid 1000 -m python
RUN mkdir -p /home/python/app

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /home/python/app
COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false