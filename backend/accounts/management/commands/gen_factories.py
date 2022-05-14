"""Gen based factories."""
# Django
from django.utils import timezone

# 3rd-party
import factory
from factory.django import DjangoModelFactory

# Project
from backend.accounts.models import CustomUser


class GenerateUsersFactory(DjangoModelFactory):
    """Factory for User model."""

    class Meta:  # noqa: D106

        model = CustomUser
        django_get_or_create = ('username',)

    username = factory.Sequence(lambda n: f'User {n}')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    is_staff = False
    is_active = True
    date_joined = timezone.now()
    account_type = CustomUser.STUDENT
    nr_index = factory.Sequence(lambda n: str(n))