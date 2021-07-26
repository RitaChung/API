FROM python:3

WORKDIR /app
RUN apt-get update
COPY . /app
COPY cache_files/. /root/.cache/huggingface/transformers
RUN pip install -r requirements.txt
CMD HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python3 app.py

## docker build -f Dockerfile -t arabic_named_entity_recognition_api:0.0.3 .
