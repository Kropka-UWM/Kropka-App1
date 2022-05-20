"""Admin file."""
# Django
from django.contrib import admin

# 3rd-party
from import_export.admin import ExportMixin

# Local
from .models import Company
from .models import CustomUser
from .models import StudentTeam
from .resources import CompanyResource
from .resources import CustomUserResource
from .resources import StudentTeamResource


@admin.register(Company)
class CompanyAdmin(ExportMixin, admin.ModelAdmin):
    """Company admin."""

    list_display = [
        'name',
    ]
    search_fields = [
        'name',
    ]
    resource_class = CompanyResource


@admin.register(StudentTeam)
class StudentTeamAdmin(ExportMixin, admin.ModelAdmin):
    """Student Team admin."""

    list_display = [
        'name',
        'company',
    ]
    search_fields = [
        'name',
    ]
    resource_class = StudentTeamResource


@admin.register(CustomUser)
class CustomUserAdmin(ExportMixin, admin.ModelAdmin):
    """Custom User admin."""

    list_display = [
        '__str__',
        'account_type',
        'team',
        'nr_index',
    ]
    search_fields = [
        'nr_index',
        'company__name'
        'team__name',
    ]
    list_filter = [
        'account_type',
    ]
    resource_class = CustomUserResource
