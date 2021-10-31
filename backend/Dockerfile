FROM python:3.9.7

COPY requirements.txt .
RUN apt-get -y update
RUN apt-get -y install libsndfile1 libxml2-dev libxmlsec1-dev
RUN pip install -r requirements.txt
RUN mkdir /app
COPY app app
WORKDIR /app