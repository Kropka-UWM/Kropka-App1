"""Apps file."""
# Django
from django.apps import AppConfig


class ChatConfig(AppConfig):
    """Chat app config."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.chat'
