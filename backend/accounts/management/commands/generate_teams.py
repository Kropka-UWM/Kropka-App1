"""Generate teams command."""

# Django
from django.core.management.base import BaseCommand

# Local
from ...models import Company
from .gen_factories import StudentTeamFactory


class Command(BaseCommand):
    """Command."""

    help = 'Generates predefined amount of users as students instances.'

    def add_arguments(self, parser):  # noqa: D102
        parser.add_argument('amount', type=int)
        parser.add_argument('company', type=int)

    def handle(self, *args, **options):
        """Handle command."""
        teams_amount = options['amount']
        try:
            company = Company.objects.get(id=options['company'])
            StudentTeamFactory.create_batch(
                size=teams_amount,
                company=company,
            )
            self.stdout.write(self.style.SUCCESS(
                f'Generated {teams_amount} teams!',
            ),
            )
        except Company.DoesNotExist:
            self.stdout.write(self.style.SUCCESS(
                    'Company with given ID does not exist!',
                ),
            )
