"""Resources file."""
# Django
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# 3rd-party
from import_export import fields
from import_export import resources

# Local
from .models import Company
from .models import StudentTeam


class StudentTeamResource(resources.ModelResource):
    """StudentTeam class resource."""

    name = fields.Field(
        attribute='name',
        column_name=_('Name of team'),
    )
    created_dt = fields.Field(
        attribute='created_dt',
        column_name=_('Created at'),
    )

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

    name = fields.Field(
        attribute='name',
        column_name=_('Name of company'),
    )
    created_dt = fields.Field(
        attribute='created_dt',
        column_name=_('Created at'),
    )

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

    first_name = fields.Field(
        attribute='first_name',
        column_name=_('First name'),
    )
    last_name = fields.Field(
        attribute='last_name',
        column_name=_('Last name'),
    )
    email = fields.Field(
        attribute='email',
        column_name=_('Email address'),
    )
    username = fields.Field(
        attribute='username',
        column_name=_('Username'),
    )
    account_type = fields.Field(
        attribute='account_type',
        column_name=_('Account type'),
    )
    nr_index = fields.Field(
        attribute='nr_index',
        column_name=_('Index number'),
    )

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
