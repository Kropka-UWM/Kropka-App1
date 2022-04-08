"""Views file."""
# Django
from django.contrib.auth import get_user_model
from django.http import Http404
# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

# 3rd-party
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

# Project
from backend.accounts.serializers import UserSerializer


class IndexView(TemplateView):
    """Template view."""

    def get(self, request, *args, **kwargs):
        raise Http404


class Demo404(TemplateView):
    """Demo 404."""

    template_name = 'errors/404.html'


def handler404(request, exception):
    """Not found 404 handler."""
    print(exception)  # In future configure logger
    return render(request, 'errors/404.html', status=404)


class Demo500(TemplateView):
    """Demo 500."""

    template_name = 'errors/500.html'


def handler500(request):
    """Bad request 500 handler."""
    return render(request, 'errors/500.html', status=500)


class CreateUserView(CreateAPIView):
    """Registration view."""

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UserSerializer
