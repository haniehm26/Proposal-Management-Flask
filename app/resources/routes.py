from resources.profs.profs import ProfsApi
from resources.students.proposal_upload import ProposalUpload
from resources.students.student_guide_file import GetStudentGuideFile
from resources.students.student_proposal import SetProposalInfo
from resources.students.students import StudentsApi
from resources.users.user import UsersApi
from resources.users.sign_up import SignupApi
from resources.users.password_handler import ForgotPassword, ResetPassword
from resources.todo_list.inbox import InboxApi
from .students.edit_proposal import EditProposal
from .students.edit_supervisor import EditSupervisor
from .todo_list.send_message import SendNewMessage
from .users.delete_account import DeleteAccount
from .users.edit_profile import EditProfileInfo
from .users.get_curr_user import GetCurrUser
from .users.login import LoginApi


def initialize_routes(api):
    # USER API
    api.add_resource(UsersApi, '/api/users')  # get
    api.add_resource(SignupApi, '/api/signup')  # post
    api.add_resource(LoginApi, '/api/login')  # post
    api.add_resource(EditProfileInfo, '/api/edit_profile_info')  # post
    api.add_resource(DeleteAccount, '/api/delete_account')  # post
    api.add_resource(ForgotPassword, '/api/forgot_password')  # post
    api.add_resource(ResetPassword, '/api/reset_password')  # post
    api.add_resource(GetCurrUser, '/api/get_curr_user')  # get
    # STUDENT API
    api.add_resource(StudentsApi, '/api/students')  # get
    api.add_resource(GetStudentGuideFile, '/api/get_student_guide_file')  # get
    api.add_resource(SetProposalInfo, '/api/set_proposal_info')  # post
    api.add_resource(ProposalUpload, '/api/proposal_upload')  # post
    api.add_resource(EditProposal, '/api/edit_proposal')  # post
    api.add_resource(EditSupervisor, '/api/edit_supervisor')  # post
    # PROF API
    api.add_resource(ProfsApi, '/api/profs')  # get
    # TODO_LIST API
    api.add_resource(InboxApi, '/api/inbox')  # get
    api.add_resource(SendNewMessage, '/api/send_new_message')  # post
