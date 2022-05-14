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
    created_dt = models.DateTimeField(_('Creation time'), auto_now_add=True)

    def __str__(self):  # noqa: D102
        return self.name

    class Meta:
        verbose_name = _('Conversation')
        verbose_name_plural = _('Conversations')


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
    created_dt = models.DateTimeField(_('Creation time'), auto_now_add=True)
    update_dt = models.DateTimeField(_('Update time'), auto_now=True)

    def __str__(self):  # noqa: D102
        return _('Message {0} from user {1}').format(self.id, self.user)

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')
