from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings  # or use another embedding model
import os

CHROMA_HOST = os.getenv('CHROMA_HOST', 'localhost')
CHROMA_PORT = os.getenv('CHROMA_PORT', '8000')
CHROMA_COLLECTION = os.getenv('CHROMA_COLLECTION', 'news_articles')

# You may need to adjust embedding model to your use case
embeddings = OpenAIEmbeddings()

chroma = Chroma(
    collection_name=CHROMA_COLLECTION,
    embedding_function=embeddings,
    persist_directory=None,  # Use remote ChromaDB
    client_settings={
        "host": CHROMA_HOST,
        "port": int(CHROMA_PORT),
    },
)

def index_articles(articles):
    """
    Index a list of articles into ChromaDB.
    Each article should be a dict with at least 'id', 'title', 'summary', 'source_url'.
    """
    docs = []
    metadatas = []
    for article in articles:
        docs.append(article['summary'] or article['title'])
        metadatas.append({
            "id": article['id'],
            "title": article['title'],
            "source_url": article['source_url'],
            "published_at": str(article.get('published_at', '')),
            "language": article.get('language', ''),
            "status": article.get('status', ''),
        })
    chroma.add_texts(docs, metadatas=metadatas)
    return True
