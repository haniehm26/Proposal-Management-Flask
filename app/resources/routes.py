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
    # USER API------------------------------------------------------------------------------------- #

    # input: {}
    # output: list of users 'email' & 'is_prof'
    api.add_resource(UsersApi, '/api/users')  # get

    # input: (required): {
    #                      "email" : "hanieh@mahdavi.com",
    #                      "password" : "1234567890",
    #                      "is_prof" : "false"
    #                      "first_name" : "hanieh",
    #                      "last_name" : "mahdavi",
    #                      "id" : "96243067"
    #                    }
    # output: creates new user
    api.add_resource(SignupApi, '/api/signup')  # post

    # input: {
    #         "email" : "hanieh@mahdavi.com",
    #         "password" : "1234567890"
    #        }
    # output: 'token'
    api.add_resource(LoginApi, '/api/login')  # post

    # if user is STUDENT:
    # these fields are optional
    # input: {
    #          "email" : "hanieh@mahdavi.com",
    #          "password" : "1234567890",
    #          "is_prof" : "false",
    #          "first_name" : "hanieh",
    #          "last_name" : "mahdavi",
    #          "id" : "96243067",
    #          "entry_date" : "1396",
    #          "field" : "مهندسی کامپیوتر",
    #          "attitude" : CHOICES -> GROUP,
    #          "profile_pic" : ""
    #        }
    #
    # if user is PROF:
    # these fields are optional
    # input: {
    #          "email" : "alireza@shameli.com",
    #          "password" : "1234567890",
    #          "is_prof" : "true",
    #          "first_name" : "alireza",
    #          "last_name" : "shameli",
    #          "id" : "12345",
    #          "rank" : CHOICES -> PROFESSOR_STATUS,
    #          "field_of_study" : CHOICES -> GROUP,
    #          "responsibilities" : CHOICES -> PROFESSOR_RESPONSIBILITIES,
    #          "profile_pic" : ""
    #        }
    api.add_resource(EditProfileInfo, '/api/edit_profile_info')  # post

    # deletes the access of user
    # input: {
    #          "password" : "1234567890"
    #        }
    api.add_resource(DeleteAccount, '/api/delete_account')  # post

    # input: {
    #          "email" : "hanieh@mahdavi.com"
    #        }
    # output: token for reset password
    api.add_resource(ForgotPassword, '/api/forgot_password')  # post

    # input: {
    #          "reset_token" : the token from forgot password,
    #          "password" : new password
    #        }
    api.add_resource(ResetPassword, '/api/reset_password')  # post

    # input: {}
    # output: returns current user email (it is not used in project)
    api.add_resource(GetCurrUser, '/api/get_curr_user')  # get

    # STUDENT API------------------------------------------------------------------------------------- #

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
