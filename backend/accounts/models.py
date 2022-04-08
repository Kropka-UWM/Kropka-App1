"""Init project."""
# Django
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class StudentTeam(models.Model):
    """Student Team model."""
    name = models.CharField(
        _('Name of team'),
        max_length=255,
    )


class Company(models.Model):
    """Company model."""
    name = models.CharField(
        _('Name of company'),
        max_length=255,
    )


class CustomUser(AbstractUser):
    """Custom User with extended functionality."""
    COMPANY = 'company'
    LEADER = 'leader'
    STUDENT = 'student'

    ACCOUNT_TYPE = [
        (COMPANY, _('Company')),
        (LEADER, _('Leader')),
        (STUDENT, _('Student')),
    ]

    account_type = models.CharField(
        _('Account type'),
        max_length=255,
        choices=ACCOUNT_TYPE,
    )
    team = models.ForeignKey(
        StudentTeam,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        verbose_name=_('Team assigned to student'),
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        verbose_name=_('Company'),
    )
    nr_index = models.CharField(_('Index student number'), max_length=16, null=True, blank=True)
    students_amount = models.IntegerField(
        _('Students amount for project'),
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
        null=True,
        blank=True,
    )

    def __str__(self):  # noqa: D102
        get_name = super().__str__()
        if self.account_type:
            return f'[{self.account_type}] {get_name}'
        return get_name

    @property
    def has_team(self):  # noqa: D102
        return bool(self.team)
