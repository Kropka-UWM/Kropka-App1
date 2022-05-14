"""Chat urls file."""
# Django
from django.conf import settings
from django.urls import path

# Local
from .views import ChatDemoView
from .views import GetConversationsView
from .views import GetMessagesView

app_name = 'chat'

urlpatterns = [
    path('get_conversations/', GetConversationsView.as_view(), name='get_conversations'),
    path('get_messages/', GetMessagesView.as_view(), name='get_messages'),
    path('get_messages/<int:conv_id>/', GetMessagesView.as_view(), name='get_messages'),
]

if getattr(settings, 'DEBUG', False):
    urlpatterns += [
        path('chat-demo/', ChatDemoView.as_view(), name='chat_demo'),
        path('chat-demo/<str:conv>/', ChatDemoView.as_view(), name='chat_demo'),
    ]
