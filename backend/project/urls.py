"""Project url configuration."""

# Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views.generic import TemplateView

# 3rd-party
from allauth.account.views import ConfirmEmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.settings.urls', namespace='settings')),
    path('', include('backend.handlers.urls', namespace='handlers')),
    path('', include('backend.accounts.urls', namespace='accounts')),
    path('', include('backend.chat.urls', namespace='messages')),
    path('', include('backend.notify.urls', namespace='notify')),
    path('', include('dj_rest_auth.urls')),
]


# Additional views from dj-rest-auth:
urlpatterns += [
    re_path(
        r'^account-confirm-email/(?P<key>[-:\w]+)/$',
        ConfirmEmailView.as_view(),
        name='account_confirm_email',
    ),
    path(
        'account-email-verification-sent/',
        TemplateView.as_view(
            template_name='account/email/verify_sent.html'),
        name='account_email_verification_sent',
    ),
]


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls')),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'backend.handlers.views.handler404'
handler500 = 'backend.handlers.views.handler500'
