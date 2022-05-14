"""Utils file."""
# Local
from .models import Conversation


def get_conversation(conv_name):  # noqa: D103
    return Conversation.objects.get_or_create(
        name=conv_name)[0]
