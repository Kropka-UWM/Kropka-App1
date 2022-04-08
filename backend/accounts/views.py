"""Views file."""
# Standard Library
import io

# Django
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.http import FileResponse
from django.http import Http404
from django.template.loader import render_to_string
from django.views.generic import TemplateView

# 3rd-party
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from weasyprint import HTML

# Project
from backend.accounts.serializers import UserSerializer


class IndexView(TemplateView):
    """Template view."""

    def get(self, request, *args, **kwargs):
        raise Http404


class CreateUserView(CreateAPIView):
    """Registration view."""

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UserSerializer


def pdf_gen_code(request):
    """PDF gen code with weasyprint."""
    try:
        template = render_to_string(
            'pdf_template.html',
            {},
        )
        html = HTML(
            string=template,
            base_url=request.build_absolute_uri(),
        )
        file_buffer = io.BytesIO(html.write_pdf())
        response = FileResponse(
            ContentFile(file_buffer.getvalue(), 'example.pdf'),
            as_attachment=True, content_type='applicatiopn/pdf',
        )
        return response
    except BaseException:
        pass
    raise Http404
