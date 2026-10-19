"""Regression tests for authentication and PDF dependency upgrades."""

# Django
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test import override_settings

# 3rd-party
from rest_framework.test import APIClient


@override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
class AccountUpgradeTests(TestCase):
    """Exercise the integration between REST auth, allauth, and Django."""

    def setUp(self):  # noqa: D102
        self.client = APIClient()
        self.registration = {
            'username': 'student',
            'email': 'student@example.com',
            'first_name': 'Jan',
            'last_name': 'Kowalski',
            'password1': 'Upgrade-test-password!42',
            'password2': 'Upgrade-test-password!42',
            'account_type': 'student',
        }

    def test_registration_uses_custom_serializer(self):
        """Preserve project fields when dj-rest-auth creates an account."""
        response = self.client.post('/register/', self.registration, format='json')
        self.assertEqual(response.status_code, 201, response.data)
        user = get_user_model().objects.get(username='student')
        self.assertEqual(user.account_type, 'student')
        self.assertEqual(user.first_name, 'Jan')
        self.assertEqual(user.last_name, 'Kowalski')
        self.assertTrue(user.check_password(self.registration['password1']))

    def test_registration_rejects_unknown_account_type(self):
        """Continue validating project-specific registration fields."""
        self.registration['account_type'] = 'unknown'
        response = self.client.post('/register/', self.registration, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('account_type', response.data)

    def test_login_with_username_and_email(self):
        """Both login methods continue to return usable authentication tokens."""
        user = get_user_model().objects.create_user(
            username='student', email='student@example.com',
            password=self.registration['password1'], account_type='student',
        )
        for login in [{'username': user.username}, {'email': user.email}]:
            with self.subTest(login=login):
                client = APIClient()
                response = client.post('/login/', {
                    **login, 'password': self.registration['password1'],
                }, format='json')
                self.assertEqual(response.status_code, 200, response.data)
                client.credentials(HTTP_AUTHORIZATION=f'Token {response.data["key"]}')
                response = client.get('/get_account_info/')
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.data['id'], user.pk)
                self.assertNotIn('password1', response.data)

    def test_pdf_summary_is_generated(self):
        """Generate a real PDF with WeasyPrint and its native dependencies."""
        user = get_user_model().objects.create_user(
            username='admin', email='admin@example.com', account_type='leader',
        )
        self.client.force_authenticate(user=user)
        response = self.client.post('/generate_summary/', {}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertTrue(b''.join(response.streaming_content).startswith(b'%PDF-'))
