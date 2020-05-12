from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource


class GetCurrUser(Resource):
    @jwt_required
    def get(self):
        current_user_email = get_jwt_identity()
        return current_user_email
