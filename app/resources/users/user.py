from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from pymongo.errors import CollectionInvalid, CursorNotFound, \
    InvalidName, ConfigurationError

from resources.errors import InternalServerError, SchemaValidationError, UserNotExistsError, EmailAlreadyExistsError
from database.db import mongo
from database.checking import hash_password


class UsersApi(Resource):
    def get(self):
        users = mongo.db.users
        output = []
        for u in users.find():
            output.append({'email': u['email'], 'password': u['password'], 'is_prof': u['is_prof']})
        return jsonify({'result': output})

    @jwt_required
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
            return jsonify({'result': output})
        except (CollectionInvalid, InvalidName):
            raise SchemaValidationError
        except Exception:
            raise InternalServerError


class UserApi(Resource):
    @jwt_required
    def put(self, email):
        try:
            users = mongo.db.users
            body = request.get_json()
            password = hash_password(body['password'])
            output = users.update({'email': email}, {"$set": {'email': body['email'], 'password': password,
                                                              'is_prof': body['is_prof']}})
            return jsonify(output)
        except ConfigurationError:
            raise SchemaValidationError
        except CursorNotFound:
            raise UserNotExistsError
        except Exception:
            raise InternalServerError

    @jwt_required
    def delete(self, email):
        try:
            users = mongo.db.users
            output = users.delete_one({'email': email})
            return ''
        except CursorNotFound:
            raise UserNotExistsError
        except Exception:
            raise InternalServerError

    def get(self, email):
        try:
            users = mongo.db.users
            user_found = users.find_one({'email': email})
            if user_found:
                output = {'email': user_found['email'], 'password': user_found['password'],
                          'is_prof': user_found['is_prof']}
            else:
                output = "No such element"
            return jsonify({'result': output})
        except CursorNotFound:
            raise UserNotExistsError
        except Exception:
            raise InternalServerError
