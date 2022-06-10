"""Project url configuration."""

# Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.settings.urls', namespace='settings')),
    path('', include('backend.handlers.urls', namespace='handlers')),
    path('', include('backend.accounts.urls', namespace='accounts')),
    path('', include('backend.chat.urls', namespace='messages')),
    path('', include('backend.notify.urls', namespace='notify')),
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls'))
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
