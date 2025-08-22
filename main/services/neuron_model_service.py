import ollama

def generate_answer(documents, question, model="llama3.1:8b"):
    context = "\n".join(documents)
    messages = [
        {"role": "system", "content": "Ты помогаешь отвечать на вопросы на основе вики."},
        {"role": "user", "content": f"Документы:\n{context}\n\nВопрос: {question}"}
    ]
    response = ollama.chat(model=model, messages=messages)
    return response.message.content
