"""Admin file."""
from django.contrib import admin

# Register your models here.
from .models import Conversation
from .models import Message


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """Conversation admin class."""

    search_fields = [
        'name',
    ]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Message admin class."""

    list_display = [
        '__str__',
        'conversation',
    ]

    search_fields = [
        'user__first_name',
        'user__last_name',
        'user__username',
        'user__email',
        'conversation__name',
    ]
