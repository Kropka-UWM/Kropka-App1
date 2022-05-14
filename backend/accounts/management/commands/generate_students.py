"""Generate students command."""

# Django
from django.core.management.base import BaseCommand

# Local
from .gen_factories import GenerateUsersFactory


class Command(BaseCommand):
    """Command."""

    help = 'Generates predefined amount of users as students instances.'

    def add_arguments(self, parser):  # noqa: D102
        parser.add_argument('amount', type=int)

    def handle(self, *args, **options):
        """Handle command."""
        students_amount = options['amount']
        GenerateUsersFactory.create_batch(size=students_amount)
        self.stdout.write(self.style.SUCCESS(
                f'Generated {students_amount} students!',
            ),
        )
