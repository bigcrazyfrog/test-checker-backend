FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install make

COPY requirements/ requirements/

RUN apt-get update && \
    python -m pip install --upgrade pip && \
    pip install -r requirements/production.txt

COPY . .

