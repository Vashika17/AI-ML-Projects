from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "AI is transforming industries",
    "Machine learning is a subset of AI",
    "NLP deals with text data"
]

vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(documents)

def retrieve(query):
    query_vec = vectorizer.transform([query])
    sim = cosine_similarity(query_vec, doc_vectors)
    return documents[sim.argmax()]
