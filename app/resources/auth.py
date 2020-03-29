from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from database.models import User
import datetime


class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Invalid email or password'}, 401
        expires = datetime.timedelta(days=14)
        access_token = create_access_token(
            identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200
