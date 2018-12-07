"""Create api version two blueprint."""
from flask import Blueprint

from flask_restful import Api

version_two = Blueprint('v1', __name__, url_prefix='/api/v2')

API = Api(version_two)

from app.api_2_0 import routes
