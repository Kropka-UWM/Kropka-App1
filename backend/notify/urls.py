"""Urls file."""
from django.conf import settings
from django.urls import path
from backend.notify.views import PushDemoView
from backend.notify.views import PushNavigatorView

app_name = 'notify'

urlpatterns = [
    path('navigatorPush.service.js', PushNavigatorView.as_view(), name='navigator'),
]

if getattr(settings, 'DEBUG', False):
    urlpatterns += [
        path('push-demo/', PushDemoView.as_view(), name='push_demo'),
    ]