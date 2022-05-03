"""Chat view file."""
from django.http import Http404
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Conversation
from .models import Message
from .serializers import ConversationSerializer
from .serializers import MessageSerializer


class CreateMessageView(APIView):
    """Student base info class."""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):  # noqa: D102
        if not request.user.is_authenticated:
            raise Http404
        initial_dict = {
            'test': 123,
        }
        return Response(initial_dict)


class GetConversationsView(ListAPIView):
    """Get conversations view class."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        messages = Message.objects.filter(user=self.request.user)
        return qs.filter(message__id__in=messages.values_list('id', flat=True))


class GetMessagesView(ListAPIView):
    """Get messages view class."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

