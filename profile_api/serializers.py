from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serialize a name field"""
    name = serializers.CharField(max_length=10)
