"""Backend urls file."""
# Django
from django.urls import path

# 3rd-party
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.registration.views import ResendEmailVerificationView
from dj_rest_auth.registration.views import VerifyEmailView

# Local
from .views import AssignStudentView
from .views import GetAccountInfo
from .views import GroupStudentsView
from .views import ListCompanyView
from .views import ListStudentsView
from .views import PDFSummaryView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='rest_register'),
    path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('resend-email/', ResendEmailVerificationView.as_view(), name='rest_resend_email'),
    path('group_students/', GroupStudentsView.as_view(), name='group_students'),
    path('list_students/', ListStudentsView.as_view(), name='list_students'),
    path('list_companies/', ListCompanyView.as_view(), name='list_companies'),
    path('assign_student/', AssignStudentView.as_view(), name='assign_student'),
    path('get_account_info/', GetAccountInfo.as_view(), name='get_account_info'),
    path('generate_summary/', PDFSummaryView.as_view(), name='gen_summary'),
]
