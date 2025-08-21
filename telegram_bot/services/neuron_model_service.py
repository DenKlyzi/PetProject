from ollama import Client
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class NeuronModelService:
    @staticmethod
    def get_ai_response(prompt: str, user_id: int) -> str:
        client = Client(settings.OLLAMA_HOST)
        response = client.chat(
            model="llama3.1:8b",
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": prompt}
            ]
        )
        return response["message"]["content"]
