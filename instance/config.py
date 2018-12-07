"""Contains configurations for the app."""

import os


class Config:
    """Contains the basic settings for all configurations."""

    debug = False
    SECRET_KEY = os.urandom(30)


class Development(Config):
    """Contains configurations to be used by developer."""

    DEBUG = True
    db = {
        "dbname": os.getenv('DATABASE_NAME'),
        "user": os.getenv('USER'),
        "password": os.getenv('PASSWORD'),
        "host": os.getenv('HOST'),
        "port": os.getenv('POSTRGRESPORT')
    }


class Testing(Config):
    """Contains configurations for testing."""

    TESTING = True
    db = {
        "dbname": os.getenv('TEST_DATABASE_NAME'),
        "user": os.getenv('USER'),
        "password": os.getenv('PASSWORD'),
        "host": os.getenv('HOST'),
        "port": os.getenv('POSTRGRESPORT')
    }


class Production(Config):
    """Contains configurations for production setting."""

    DEBUG = False


# Register the configurations
config = {
    'development': Development,
    'testing': Testing,
    'production': Production,
    'default': Development
}
