from flask import request, jsonify
from flask_restful import Resource
from pymongo.errors import CollectionInvalid

from database.hashing import hash_password
from database.db import mongo
from resources.errors import InternalServerError, EmailAlreadyExistsError, SchemaValidationError


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
                output = {'email': new_user['email'], 'is_prof': new_user['is_prof']}
                inbox = mongo.db.inbox
                inbox.insert({
                    'receiver': new_user['email'],
                    'sender': "",
                    'messages': []
                })
                if new_user['is_prof'] == 'false':
                    handle_student(new_user, body)
                else:
                    handle_prof(new_user, body)
            return jsonify({'result': output})
        except CollectionInvalid:
            raise SchemaValidationError
        except Exception:
            raise InternalServerError


def handle_student(new_user, body):
    students = mongo.db.students
    students.insert({
        'email': new_user['email'],
        'first_name': body.get('first_name'),
        'last_name': body.get('last_name'),
        'info_student_id': body.get('id'),
        'info_entry_date': " ",
        'info_field': " ",
        'info_attitude': " ",
        'info_profile_pic': " ",
        'info_state': " ",
        'proposal_year': " ",
        'proposal_semester': " ",
        'proposal_group': " ",
        'proposal_supervisor_prof_email': " ",
        'proposal_judge_1_email': " ",
        'proposal_judge_2_email': " ",
        'proposal_state': " ",
        'proposal_document_title_persian': " ",
        'proposal_document_title_english': " ",
        'proposal_document_keywords_persian': [],
        'proposal_document_keywords_english': [],
        'proposal_document_type': " ",
        'proposal_document_supportive_reference': " ",
        'proposal_document_how_to_solve': " ",
        'proposal_document_is_new': " ",
        'proposal_document_assumption': " ",
        'proposal_document_definition': " ",
        'proposal_document_history': " ",
        'proposal_document_tools': " ",
        'proposal_document_references': " ",
        'proposal_document_references_other_languages': " ",
        'proposal_document_time_table': " ",
        'proposal_checking_judge_1_opinion': " ",
        'proposal_checking_result': " ",
        'proposal_modification_judge_1_opinion': " ",
        'proposal_modification_judge_2_opinion': " ",
        'proposal_modification_result': " ",
        'proposal_defend_day_judge_1_opinion': " ",
        'proposal_defend_day_judge_2_opinion': " ",
        'proposal_defend_day_result': " ",
        'proposal_defend_day_time': " ",
        'proposal_council_result': " ",
        'proposal_council_final_result': " "
    })


def handle_prof(new_user, body):
    profs = mongo.db.profs
    profs.insert({
        'email': new_user['email'],
        'first_name': body.get('first_name'),
        'last_name': body.get('last_name'),
        'students_to_judge': [],
        'supervisor_of': [],
        'info_prof_id': body.get('id'),
        'info_rank': " ",
        'info_license': " ",
        'info_major': " ",
        'info_groups': " ",
        'info_field_of_study': " ",
        'info_profile_pic': " ",
        'info_responsibilities': " ",
        'free_times_dates': []
    })
