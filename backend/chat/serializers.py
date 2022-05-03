"""Chat serializers file."""
from rest_framework import serializers
from .models import Conversation
from .models import Message


class ConversationSerializer(serializers.ModelSerializer):
    """Conversation serializer."""

    class Meta:
        model = Conversation
        fields = [
            'id',
            'name',
        ]


class MessageSerializer(serializers.ModelSerializer):
    """Message serializer."""

    class Meta:
        model = Message
        fields = [
            'id',
            'conversation',
            'content',
        ]
