"""Chat view file."""
# Django
from django.views.generic import TemplateView

# 3rd-party
from rest_framework import permissions
from rest_framework.generics import ListAPIView

# Project
from backend.chat.models import Conversation
from backend.chat.models import Message
from backend.chat.serializers import ConversationSerializer
from backend.chat.serializers import MessageSerializer
from backend.chat.utils import get_conversation


class GetConversationsView(ListAPIView):
    """Get conversations view class."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()

    def get_queryset(self):  # noqa: D102
        qs = super().get_queryset()
        messages = Message.objects.filter(user=self.request.user)
        return qs.filter(
            message__id__in=messages.values_list('id', flat=True),
        ).order_by('created_dt')[:100]


class GetMessagesView(ListAPIView):
    """Get messages view class."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def get_queryset(self):  # noqa: D102
        qs = super().get_queryset()
        filter_kwargs = {}
        if 'conv_id' in self.kwargs:
            filter_kwargs['conversation_id'] = self.kwargs['conv_id']
        return qs.filter(user=self.request.user, **filter_kwargs).order_by('created_dt')[:25]


class ChatDemoView(TemplateView):
    """Chat demo view class."""

    template_name = 'demo/chat.html'

    def get_context_data(self, **kwargs):  # noqa: D102
        context = super().get_context_data(**kwargs)
        conv_name = kwargs.get('conv', 'test')
        context['conv'] = get_conversation(conv_name)
        return context
