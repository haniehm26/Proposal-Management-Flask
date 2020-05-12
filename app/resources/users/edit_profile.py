from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from pymongo.errors import CursorNotFound, ConfigurationError

from resources.errors import InternalServerError, SchemaValidationError, UserNotExistsError
from database.db import mongo
from database.hashing import hash_password
from resources.students.student_proposal import curr_user_is_student


class EditProfileInfo(Resource):
    @jwt_required
    def post(self):
        try:
            current_user_email = get_jwt_identity()
            users = mongo.db.users
            found_user = users.find_one({'email': current_user_email})
            if found_user:
                body = request.get_json()
                password = hash_password(body['password'])
                output = users.update({'email': current_user_email},
                                      {"$set": {'email': body['email'],
                                                'password': password,
                                                'is_prof': body['is_prof']}
                                       })
                if curr_user_is_student(current_user_email):
                    students = mongo.db.students
                    student = students.find_one({'email': current_user_email})
                    students.update({'email': student['email']},
                                    {"$set": {'email': body['email'],
                                              'password': password,
                                              'is_prof': body['is_prof'],
                                              'first_name': body['first_name'],
                                              'last_name': body['last_name'],
                                              'info_student_id': body['id'],
                                              'info_entry_date': body['entry_date'],
                                              'info_field': body['field'],
                                              'info_attitude': body['attitude'],
                                              'info_profile_pic': body['profile_pic']
                                              }})
                else:
                    profs = mongo.db.profs
                    prof = profs.find_one({'email': current_user_email})
                    profs.update({'email': prof['email']},
                                 {"$set": {'email': body['email'],
                                           'password': password,
                                           'is_prof': body['is_prof'],
                                           'first_name': body['first_name'],
                                           'last_name': body['last_name'],
                                           'info_prof_id': body['id'],
                                           'info_rank': body['rank'],
                                           'info_license': body['license'],
                                           'info_major': body['major'],
                                           'info_groups': body['groups'],
                                           'info_field_of_study': body['field_of_study'],
                                           'info_profile_pic': body['profile_pic'],
                                           'info_responsibilities': body['responsibilities']
                                           }})
            else:
                raise UserNotExistsError
            return jsonify(output)

        except ConfigurationError:
            raise SchemaValidationError
        except CursorNotFound:
            raise UserNotExistsError
        except Exception:
            raise InternalServerError
