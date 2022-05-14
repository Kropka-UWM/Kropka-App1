"""Apps file."""
# Django
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Accounts app config."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.accounts'
