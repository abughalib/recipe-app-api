FROM python:3.9-alpine
LABEL maintainer="abughalib63@hotmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./app/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
