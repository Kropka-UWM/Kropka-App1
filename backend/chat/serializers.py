"""Chat serializers file."""
# 3rd-party
from rest_framework import serializers

# Local
from .models import Conversation
from .models import Message


class ConversationSerializer(serializers.ModelSerializer):
    """Conversation serializer."""

    class Meta:  # noqa: D106
        model = Conversation
        fields = [
            'id',
            'name',
        ]


class MessageSerializer(serializers.ModelSerializer):
    """Message serializer."""

    message = serializers.SerializerMethodField()

    class Meta:  # noqa: D106
        model = Message
        fields = [
            'id',
            'conversation',
            'message',
        ]

    @staticmethod
    def get_message(obj):  # noqa: D102
        return f'{obj.user}: {obj.content}'
