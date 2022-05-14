"""Generate leaders command."""

# Django
from django.core.management.base import BaseCommand

# Local
from ...models import CustomUser
from .gen_factories import GenerateUsersFactory


class Command(BaseCommand):
    """Command."""

    help = 'Generates predefined amount of user as leaders instances.'

    def add_arguments(self, parser):  # noqa: D102
        parser.add_argument('amount', type=int)

    def handle(self, *args, **options):
        """Handle command."""
        companies_amount = options['amount']
        GenerateUsersFactory.create_batch(
            size=companies_amount,
            account_type=CustomUser.LEADER,
        )
        self.stdout.write(self.style.SUCCESS(
                f'Generated {companies_amount} leaders!',
            ),
        )
