"""Context processor file."""
# Project
from backend.settings.models import SettingsModel


def settings_processor(request):
    """Return processed settings."""
    return {
        'settings': SettingsModel.objects.get_or_create()[0],
    }
