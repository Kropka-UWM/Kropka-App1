"""Admin file."""
# Django
from django.contrib import admin

# Local
from .models import Company
from .models import CustomUser
from .models import StudentTeam


@admin.register(StudentTeam)
class StudentTeamAdmin(admin.ModelAdmin):
    """Student Team admin."""

    list_display = [
        'name',
    ]
    search_fields = [
        'name',
    ]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Company admin."""

    list_display = [
        'name',
    ]
    search_fields = [
        'name',
    ]


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Custom User admin."""

    list_display = [
        '__str__',
        'account_type',
        'nr_index',
    ]
    search_fields = [
        'nr_index',
    ]
    list_filter = [
        'account_type',
    ]
