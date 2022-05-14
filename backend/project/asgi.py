"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

# Standard Library
import os

# 3rd-party
from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

# Project
from backend.chat import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.project.settings')

application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(routing.websocket_urlpatterns)
        ),
    ),
})
