"""Views file."""

# Standard Library
import io
from collections import OrderedDict

# Django
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.db.models import Prefetch
from django.http import FileResponse
from django.http import Http404
from django.template.loader import render_to_string

# 3rd-party
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from weasyprint import HTML

# Local
from .models import Company
from .models import StudentTeam
from .serializers import AssignStudentSerializer
from .serializers import ClassicUserSerializer
from .serializers import GroupedCompanySerializer
from .serializers import JustEmailSerializer
from .serializers import StudentTeamSerializer
from .serializers import UserSerializer
from .utils import send_email_to

UserModel = get_user_model()


class CreateUserView(CreateAPIView):
    """Registration view."""

    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class GetAccountInfo(RetrieveAPIView):
    """Student base info class."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def get_object(self):  # noqa: D102
        return self.request.user


class GroupStudentsView(ListAPIView):
    """Group students view."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GroupedCompanySerializer
    queryset = Company.objects.prefetch_related('customuser_set')

    def list(self, request, *args, **kwargs):  # noqa: D102
        response = super().list(request, *args, **kwargs)
        unsetted_qs = UserModel.objects.filter(company=None)
        get_data = OrderedDict()
        for response_dict in response.data:
            if list(response_dict.items())[0][1]:
                get_data.update(response_dict)
        get_data['unsetted'] = ClassicUserSerializer(
            unsetted_qs, many=True).data
        return Response(get_data)


class AssignStudentView(APIView):
    """Assign student view."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AssignStudentSerializer

    def post(self, request, format=None):  # noqa: D102
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            student = data['student']
            student.company = data['company']
            student.save()
            serialized_user = UserSerializer(
                UserModel.objects.filter(id=student.id), many=True)
            return Response(serialized_user.data[0])
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST,
        )


class ListStudentsView(ListAPIView):
    """Retrieve students view."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClassicUserSerializer
    queryset = UserModel.objects.all()

    def get_queryset(self):  # noqa: D102
        qs = super().get_queryset()
        if not self.request.user.team:
            raise Http404
        return qs.filter(team=self.request.user.team)


class ListCompanyView(ListAPIView):
    """List company view."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StudentTeamSerializer
    queryset = StudentTeam.objects.prefetch_related('customuser_set')

    def get_queryset(self):  # noqa: D102
        qs = super().get_queryset()
        if not self.request.user.company:
            raise Http404
        return qs.filter(company=self.request.user.company)

    def list(self, request, *args, **kwargs):  # noqa: D102
        response = super().list(request, *args, **kwargs)
        data_dict = OrderedDict()
        for response_dict in response.data:
            data_dict.update(response_dict)
        return Response(data_dict)


class PDFSummaryView(APIView):
    """Just PDF view."""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = JustEmailSerializer

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
        file_buffer = io.BytesIO(html.write_pdf(
            stylesheets=[
                f'{settings.BASE_DIR}/static/css/bootstrap.min.css',
            ],
        ))
        return file_buffer

    def post(self, request, format=None):  # noqa: D102
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            file = self.gen_summary_pdf()
            fname = 'podsumowanie_i_kropka.pdf'
            if 'email' in data:
                attachments = [{'file': file, 'name': fname}]
                email = data['email']
                send_email_to(
                    email, 'Raport rozłożenia studentów z aplikacji i kropka',
                    {}, 'emails/summary.html', attachments)
            return FileResponse(
                ContentFile(file.getvalue(), fname),
                as_attachment=True, content_type='applicatiopn/pdf',
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST,
        )
