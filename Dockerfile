FROM python:3.9-slim
LABEL maintainer="Adam Kielar"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get update \
    && apt-get -y install netcat gcc make libpq-dev -y \
    && apt-get clean

COPY ./app /app

RUN pip install poetry==1.0.5 \
    && poetry config virtualenvs.create false \
    && poetry install -n --no-root --no-dev

WORKDIR /app

RUN chmod +x entrypoint.sh
RUN useradd -ms /bin/bash user
USER user
ENTRYPOINT ["/app/entrypoint.sh"]