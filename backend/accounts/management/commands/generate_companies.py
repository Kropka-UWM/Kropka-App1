"""Generate teams command."""

# Django
from django.core.management.base import BaseCommand

# Local
from .gen_factories import CompanyFactory


class Command(BaseCommand):
    """Command."""

    help = 'Generates predefined amount of users as company instances.'

    def add_arguments(self, parser):  # noqa: D102
        parser.add_argument('amount', type=int)

    def handle(self, *args, **options):
        """Handle command."""
        company_amount = options['amount']
        CompanyFactory.create_batch(
            size=company_amount,
        )
        self.stdout.write(self.style.SUCCESS(
                f'Generated {company_amount} companies!',
            ),
        )
