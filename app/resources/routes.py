from .user import UsersApi, UserApi
from .auth import LoginApi


def initialize_routes(api):
    api.add_resource(UsersApi, '/api/users')
    api.add_resource(UserApi, '/api/users/<id>')
    api.add_resource(LoginApi,'/api/login')
