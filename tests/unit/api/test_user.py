"""Contains tests for the user."""

from unittest import TestCase as TC

from app import create_app

from manage import drop_tables

from instance.config import config


class TestUser(TC):
    """Test user endpoints."""

    def setUp(self):
        """Initialize variables for testing."""
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.user = {
            "Email": "pndungu54@gmail.com",
            "Password": "pass1234",
            "Confirm Password": "pass1234"
        }

    def tearDown(self):
        """Clear data after use."""
        drop_tables(config['testing'].db)

    def test_create_user_with_valid_data_success(self):
        """Register a user with valid data."""
        res = self.client().post('/api/v2/auth/signup', data=self.user)
        self.assertEqual(res.status_code, 201)
        res = res.get_json()

        self.assertEqual(res['data']['message'],
                         'You have successfuly signed up')

    def test_signup_with_invalid_email_false(self):
        """Test email is valid."""
        user = {
            "Email": "user.com",
            "Password": "pass1234",
            "Confirm Password": "pass1234"
        }
        res = self.client().post('/api/v2/auth/signup', data=user)
        self.assertEqual(res.status_code, 400)
        res = res.get_json()
        self.assertEqual(res['error'][0],
                         'Invalid Email Address')

    def test_signup_user_with_short_password_false(self):
        """Test password is long enough."""
        user = {
            "Email": "user@example.com",
            "Password": "pass",
            "Confirm Password": "pass"
        }
        res = self.client().post('/api/v2/auth/signup', data=user)
        self.assertEqual(res.status_code, 400)
        res = res.get_json()
        self.assertEqual(res['error'][0],
                         'Password should be atleast eight characters')

    def test_signup_user_with_mistmatching_passwords_false(self):
        """Test passwords match."""
        user = {
            "Email": "user@example.com",
            "Password": "pass1234",
            "Confirm Password": "pass5678"
        }
        res = self.client().post('/api/v2/auth/signup', data=user)
        self.assertEqual(res.status_code, 400)
        res = res.get_json()
        self.assertEqual(res['error'][0],
                         'Passwords should match')

    def test_multiple_signup_false(self):
        """Test user cannot register more than once."""
        res = self.client().post('/api/v2/auth/signup', data=self.user)
        self.assertEqual(res.status_code, 201)
        res = self.client().post('/api/v2/auth/signup', data=self.user)
        self.assertEqual(res.status_code, 400)
        res = res.get_json()
        self.assertEqual(res['error'][0], 'That email is already taken')

    def test_signup_with_blank_email_false(self):
        """Test email is present."""
        user = {
            "Email": "",
            "Password": "pass1234",
            "Confirm Password": "pass1234"
        }
        res = self.client().post('/api/v2/auth/signup', data=user)
        self.assertEqual(res.status_code, 400)
        res = res.get_json()
        self.assertEqual(res['error'][0],
                         'Email should not be blank')

    def test_signup_with_blank_password_false(self):
        """Test password is present."""
        user = {
            "Email": "a@g.com",
            "Password": "",
            "Confirm Password": "pass5678"
        }
        res = self.client().post('/api/v2/auth/signup', data=user)
        self.assertEqual(res.status_code, 400)
        res = res.get_json()
        self.assertEqual(res['error'][0],
                         'Password should not be blank')
