"""Urls file."""
from django.conf import settings
from django.urls import path
from .views import FirebasePushView
from .views import PushDemoView
# from .views import PushNavigatorView
from .views import register_push

app_name = 'notify'

urlpatterns = [
    # path('navigatorPush.service.js', PushNavigatorView.as_view(), name='navigator'),
    path('firebase-messaging-sw.js', FirebasePushView.as_view(), name='firebase_sw'),
    path('register-push/', register_push, name='push_registration')
]

if getattr(settings, 'DEBUG', False):
    urlpatterns += [
        path('push-demo/', PushDemoView.as_view(), name='push_demo'),
    ]