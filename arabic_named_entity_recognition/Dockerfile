FROM python:3

WORKDIR /app
RUN apt-get update
COPY . /app
RUN pip install -r requirements.txt
CMD python3 app.py

## docker build -f Dockerfile -t arabic_named_entity_recognition_api:0.0.1 .
