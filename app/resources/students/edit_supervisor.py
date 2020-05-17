from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flask import request, jsonify

from database.db import mongo
from resources.students.student_proposal import curr_user_is_student


class EditSupervisor(Resource):
    @jwt_required
    def post(self):
        output = "Error"
        current_user_email = get_jwt_identity()
        if curr_user_is_student(current_user_email):
            body = request.get_json()
            students = mongo.db.students
            student = students.find_one({'email': current_user_email})
            if student:
                before_supervisor = student['proposal_supervisor_prof_email']
                profs = mongo.db.profs
                before_supervisor_found = profs.find_one({'email': before_supervisor})
                if before_supervisor_found:
                    if before_supervisor_found['first_name'] != body.get('first_name') and \
                            before_supervisor_found['last_name'] != body.get('last_name'):
                        students_list = before_supervisor_found['supervisor_of']
                        for email in students_list:
                            if email == current_user_email:
                                students_list.remove(current_user_email)
                                profs.update({'email': before_supervisor_found['email']},
                                             {"$set": {'supervisor_of': students_list}})
                                output = "Successfully the current student email is removed from before supervisor list"
                            else:
                                output = "Current student email is not found in before supervisor list"
                    else:
                        output = "New supervisor is equal to before supervisor"
                else:
                    output = "Before supervisor not found"
                profs = mongo.db.profs
                new_supervisor = profs.find_one(
                    {'first_name': body.get('first_name'), 'last_name': body.get('last_name')})
                if new_supervisor:
                    if not new_supervisor['supervisor_of'].__contains__(current_user_email):
                        new_supervisor['supervisor_of'].append(current_user_email)
                        profs.update({'email': new_supervisor['email']},
                                     {"$set": {'supervisor_of': new_supervisor['supervisor_of']}})
                        students.update({'email': current_user_email},
                                        {"$set": {'proposal_supervisor_prof_email': new_supervisor['email']}})
                        out = "Editing supervisor is successfully done"
                    else:
                        out = "This student is already in supervisor list"
                else:
                    out = "New supervisor is not found"
            else:
                out = "Student not found"
        else:
            out = "It's prof"
        return jsonify({'out': out, 'output': output})
