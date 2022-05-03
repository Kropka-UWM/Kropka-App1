"""Chat urls file."""
# Django
from django.urls import path
from .views import CreateMessageView
from .views import GetConversationsView
from .views import GetMessagesView

app_name = 'chat'

urlpatterns = [
    path('get_conversations/', GetConversationsView.as_view(), name='get_conversations'),
    path('get_messages/', GetMessagesView.as_view(), name='get_messages'),
    path('create_message/', CreateMessageView.as_view(), name='create_message'),
]
