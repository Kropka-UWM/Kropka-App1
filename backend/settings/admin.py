"""Settings file."""
# Django
from django.contrib import admin

# Project
from backend.settings.models import SettingsModel


@admin.register(SettingsModel)
class SettingsModelAdmin(admin.ModelAdmin):
    """SettingsModel admin class."""

    list_display = [
        '__str__',
    ]
