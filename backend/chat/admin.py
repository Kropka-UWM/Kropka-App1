"""Admin file."""
from django.contrib import admin

# Register your models here.
from .models import Conversation
from .models import Message


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """Conversation admin class."""

    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Message admin class."""

    pass
