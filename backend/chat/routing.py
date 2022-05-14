"""Chat routing"""
# Django
from django.urls import path

# Local
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/<str:conv_name>/', ChatConsumer.as_asgi()),
]