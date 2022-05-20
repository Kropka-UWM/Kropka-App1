"""Views file."""
# 3rd-party
from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView

# Project
from backend.settings.models import SettingsModel
from backend.settings.serializers import SettingsModelSerializer


class GetSettingsView(RetrieveAPIView):
    """Student base info class."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SettingsModelSerializer
    queryset = SettingsModel.objects.all()

    def get_object(self):  # noqa: D102
        return self.queryset.first()
