FROM python:3.9.7

COPY requirements.txt .
RUN apt-get -y update
RUN apt-get -y install libsndfile1 libxml2-dev libxmlsec1-dev
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
RUN python3 -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl
RUN mkdir /app
COPY app app
WORKDIR /app