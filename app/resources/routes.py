from .user import UsersApi, UserApi
from .auth import LoginApi
from .reset_password import ForgotPassword, ResetPassword


def initialize_routes(api):
    api.add_resource(UsersApi, '/api/users')
    api.add_resource(UserApi, '/api/users/<id>')
    api.add_resource(LoginApi, '/api/login')
    api.add_resource(ForgotPassword, '/api/auth/forgot')
    api.add_resource(ResetPassword, '/api/auth/reset')
