"""Backend urls file."""
# Django
from django.urls import path

# Local
from .views import CreateUserView
from .views import GetAccountInfo
from .views import PDFSummaryView

app_name = 'accounts'

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='rest_register'),
    path('get_account_info/', GetAccountInfo.as_view(), name='get_account_info'),
    path('generate_summary/', PDFSummaryView.as_view(), name='gen_summary')
]
