"""Chat routing"""
from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/<str:conv_name>/', ChatConsumer.as_asgi()),
]