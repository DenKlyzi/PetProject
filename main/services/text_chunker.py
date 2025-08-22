def split_text_into_chunks(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def prepare_chunks(pages, chunk_size=500, overlap=50):
    dataset = []
    for page in pages:
        text = page.get("content", "")
        chunks = split_text_into_chunks(text, chunk_size, overlap)
        for i, chunk in enumerate(chunks):
            dataset.append({
                "id": f"{page['id']}_{i}",
                "text": chunk,
                "metadata": {
                    "page_id": page["id"],
                    "title": page["title"],
                    "path": page["path"],
                    "description": page.get("description", ""),
                    "updatedAt": page["updatedAt"],
                    "chunk_index": i
                }
            })
    return dataset
