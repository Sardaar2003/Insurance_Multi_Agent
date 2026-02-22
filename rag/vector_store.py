"""
LangChain Vector Store (Production RAG)
- Persistent storage
- Automatic chunking
- Embeddings
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# persistent directory
PERSIST_DIR = "./vector_db"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

vector_db = Chroma(
    persist_directory=PERSIST_DIR,
    embedding_function=embeddings
)


# ============================================================
# ADD DOCUMENT
# ============================================================

def add_document(text):
    """
    Chunk + store document.
    """

    docs = text_splitter.create_documents([text])

    vector_db.add_documents(docs)
    vector_db.persist()

    print("Document indexed:", len(docs), "chunks")


# ============================================================
# SEARCH
# ============================================================

def search(query, k=3):
    """
    Semantic search.
    """

    docs = vector_db.similarity_search(query, k=k)

    return [doc.page_content for doc in docs]