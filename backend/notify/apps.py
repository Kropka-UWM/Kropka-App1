"""Apps file."""
from django.apps import AppConfig


class NotifyConfig(AppConfig):
    """Notify config."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.notify'
