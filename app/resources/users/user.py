from flask import jsonify
from flask_restful import Resource

from database.db import mongo


class UsersApi(Resource):
    def get(self):
        users = mongo.db.users
        output = []
        for u in users.find():
            output.append({'email': u['email'], 'is_prof': u['is_prof']})
        return jsonify({'result': output})
