from flask import jsonify
from flask_restful import Resource

from database.db import mongo


class StudentsApi(Resource):
    def get(self):
        students = mongo.db.students
        output = []
        for u in students.find():
            output.append({
                'email': u['email'],
                'first_name': u['first_name'],
                'last_name': u['last_name'],
                'id': u['info_student_id'],
                'proposal_supervisor_prof_email': u['proposal_supervisor_prof_email']
            })
        return jsonify({'result': output})
