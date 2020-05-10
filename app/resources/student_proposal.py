from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flask import request, jsonify

from database.db import mongo


class SetStudentSupervisor(Resource):
    @jwt_required
    def post(self):
        current_user_email = get_jwt_identity()
        users = mongo.db.users
        user = users.find_one({'email': current_user_email})
        output = "None"
        if user['is_prof'] == 'false':
            out = "It's student"
            body = request.get_json()
            supervisor_first_name = body.get('first_name')
            supervisor_last_name = body.get('last_name')
            profs = mongo.db.profs
            supervisor = profs.find_one({'first_name': supervisor_first_name, 'last_name': supervisor_last_name})
            if supervisor:
                output = "Supervisor found"
                supervisor['supervisor_of'].append(current_user_email)
                profs.update({'email': supervisor['email']}, {"$set": {'supervisor_of': supervisor['supervisor_of']}})
                students = mongo.db.students
                student = students.find_one({'email': current_user_email})
                students.update({'email': student['email']},
                                {"$set": {'proposal_supervisor_prof_email': supervisor['email']}})
            else:
                output = "Supervisor not found"
        else:
            out = "It's prof"
        return jsonify({'out': out, 'output': output})


class SetProposalGeneralInfo(Resource):
    @jwt_required
    def post(self):
        current_user_email = get_jwt_identity()
        users = mongo.db.users
        user = users.find_one({'email': current_user_email})
        if user['is_prof'] == 'false':
            out = "It's student"
            body = request.get_json()
            proposal_document_title_persian = body.get('title_persian')
            proposal_document_title_english = body.get('title_english')
            proposal_document_keywords_persian = body.get('keywords_persian')
            proposal_document_keywords_english = body.get('keywords_english')
            proposal_document_type = body.get('type')
            students = mongo.db.students
            student = students.find_one({'email': current_user_email})
            students.update({'email': student['email']},
                            {"$set": {
                                'proposal_document_title_persian': proposal_document_title_persian,
                                'proposal_document_title_english': proposal_document_title_english,
                                'proposal_document_keywords_persian': proposal_document_keywords_persian,
                                'proposal_document_keywords_english': proposal_document_keywords_english,
                                'proposal_document_type': proposal_document_type
                            }})
            print(student)
        else:
            out = "It's prof"
        return jsonify({'out': out})

