"""Utils file."""
# Django
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Project
from backend.project import settings


def send_email_to_user(user):
    """Send email contains order-data to client."""
    template = 'pdf_template.html'
    msg = EmailMultiAlternatives(
        'Jakis fajny tytul',
        render_to_string(template, {
            'context': 'test',
        }),
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
    )
    msg.content_subtype = 'html'
    msg.send()