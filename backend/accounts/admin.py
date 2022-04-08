"""Admin file."""
# Django
from django.contrib import admin

# Register your models here.
from backend.accounts.models import CustomUser


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
