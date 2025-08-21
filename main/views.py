import logging
# import chromadb
import ollama

# from wikijs import WikiJS

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from telegram_bot.services.neuron_model_service import NeuronModelService
from .serializers import PromptSerializer

logger = logging.getLogger(__name__)


class NeuronModelMessageApiView(APIView):
    def post(self, request):
        serializer = PromptSerializer(data=request.data)
        if not serializer.is_valid():
            logger.warning(f"Invalid request data: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        prompt = serializer.validated_data['prompt']
        user_id = serializer.validated_data['user_id']
        response_text = NeuronModelService.get_ai_response(prompt, user_id)
        return Response({"response": response_text}, status=status.HTTP_200_OK)

class WebHock(APIView):
    def hock_wiki(self):
        ...



# class EmbedingModelMessageApiView(APIView):
#     def get_embedings(self) -> str:
#         documents = []
#         client = chromadb.Client()
#         collection = client.create_collection(name="md_docs")
#         for i, d in enumerate(documents):
#             response = ollama.embed(model="mxbai-embed-large", input=d)
#             embeddings = response["embeddings"]
#             collection.add(
#                 ids=[str(i)],
#                 embeddings=embeddings,
#                 documents=[d]
#             )
