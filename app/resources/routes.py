from .user import UsersApi, UserApi
from .auth import LoginApi, SignupApi
from .password_handler import ForgotPassword, ResetPassword


def initialize_routes(api):
    api.add_resource(UsersApi, '/api/users')
    api.add_resource(UserApi, '/api/users/<id>')
    api.add_resource(SignupApi, '/api/signup')
    api.add_resource(LoginApi, '/api/login')
    api.add_resource(ForgotPassword, '/api/forgot_password')
    api.add_resource(ResetPassword, '/api/reset_password')
