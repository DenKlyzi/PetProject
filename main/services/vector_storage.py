import chromadb
import ollama


def embed_with_ollama(texts, model="mxbai-embed-large"):
    embeddings = []
    for t in texts:
        response = ollama.embed(model=model, input=t)
        embeddings.append(response["embeddings"][0])
    return embeddings

def save_to_chroma(dataset, collection_name="wiki_pages", model="mxbai-embed-large"):
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(name=collection_name)
    ids = [str(item["id"]) for item in dataset]
    documents = [item["text"] for item in dataset]
    metadatas = [item["metadata"] for item in dataset]
    embeddings = embed_with_ollama(documents, model=model)
    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas,
    )
    return collection
