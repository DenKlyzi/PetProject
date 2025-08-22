import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from telegram_bot.services.neuron_model_service import NeuronModelService
from .serializers import PromptSerializer
from main.services.wiki_extractor import WikiExtractorService
from main.services.text_chunker import prepare_chunks
from main.services.vector_storage import save_to_chroma
from main.services.search_service import search_chroma

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


class WikiExtractorApiView(APIView):
    def get(self, request):
        pages = WikiExtractorService().collect_all()
        return Response(pages, status=status.HTTP_200_OK)


class WikiEmbeddingApiView(APIView):
    def post(self, request):
        pages = WikiExtractorService().collect_all()
        for page in pages:
            page["content"] = page.get("description") or page["title"]
        dataset = prepare_chunks(pages, chunk_size=800, overlap=100)
        if not dataset:
            return Response({"error": "Нет чанков для добавления"}, status=400)
        collection = save_to_chroma(dataset, collection_name="wiki_embeddings")
        return Response(
            {
                "message": f"Загружено {len(dataset)} чанков",
                "collection": collection.name,
            },
            status=status.HTTP_200_OK
        )


class WikiSearchApiView(APIView):
    def post(self, request):
        query = request.data.get("query", "").strip()
        if not query:
            return Response({"error": "Query is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            results = search_chroma(query, collection_name="wiki_embeddings", top_k=5)
            return Response(results, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
