"""Serializers file."""
# 3rd-party
from rest_framework import serializers

# Project
from backend.settings.models import SettingsModel


class SettingsModelSerializer(serializers.ModelSerializer):
    """Conversation serializer."""

    class Meta:  # noqa: D106
        model = SettingsModel
        fields = [
            'project_name',
            'project_logo',
            'contact_phone',
            'registration_end',
        ]
