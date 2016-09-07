FROM python:2.7-alpine
RUN mkdir /code
WORKDIR /code
RUN python setup.py install
