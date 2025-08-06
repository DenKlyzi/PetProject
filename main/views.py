import ollama
from rest_framework.views import APIView
from rest_framework.response import Response


class NeuronModelMessageApiView(APIView):
    def post(self, request):
        model = request.data.get("model")
        prompt = request.data.get("prompt")
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        content = response["message"]["content"]
        return Response({"response": content})
