from chromadb import PersistentClient
from main.services.neuron_model_service import generate_answer
from main.services.vector_storage import embed_with_ollama

def answer_query(user_query, collection_name="wiki_pages", top_k=5, model="mxbai-embed-large"):
    client = PersistentClient(path="./chroma_db")
    collection = client.get_collection(name=collection_name)
    query_embedding = embed_with_ollama([user_query], model=model)
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k,
        include=["documents", "distances", "metadatas"]
    )
    documents = results["documents"][0]
    distances = results["distances"][0]
    relevant_docs = [doc for doc, dist in zip(documents, distances) if dist < 1.0]
    if not relevant_docs:
        return "По вашему запросу ничего не найдено."
    answer = generate_answer(relevant_docs, user_query)
    return answer
