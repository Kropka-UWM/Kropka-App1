"""Apps file."""
# Django
from django.apps import AppConfig


class HandlersConfig(AppConfig):
    """Handlers app config."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.handlers'
