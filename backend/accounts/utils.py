"""Utils file."""
# Django
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Project
from backend.project import settings


def send_email_to_user(user, title, context, template_name=None):
    """Send email contains order-data to client."""
    if not template_name:
        template = 'pdf_template.html'
    msg = EmailMultiAlternatives(
        title,
        render_to_string(template, context),
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
    )
    msg.content_subtype = 'html'
    msg.send()
