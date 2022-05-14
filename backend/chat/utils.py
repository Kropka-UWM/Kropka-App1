"""Utils file."""
from .models import Conversation


def get_conversation(conv_name):  # noqa: D102
    return Conversation.objects.get_or_create(
        name=conv_name)[0]
