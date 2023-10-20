
# syntax = docker/dockerfile:1.2
FROM python:3.9.5-slim-buster

WORKDIR /app/src
COPY ./requirements.txt /app/src/requirements.txt
RUN pip install -r requirements.txt

COPY ./src /app/src

EXPOSE 8080
CMD ["uvicorn", "--forwarded-allow-ips", "*", "--host", "0.0.0.0", "--port", "8080", "main:app"]
