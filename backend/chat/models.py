"""Models file."""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from backend.accounts.models import CustomUser


class Conversation(models.Model):
    """Conversation model class."""

    name = models.CharField(
        _('Name of conversation'),
        max_length=255,
    )

    def __str__(self):  # noqa: D102
        return self.name


class Message(models.Model):
    """Message model class."""

    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    content = models.CharField(
        _('Content of message'),
        max_length=255,
    )

    def __str__(self):  # noqa: D102
        return _('Message from user {0}').format(self.user)
