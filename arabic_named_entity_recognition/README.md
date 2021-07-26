# install steps

1. git clone https://github.com/RitaChung/API.git and access into arabic_named_entity_recognition
2. docker build -f Dockerfile -t arabic_named_entity_recognition_api:0.0.1 .
3. docker run -p 3838:3838 --name entity_tmp arabic_named_entity_recognition_api:0.0.1 
4. open the browser at http://localhost:3838/ and test one example(run one time)
5. docker commit entity_tmp arabic_named_entity_recognition_api:0.0.2 
6. (offline) docker run -p 3880:3838 -e HF_DATASETS_OFFLINE=1 -e TRANSFORMERS_OFFLINE=1 arabic_named_entity_recognition_api:0.0.2
