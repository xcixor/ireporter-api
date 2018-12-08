"""Defines the routes of the api."""

from app.api_2_0 import API as api

from app.api_2_0 import views

api.add_resource(views.Signup, '/auth/signup')
