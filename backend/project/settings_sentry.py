"""Sentry settings."""
# Django
from django.conf import settings

# 3rd-party
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

if not getattr(settings, 'DEBUG', True) or getattr(settings, 'ENABLE_SENTRY', False):
    sentry_sdk.init(
        dsn='https://2885af6e3adc4cf1a95e4b3a10e36119@o1282924.ingest.sentry.io/6491964',
        integrations=[DjangoIntegration()],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
    )
