"""Apps file."""
# Django
from django.apps import AppConfig


class SettingsConfig(AppConfig):
    """Settings app config."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.settings'
