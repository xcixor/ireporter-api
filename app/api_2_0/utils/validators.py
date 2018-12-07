"""Custom model validators."""

from app.api_2_0.utils.utils import is_email, is_empty, is_valid_password


class UserValidator():
    """Validate user fields."""

    def __init__(self):
        """Initialize validator with empty errors list."""
        self.errors = []

    def validate_email(self, email):
        """Validate email."""
        if not is_empty(email):
            if is_email(email):
                return True
            self.errors.append('Invalid Email Address')
            return False
        self.errors.append("Email should not be blank")
        return False

    def validate_password(self, password):
        """Validate password."""
        if not is_empty(password):
            if is_valid_password(password):
                return True
            self.errors.append("Password should be atleast eight characters")
            return False
        self.errors.append("Password should not be blank")
        return False

    def match_password(self, password, confirm_passowrd):
        """Match passwords."""
        if password == confirm_passowrd:
            return True
        self.errors.append("Passwords should match")
        return False
