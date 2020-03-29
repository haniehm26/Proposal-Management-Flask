from flask import Response, request
from database.models import User
from flask_restful import Resource
from flask_jwt_extended import jwt_required


class UsersApi(Resource):
    def get(self):
        users = User.objects().to_json()
        return Response(users, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 200


class UserApi(Resource):
    @jwt_required
    def put(self, id):
        body = request.get_json()
        User.objects.get(id=id).update(**body)
        return '', 200

    @jwt_required
    def delete(self, id):
        user = User.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        users = User.objects.get(id=id).to_json()
        return Response(users, mimetype="application/json", status=200)
