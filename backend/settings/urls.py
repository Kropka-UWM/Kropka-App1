"""Settings url file."""
# Django
from django.urls import path

# Local
from .views import GetSettingsView

app_name = 'settings'

urlpatterns = [
    path('get_site_settings/', GetSettingsView.as_view(), name='get_settings'),
]
