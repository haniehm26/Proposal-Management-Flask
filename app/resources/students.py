from flask import jsonify
from flask_restful import Resource

from database.db import mongo


class StudentsApi(Resource):
    def get(self):
        students = mongo.db.students
        output = []
        for u in students.find():
            output.append(
                {'email': u['email'], 'password': u['password'], 'is_prof': u['is_prof'], 'first_name': u['first_name'],
                 'last_name': u['last_name']})
        return jsonify({'result': output})
