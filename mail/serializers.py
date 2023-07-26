from rest_framework import serializers, status
from rest_framework.response import Response


class SendMailSerializer(serializers.Serializer):
    """Send mail serializer"""
    recipients = serializers.ListField(
        child=serializers.EmailField(
            max_length=150,
            allow_null=True
        )
    )
    body = serializers.CharField()

