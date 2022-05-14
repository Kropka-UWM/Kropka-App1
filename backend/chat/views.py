"""Chat view file."""
# Django
from django.views.generic import TemplateView

# class CreateConversationView(CreateAPIView):
#     """Create Message view."""
#
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = ConversationSerializer
#     queryset = Conversation.objects.all()
#
#
# class GetConversationsView(ListAPIView):
#     """Get conversations view class."""
#
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = ConversationSerializer
#     queryset = Conversation.objects.all()
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         messages = Message.objects.filter(user=self.request.user)
#         return qs.filter(message__id__in=messages.values_list('id', flat=True))
#
#
# class CreateMessageView(CreateAPIView):
#     """Create Message view."""
#
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = MessageSerializer
#     queryset = Message.objects.all()
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
# class GetMessagesView(ListAPIView):
#     """Get messages view class."""
#
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = MessageSerializer
#     queryset = Message.objects.all()
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         filter_kwargs = {}
#         if 'conv_id' in self.kwargs:
#             filter_kwargs['conversation_id'] = self.kwargs['conv_id']
#         return qs.filter(user=self.request.user, **filter_kwargs)


class ChatDemoView(TemplateView):
    """Chat demo view class."""

    template_name = 'demo/chat.html'

    def get_context_data(self, **kwargs):  # noqa: D102
        context = super().get_context_data(**kwargs)
        context['conv_name'] = 'test'
        return context
