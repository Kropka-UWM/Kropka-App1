"""Models file."""
# Django
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Project
from backend.settings.mixins import SingleInstanceMixin


class SettingsModel(SingleInstanceMixin, models.Model):
    """Settings model."""

    project_name = models.CharField(_('Name of project'), max_length=255, default='Kropka-App1')
    project_logo = models.ImageField(_('Logo of project'), max_length=255, blank=True, null=True)
    contact_phone = models.CharField(
        _('Phone number for contact'),
        max_length=255,
        blank=True,
        null=True,
    )
    registration_end = models.DateTimeField(
        _('Registration end time'),
        blank=True, null=True,
    )

    def check_if_registration_open(self):  # noqa: D102
        return timezone.now() <= self.registration_end

    def __str__(self):  # noqa: D105
        return self.project_name

    class Meta:  # noqa: D106
        verbose_name = _('Settings')
        verbose_name_plural = verbose_name
