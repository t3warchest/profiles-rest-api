from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes A Name field for testing out API View"""
    name = serializers.CharField(max_length=10)