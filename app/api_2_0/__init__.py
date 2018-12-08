"""Create api version two blueprint."""
from flask import Blueprint

from flask_restful import Api

VERSION_TWO = Blueprint('v1', __name__, url_prefix='/api/v2')

API = Api(VERSION_TWO)

from app.api_2_0 import routes
