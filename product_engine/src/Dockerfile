FROM python:3.11

COPY product_engine/src/ /app
COPY common/ /app/common

WORKDIR /app

RUN pip install -r requirements.txt

ENV PYTHONPATH=/app
