"""Resources file."""
# Django
from django.contrib.auth import get_user_model

# 3rd-party
from import_export import resources

# Local
from .models import Company
from .models import StudentTeam


class StudentTeamResource(resources.ModelResource):
    """StudentTeam class resource."""

    class Meta:  # noqa: D106
        model = StudentTeam
        fields = [
            'name',
            'created_dt',
        ]
        use_bulk = True
        force_init_instance = True
        skip_diff = True


class CompanyResource(resources.ModelResource):
    """Company class resource."""

    class Meta:  # noqa: D106
        model = Company
        fields = [
            'name',
            'created_dt',
        ]
        use_bulk = True
        force_init_instance = True
        skip_diff = True


class CustomUserResource(resources.ModelResource):
    """CustomUser class resource."""

    class Meta:  # noqa: D106
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'account_type',
            'nr_index',
        ]
        use_bulk = True
        force_init_instance = True
        skip_diff = True
