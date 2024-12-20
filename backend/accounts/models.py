"""Init project."""
# Django
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    """Company model."""

    name = models.CharField(
        _('Name of company'),
        max_length=255,
        unique=True,
    )
    logo = models.ImageField(
        _('Logo of company'),
        null=True, blank=True,
    )
    created_dt = models.DateTimeField(_('Creation time'), auto_now_add=True)

    def __str__(self):  # noqa: D105
        return f'{self.name}'

    class Meta:  # noqa: D106
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')


class StudentTeam(models.Model):
    """Student Team model."""

    company = models.ForeignKey(
        Company,
        null=True, blank=True,
        verbose_name=_('Company that team belongs to'),
        on_delete=models.DO_NOTHING,
    )
    name = models.CharField(
        _('Name of team'),
        max_length=255,
        unique=True,
    )
    logo = models.ImageField(
        _('Logo of student team'),
        null=True, blank=True,
    )
    created_dt = models.DateTimeField(_('Creation time'), auto_now_add=True)

    def __str__(self):  # noqa: D105
        return f'{self.name}'

    class Meta:  # noqa: D106
        verbose_name = _('Students team')
        verbose_name_plural = _('Students teams')


class CustomUser(AbstractUser):
    """Custom User with extended functionality."""

    COMPANY = 'company'
    LEADER = 'leader'
    STUDENT_LEADER = 'student_leader'
    STUDENT = 'student'

    ACCOUNT_TYPE = [
        (COMPANY, _('Company')),
        (LEADER, _('Leader')),
        (STUDENT_LEADER, _('Student leader')),
        (STUDENT, _('Student')),
    ]

    email = models.EmailField(
        _('Email address'),
        blank=True,
        unique=True,
        error_messages={'unique': _('A user with that email already exists.')},
    )
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
    account_notes = models.TextField(_('Registration notes'), null=True, blank=True)
    average = models.DecimalField(
        _('Average from studies grades'),
        max_digits=5,
        decimal_places=2,
        null=True, blank=True,
    )

    def __str__(self):  # noqa: D105
        get_name = super().__str__()
        if self.account_type:
            return f'[{self.get_account_type_display()}] {get_name}'
        return get_name

    def get_average(self):
        """Return minimal passable average if it's not filled."""
        if self.average:
            return f'{self.average}'
        return f'{3.0}'  # Default value

    def clean(self):  # noqa: D102:
        if self.team and self.account_type == CustomUser.STUDENT_LEADER:
            queryset = self.team.customuser_set.filter(
                account_type=CustomUser.STUDENT_LEADER).exclude(id=self.id)
            if queryset.exists():
                raise ValidationError(_('No more than one leader can exist in the team!'))
        super().clean()

    @property
    def has_team(self):  # noqa: D102
        return bool(self.team)
