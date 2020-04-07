from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
from .choices import USER_TYPE, STUDENT_TYPE, PROFESSOR_GROUP, PROFESSOR_RESPONSIBILITIES, \
    PROFESSOR_STATUS, PROFESSOR_DEGREE, PROPOSAL_STATE, RESEARCH_TYPE, CHECKING_RESULT, \
    COUNCIL_FINAL_RESULT, DEFEND_DAY_RESULT


class User(db.Document):
    email = db.EmailField(required=True, unique=True, max_length=45, default="test@example.com")
    password = db.StringField(required=True, max_length=45, default="password")
    type = db.StringField(choices=USER_TYPE, required=True, max_length=1)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Student(db.Document):
    # state = db.IntField(required=True, max_length=1)
    s_id = db.IntField(required=True, unique=True, max_length=11, default=11111111)
    name = db.StringField(required=True, max_length=45, default="رضا")
    last_name = db.StringField(required=True, max_length=45, default="رضایی")
    entry_date = db.DateTimeField(required=True)
    field = db.StringField(required=True, max_length=45, default="مهندسی کامپیوتر")
    type = db.IntField(choices=STUDENT_TYPE, required=True, max_length=1)
    attitude = db.IntField(choices=PROFESSOR_GROUP, required=True, max_length=1)
    profile_pic = db.URLField(max_length=1000)
    # User.email


class Professor(db.Document):
    prof_id = db.IntField(required=True, unique=True, max_length=45, default=1111)
    name = db.StringField(required=True, max_length=45, default="حسین")
    last_name = db.StringField(required=True, max_length=45, default="حسینی")
    field = db.StringField(required=True, max_length=45, default="مهندسی کامپیوتر")
    expertise = db.StringField(required=True, max_length=45)
    responsibilities = db.IntField(choices=PROFESSOR_RESPONSIBILITIES, required=True, max_length=1)
    status = db.IntField(choices=PROFESSOR_STATUS, required=True, max_length=1)
    degree = db.IntField(choices=PROFESSOR_DEGREE, required=True, max_length=1)
    group = db.IntField(choices=PROFESSOR_GROUP, required=True, max_length=1)
    profile_pic = db.URLField(max_length=1000)
    # User.email


class DefendDay(db.Document):
    time = db.DateTimeField(required=True)
    judge_1_view = db.StringField(required=True)
    judge_2_view = db.StringField(required=True)
    result = db.IntField(choices=DEFEND_DAY_RESULT, required=True, max_length=1)
    # Proposal.id


class Proposal(db.Document):
    p_id = db.IntField(required=True, unique=True, max_length=11)
    year = db.IntField(required=True, max_length=4, default=1399)
    term = db.IntField(required=True, max_length=11)
    helper_prof_id = db.IntField(required=True, max_length=11)
    judge_1_id = db.IntField(required=True, max_length=11)
    judge_2_id = db.IntField(required=True, max_length=11)
    group = db.IntField(choices=PROFESSOR_GROUP, required=True, max_length=1)
    state = db.IntField(choices=PROPOSAL_STATE, required=True, max_length=1)
    # Student.id


class FreeTimes(db.Document):
    date = db.DateTimeField(required=True)
    start = db.DateTimeField(required=True)
    end = db.DateTimeField(required=True)
    # Professor.id


class Document(db.Document):
    title_persian = db.StringField(required=True, max_length=200, default="بهبود روش امتیازدهی ")
    title_english = db.StringField(required=True, max_length=200, default="Improving the method of scoring")
    keywords_persian = db.ListField(db.StringField(max_length=15), required=True)
    keywords_english = db.ListField(db.StringField(max_length=15), required=True)
    type = db.IntField(choices=RESEARCH_TYPE, required=True, max_length=1)
    introduction = db.FileField(required=True)
    how_to_solve = db.FileField(required=True)
    back_words = db.FileField(required=True)
    assumption = db.FileField(required=True)
    is_new = db.FileField(required=True)
    testing_tools = db.FileField(required=True)
    references = db.FileField(required=True)
    time_table = db.FileField(required=True)
    # Proposal.id


class Checking(db.Document):
    judge_1_view = db.StringField(required=True)
    judge_2_view = db.StringField(required=True)
    result = db.IntField(choices=CHECKING_RESULT, required=True, max_length=1)
    # Proposal.id


class Council(db.Document):
    result = db.IntField(choices=CHECKING_RESULT, required=True, max_length=1)
    final_result = db.IntField(choices=COUNCIL_FINAL_RESULT, required=True, max_length=1)
    # Proposal.id


class Modification(db.Document):
    judge_1_view = db.StringField(required=True)
    judge_2_view = db.StringField(required=True)
    result = db.IntField(choices=COUNCIL_FINAL_RESULT, required=True, max_length=1)
    # Proposal.id
