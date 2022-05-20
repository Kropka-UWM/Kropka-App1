"""Gen based factories."""
# Django
from django.utils import timezone

# 3rd-party
import factory
from factory.django import DjangoModelFactory

# Project
from backend.accounts.models import Company
from backend.accounts.models import CustomUser
from backend.accounts.models import StudentTeam


class GenerateUsersFactory(DjangoModelFactory):
    """Factory for User model."""

    class Meta:  # noqa: D106

        model = CustomUser
        django_get_or_create = ('username',)

    username = factory.Sequence(lambda n: f'User{n}')
    password = factory.Sequence(lambda n: f'BeSurprisedWithThisPassword{n}')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    is_staff = False
    is_active = True
    date_joined = timezone.now()
    account_type = CustomUser.STUDENT
    nr_index = factory.Sequence(lambda n: str(n))


class StudentTeamFactory(DjangoModelFactory):
    """Student Team factory."""

    class Meta:  # noqa: D106

        model = StudentTeam
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: f'Team {n}')


class CompanyFactory(DjangoModelFactory):
    """Company factory."""

    class Meta:  # noqa: D106

        model = Company
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: f'Company {n}')
