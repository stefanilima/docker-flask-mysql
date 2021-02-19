FROM python:3

MAINTAINER Stefani Lima <stefanisilvadelima@hotmail.com>

EXPOSE 5000

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./app /app
CMD python index.py