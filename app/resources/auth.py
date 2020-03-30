from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from database.models import User
import datetime
from mongoengine.errors import DoesNotExist
from resources.errors import InternalServerError, UnauthorizedError


class LoginApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User.objects.get(email=body.get('email'))
            authorized = user.check_password(body.get('password'))
            if not authorized:
                raise UnauthorizedError
            expires = datetime.timedelta(days=14)
            access_token = create_access_token(
                identity=str(user.id), expires_delta=expires)
            return {'token': access_token}, 200
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception:
            raise InternalServerError
