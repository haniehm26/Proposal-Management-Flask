from resources.profs.profs import ProfsApi
from resources.students.proposal_upload import ProposalUpload
from resources.students.student_guide_file import GetStudentGuideFile
from resources.students.student_proposal import SetProposalInfo
from .students import StudentsApi
from resources.users.user import UsersApi
from resources.users.auth import LoginApi, SignupApi
from resources.users.password_handler import ForgotPassword, ResetPassword
from .users.delete_account import DeleteAccount
from .users.edit_profile import EditProfileInfo


def initialize_routes(api):
    # USER API
    api.add_resource(UsersApi, '/api/users')
    api.add_resource(SignupApi, '/api/signup')
    api.add_resource(LoginApi, '/api/login')
    api.add_resource(EditProfileInfo, '/api/edit_profile_info')
    api.add_resource(DeleteAccount, '/api/delete_account')
    api.add_resource(ForgotPassword, '/api/forgot_password')
    api.add_resource(ResetPassword, '/api/reset_password')
    # STUDENT API
    api.add_resource(StudentsApi, '/api/students')
    api.add_resource(GetStudentGuideFile, '/api/get_student_guide_file')
    api.add_resource(SetProposalInfo, '/api/set_proposal_info')
    api.add_resource(ProposalUpload, '/api/proposal_upload')
    # PROF API
    api.add_resource(ProfsApi, '/api/profs')
