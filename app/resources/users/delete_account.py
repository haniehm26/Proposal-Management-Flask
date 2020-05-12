from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from pymongo.errors import CursorNotFound

from resources.errors import InternalServerError, UserNotExistsError
from database.db import mongo
from resources.students.student_proposal import curr_user_is_student


class DeleteAccount(Resource):
    @jwt_required
    def delete(self):
        try:
            current_user_email = get_jwt_identity()
            users = mongo.db.users
            users.delete_one({'email': current_user_email})
            if curr_user_is_student(current_user_email):
                students = mongo.db.students
                students.delete_one({'email': current_user_email})
            else:
                profs = mongo.db.profs
                profs.delete_one({'email': current_user_email})
            return ''
        except CursorNotFound:
            raise UserNotExistsError
        except Exception:
            raise InternalServerError
