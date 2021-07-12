from sentence_transformers import SentenceTransformer


def sentence2vector(sentence):
    model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v2')
    embeddings = model.encode(sentence)
    return embeddings
