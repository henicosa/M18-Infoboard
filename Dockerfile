# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP app.py

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]
