from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flask import request, jsonify

from database.db import mongo
from resources.students.student_proposal import curr_user_is_student


class EditProposal(Resource):
    @jwt_required
    def post(self):
        current_user_email = get_jwt_identity()
        if curr_user_is_student(current_user_email):
            out = "It's student"
            body = request.get_json()
            students = mongo.db.students
            student = students.find_one({'email': current_user_email})
            if student:
                students.update({'email': student['email']},
                                {"$set": {
                                    'proposal_document_title_persian': body.get('title_persian'),
                                    'proposal_document_title_english': body.get('title_english'),
                                    'proposal_document_keywords_persian': body.get('keywords_persian'),
                                    'proposal_document_keywords_english': body.get('keywords_english'),
                                    'proposal_document_type': body.get('type'),
                                    'proposal_document_definition': body.get('definition'),
                                    'proposal_document_history': body.get('history'),
                                    'proposal_document_how_to_solve': body.get('how_to_solve'),
                                    'proposal_document_assumption': body.get('assumption'),
                                    'proposal_document_is_new': body.get('is_new'),
                                    'proposal_document_tools': body.get('tools'),
                                    'proposal_document_supportive_reference': body.get('supportive_reference'),
                                    'proposal_document_references': body.get('references'),
                                    'proposal_document_references_other_languages':
                                        body.get('references_other_languages'),
                                    'proposal_document_time_table': body.get('time_table')
                                }})
        else:
            out = "It's prof"
        return jsonify({'out': out})
