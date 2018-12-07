"""Contains classes to model app data."""

from datetime import datetime

import psycopg2

from flask_bcrypt import Bcrypt

from manage import db_connection

from app.api_2_0.utils.validators import UserValidator

BCRYPT = Bcrypt()

class User(UserValidator):
    """Class to manage user data."""

    def __init__(self, email, password, confirm_pass):
        """Initialize user."""
        super().__init__()
        self.password = password
        self.email = email
        self.confirm_pass = confirm_pass
        self.date_created = datetime.now()
        self.is_admin = False
        self.connection = db_connection['connection']

    def save(self):
        """Add user to database."""
        if self.find_user(self.email)['status']:
            return {'status': False,
                    'message': self.errors.
                               append('That email is already taken')}
        if self.validate_password(self.password):
            if self.match_password(self.password, self.confirm_pass):
                if self.validate_email(self.email):
                    try:
                        cursor = self.connection.cursor()
                        user_query = "INSERT INTO users (email,\
                                                        user_password,\
                                                        date_created,\
                                                        is_admin)\
                                    VALUES ('{}', '{}', '{}', '{}')".\
                                            format(self.email,
                                                   self.encrypt_password(self.password),
                                                   self.date_created,
                                                   self.is_admin)
                        cursor.execute(user_query)
                        self.connection.commit()
                        return {'status': True,
                                'message': "You have successfuly signed up"}
                    except Exception as e:
                        return {'Status': False, 'message': '{}'.format(e)}
                return {'status': False, 'message': self.errors}
            return {'status': False, 'message': self.errors}
        return {'status': False, 'message': self.errors}

    def find_user(self, email):
        """Find user in db."""
        query = "SELECT * FROM users WHERE email='{}'".format(email)
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows:
                return {'status': True, 'message': rows}
            return {'status': False, 'message': 'That user does not exist'}
        except (Exception, psycopg2.DatabaseError) as error:
            return {'status': False, 'message': error}

    def encrypt_password(self, password):
        """Encrypt the password"""
        self.password = BCRYPT.generate_password_hash(password)
