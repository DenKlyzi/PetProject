import chromadb
import ollama


def search_chroma(query: str, collection_name="wiki_embeddings", model="mxbai-embed-large", top_k=5):
    try:
        client = chromadb.PersistentClient(path="./chroma_db")
        collection = client.get_collection(name=collection_name)
    except Exception as e:
        raise RuntimeError(f"Не удалось подключиться к Chroma: {e}")
    try:
        response = ollama.embed(model=model, input=query)
        query_vector = response["embeddings"][0]
    except Exception as e:
        raise RuntimeError(f"Не удалось получить эмбеддинг через Ollama: {e}")
    try:
        results = collection.query(
            query_embeddings=[query_vector],
            n_results=top_k,
            include=["documents", "metadatas", "distances"]
        )
    except Exception as e:
        raise RuntimeError(f"Ошибка при поиске в Chroma: {e}")
    return results
