"""Mixins file."""

# Django
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class SingleInstanceMixin(object):
    """Makes sure that no more than one instance of a given model is created."""

    def clean(self):  # noqa: D102
        model = self.__class__
        if model.objects.exists() and self.id != model.objects.get().id:
            raise ValidationError(
                _('Only one object of {0} can be created').format(model.__name__),
            )
        super().clean()
