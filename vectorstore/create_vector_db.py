from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

# Importamos la función que ya creaste en el paso anterior
from loaders.load_documents import load_all_documents


def create_vector_database():
    print("=" * 50)
    print("Loading documents...")
    print("=" * 50)

    documents = load_all_documents()

    print(f"Documents loaded: {len(documents)}")

    print("\nSplitting documents into chunks...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print(f"Chunks created: {len(chunks)}")

    print("\nCreating embeddings with Ollama...")

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    print("\nCreating FAISS vector database...")

    vector_db = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    output_folder = Path("vectorstore/faiss_index")
    output_folder.mkdir(parents=True, exist_ok=True)

    vector_db.save_local(str(output_folder))

    print("\nVector database created successfully!")
    print(f"Saved in: {output_folder}")


if __name__ == "__main__":
    create_vector_database()