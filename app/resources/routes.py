from .profs import ProfsApi
from .student_guide_file import GetStudentGuideFile
from .student_proposal import SetStudentSupervisor, SetProposalGeneralInfo
from .students import StudentsApi
from resources.users.user import UsersApi, UserApi
from resources.users.auth import LoginApi, SignupApi
from resources.users.password_handler import ForgotPassword, ResetPassword


def initialize_routes(api):
    # USER API
    api.add_resource(UsersApi, '/api/users')
    api.add_resource(UserApi, '/api/users/<string:email>')
    api.add_resource(SignupApi, '/api/signup')
    api.add_resource(LoginApi, '/api/login')
    api.add_resource(ForgotPassword, '/api/forgot_password')
    api.add_resource(ResetPassword, '/api/reset_password')
    # STUDENT API
    api.add_resource(StudentsApi, '/api/students')
    api.add_resource(GetStudentGuideFile, '/api/get_student_guide_file')
    api.add_resource(SetStudentSupervisor, '/api/set_student_supervisor')
    api.add_resource(SetProposalGeneralInfo, '/api/set_proposal_general_info')
    # PROF API
    api.add_resource(ProfsApi, '/api/profs')
