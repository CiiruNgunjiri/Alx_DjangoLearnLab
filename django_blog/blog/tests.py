from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

class AuthTests(TestCase):
    def setUp(self):
        # Define user credentials
        self.credentials = {
            'username': 'testuser',
            'password': 'testpass'
        }
        # Create a user for testing
        self.user = User.objects.create_user(**self.credentials)

    def test_login_success(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass',
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful login

    def test_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'newpass',
            'password2': 'newpass',
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful registration

    def test_logout(self):
        # Log in first
        response = self.client.post(reverse('logout'))  # Ensure you're using the correct URL name
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after logout

    def test_login_failure(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  # Expecting to stay on login page
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_profile_update(self):
        self.client.login(**self.credentials)
        response = self.client.post(reverse('profile'), {
            'email': 'updated@example.com'
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful update
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'updated@example.com')

    def test_csrf_token_in_login_form(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'csrfmiddlewaretoken')
