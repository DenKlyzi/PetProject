from main.services.wiki_extractor import WikiExtractorService
from main.services.vector_storage import save_to_chroma
from chromadb import PersistentClient

def chunk_text(text, max_len=1000):
    chunks = []
    start = 0
    while start < len(text):
        end = start + max_len
        chunks.append(text[start:end])
        start = end
    return chunks

if __name__ == "__main__":
    extractor = WikiExtractorService()
    pages = extractor.collect_all()

    client = PersistentClient(path="./chroma_db")
    collection_name = "wiki_pages"
    collection = client.get_or_create_collection(name=collection_name)

    existing_ids = []
    docs = collection.get()
    if docs.get("ids"):
        existing_ids = [doc_id for sublist in docs["ids"] for doc_id in sublist]

    new_dataset = []
    for page in pages:
        page_chunks = chunk_text(page["text"])
        for idx, chunk in enumerate(page_chunks):
            chunk_id = f"{page['id']}_{idx}"
            if chunk_id in existing_ids:
                continue
            new_dataset.append({
                "id": chunk_id,
                "text": chunk,
                "metadata": {**page["metadata"], "chunk_index": idx}
            })

    if new_dataset:
        save_to_chroma(new_dataset, collection_name=collection_name)
        print(f"Добавлено {len(new_dataset)} новых страниц/кусков в ChromaDB.")
    else:
        print("Новых страниц нет.")
