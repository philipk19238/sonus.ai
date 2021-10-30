FROM python:3

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /app
COPY app app
WORKDIR /app