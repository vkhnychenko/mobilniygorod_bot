FROM python:3.7-slim
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./req.txt req.txt
RUN pip install -r req.txt
RUN pip install gunicorn

RUN apt-get update && apt-get install netcat -y

COPY ./api /app/api
COPY ./manage.py /app/manage.py
COPY ./bot_api /app/bot_api
RUN mkdir /app/static
RUN python manage.py collectstatic --no-input --clear