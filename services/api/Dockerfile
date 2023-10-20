# syntax = docker/dockerfile:1.2
FROM python:3.8.13-slim-buster

WORKDIR /app/src

COPY ./requirements.txt /app/src/requirements.txt
RUN pip install -r requirements.txt
COPY ./src /app/src

EXPOSE 80
CMD ["uvicorn", "--ws-ping-interval", "5", "--ws-ping-timeout", "10", "--forwarded-allow-ips", "*", "--host", "0.0.0.0", "--port", "80", "main:app"]
