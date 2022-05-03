"""Backend urls file."""
# Django
from django.urls import path

# Project
from backend.accounts.views import CreateUserView

app_name = 'accounts'

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='rest_register'),
]
