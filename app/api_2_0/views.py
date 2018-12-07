"""Api endpoint implementation."""
from flask_restful import Resource, reqparse

from app.api_2_0.models import User

from app.api_2_0.utils.errors import bad_request


class Signup(Resource):
    """Register user."""

    def post(self):
        """Create user."""
        parser = reqparse.RequestParser()
        parser.add_argument('Email',
                            type=str,
                            help='Email is required',
                            required=True)
        parser.add_argument('Password',
                            type=str,
                            help='Password is required',
                            required=True)
        parser.add_argument('Confirm Password',
                            type=str,
                            help='Confirm Password is required',
                            required=True)
        args = parser.parse_args()

        user = User(args['Email'], args['Password'], args['Confirm Password'])
        res = user.save()
        if res.get('status'):
            return {'data': {'message': res.get('message'),
                             'status': 201}}, 201
        return bad_request(user.errors)
