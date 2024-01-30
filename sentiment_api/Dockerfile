FROM python:3.11-slim-bullseye

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY config.json /app/config.json

COPY sentiment_api /app/sentiment_api

WORKDIR /app

CMD ["python", "-m", "sentiment_api", "launch", "--port", "8080"]