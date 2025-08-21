from rest_framework import serializers


class PromptSerializer(serializers.Serializer):
    prompt = serializers.CharField(required=True, max_length=1000)
    user_id = serializers.CharField(required=True, max_length=15)

    def validate_prompt(self, value):
        if not value.strip():
            raise serializers.ValidationError("Prompt не может быть пустым")
        return value
