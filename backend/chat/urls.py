"""Chat urls file."""
# Django
from django.conf import settings
from django.urls import path
from backend.chat.views import ChatDemoView

app_name = 'chat'

urlpatterns = []

if getattr(settings, 'DEBUG', False):
    urlpatterns += [
        path('chat-demo/', ChatDemoView.as_view(), name='room'),
    ]
