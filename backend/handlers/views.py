"""Views file."""
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


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