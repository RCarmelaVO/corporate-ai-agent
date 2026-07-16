from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings


VECTORSTORE_PATH = "vectorstore/faiss_index"


def load_retriever():

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    vector_db = FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vector_db.as_retriever(
        search_kwargs={
            "k": 3
        }
    )

    return retriever