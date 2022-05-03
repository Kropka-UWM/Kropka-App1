"""Chat view file."""
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from .models import Conversation
from .models import Message
from .serializers import ConversationSerializer
from .serializers import MessageSerializer


class CreateConversationView(CreateAPIView):
    """Create Message view."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()


class GetConversationsView(ListAPIView):
    """Get conversations view class."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        messages = Message.objects.filter(user=self.request.user)
        return qs.filter(message__id__in=messages.values_list('id', flat=True))


class CreateMessageView(CreateAPIView):
    """Create Message view."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GetMessagesView(ListAPIView):
    """Get messages view class."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
