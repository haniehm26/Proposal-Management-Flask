from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
import datetime
from pymongo.errors import CursorNotFound

from database.hashing import check_password
from database.db import mongo
from resources.errors import InternalServerError, UnauthorizedError


class LoginApi(Resource):
    def post(self):
        try:
            users = mongo.db.users
            body = request.get_json()
            user = users.find_one({'email': body['email']})
            authorized = check_password(user['password'], body['password'])
            if not authorized:
                raise UnauthorizedError
            expires = datetime.timedelta(days=14)
            access_token = create_access_token(
                identity=user['email'], expires_delta=expires)
            return {'token': access_token}, 200
        except CursorNotFound:
            raise UnauthorizedError
