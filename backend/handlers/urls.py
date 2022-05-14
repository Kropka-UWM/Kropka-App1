"""Urls file."""
# Django
from django.conf import settings
from django.urls import path

# Local
from .views import Demo404
from .views import Demo500

app_name = 'handlers'

urlpatterns = []

if settings.DEBUG:
    urlpatterns += [
        path('demo404/', Demo404.as_view()),
        path('demo500/', Demo500.as_view()),
    ]
