"""Views file."""

# Create your views here.
from django.views.generic import TemplateView


class PushDemoView(TemplateView):
    """Push demo view."""

    template_name = 'demo/push_notify.html'


class PushNavigatorView(TemplateView):
    """Push navigator view."""

    template_name = 'navigatorPush.service.js'
    content_type = 'application/javascript'