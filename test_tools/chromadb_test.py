import chromadb
from pathlib import Path
import pandas as pd
import numpy as np

DOCS_PATH = "../data/ielts_writing"

if __name__ == "__main__":
    docs = Path(DOCS_PATH).glob("*.txt")
    ids = []
    documents = []
    metadatas = []
    for id, file_path in enumerate(docs):
        ids.append(str(id))
        with open(file_path, 'r') as f:
            documents.append(f.read())

    # print(documents[1])
    client = chromadb.Client()
    collection = client.create_collection("Stanford_Collection")
    collection.add(
        documents=documents,
        ids=ids
    )

    results = collection.query(
        query_texts=["Number of elder citizens"],
        n_results=3,
    )
    print(results)

