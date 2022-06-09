"""Context processor file."""
from backend.settings.models import SettingsModel


def settings_processor(request):
    """Settings processor."""
    return {
        'settings': SettingsModel.objects.get_or_create(),
    }
