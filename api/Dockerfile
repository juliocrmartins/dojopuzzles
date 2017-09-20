FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD requirements.txt /config/
RUN pip install -r /config/requirements.txt
RUN mkdir /dojopuzzles_api;
WORKDIR /dojopuzzles_api
