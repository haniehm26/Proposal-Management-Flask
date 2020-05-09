from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token
import datetime
from pymongo.errors import CursorNotFound, CollectionInvalid

from database.checking import hash_password, check_password
from database.db import mongo
from .errors import InternalServerError, UnauthorizedError, EmailAlreadyExistsError, SchemaValidationError


class SignupApi(Resource):
    def post(self):
        try:
            users = mongo.db.users
            body = request.get_json()
            user_found = users.find_one({'email': body['email']})
            if user_found:
                raise EmailAlreadyExistsError
            else:
                password = hash_password(body['password'])
                user_id = users.insert({'email': body['email'], 'password': password, 'is_prof': body['is_prof']})
                new_user = users.find_one({'_id': user_id})
                output = {'email': new_user['email'], 'password': new_user['password'], 'is_prof': new_user['is_prof']}
                if new_user['is_prof'] == 'false':
                    students = mongo.db.students
                    students.insert(
                        {'email': new_user['email'], 'password': new_user['password'], 'is_prof': new_user['is_prof']})
                else:
                    profs = mongo.db.profs
                    profs.insert(
                        {'email': new_user['email'], 'password': new_user['password'], 'is_prof': new_user['is_prof']})
            return jsonify({'result': output})
        except CollectionInvalid:
            raise SchemaValidationError
        except Exception:
            raise InternalServerError


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
        except Exception:
            raise InternalServerError
