"""Generate companies command."""

# Django
from django.core.management.base import BaseCommand

from .gen_factories import GenerateUsersFactory
from ...models import CustomUser


class Command(BaseCommand):
    """Command."""

    help = 'Generates predefined amount of users as companies instances.'

    def add_arguments(self, parser):  # noqa: D102
        parser.add_argument('amount', type=int)

    def handle(self, *args, **options):
        """Handle command."""
        companies_amount = options['amount']
        GenerateUsersFactory.create_batch(
            size=companies_amount,
            account_type=CustomUser.COMPANY
        )
        self.stdout.write(self.style.SUCCESS(
                f'Generated {companies_amount} companies!',
            ),
        )