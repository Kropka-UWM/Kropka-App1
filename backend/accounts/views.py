"""Views file."""

# Standard Library
import io

# Django
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.db.models import Prefetch
from django.http import FileResponse
from django.template.loader import render_to_string

# 3rd-party
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from weasyprint import HTML

# Local
from .models import Company
from .models import StudentTeam
from .serializers import JustEmailSerializer
from .serializers import UserSerializer


class CreateUserView(CreateAPIView):
    """Registration view."""

    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class GetAccountInfo(RetrieveAPIView):
    """Student base info class."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    def get_object(self):  # noqa: D102
        return self.request.user


class PDFSummaryView(APIView):
    """Just PDF view."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = JustEmailSerializer

    def send_mail(self, email):  # noqa: D102
        pass

    def gen_summary_pdf(self):  # noqa: D102
        companies = Company.objects.prefetch_related(
            Prefetch('studentteam_set', queryset=StudentTeam.objects.prefetch_related(
                Prefetch('customuser_set', to_attr='user_list')), to_attr='team_list'))
        template = render_to_string(
            'summary.html',
            {'companies': companies},
        )
        html = HTML(
            string=template,
            base_url=self.request.build_absolute_uri(),
        )
        file_buffer = io.BytesIO(html.write_pdf())
        response = FileResponse(
            ContentFile(file_buffer.getvalue(), 'example.pdf'),
            as_attachment=True, content_type='application/pdf',
        )
        return response

    def post(self, request, format=None):  # noqa: D102
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            file = self.gen_summary_pdf()
            if 'email' in data:
                self.send_mail(data['email'])
            return FileResponse(
                ContentFile(file.getvalue(), 'podsumowanie_i_kropka.pdf'),
                as_attachment=True, content_type='applicatiopn/pdf',
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST,
        )
