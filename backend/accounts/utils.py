"""Utils file."""
# Django
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Project
from backend.project import settings


def send_email_to(email, title, context, template_name=None, attachments=None):
    """Send email contains order-data to client."""
    if not template_name:
        template_name = 'pdf_template.html'
    msg = EmailMultiAlternatives(
        title,
        render_to_string(template_name, context),
        settings.DEFAULT_FROM_EMAIL,
        [email],
    )
    if attachments:
        for attach in attachments:
            msg.attach(attach['name'], attach['file'].getvalue())
    msg.content_subtype = 'html'
    msg.send()
