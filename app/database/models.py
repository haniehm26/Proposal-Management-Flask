from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Student(db.Document):
    student_id = db.IntField(required=True, unique=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    entry_date = db.DateTimeField(required=True)
    field = db.StringField(required=True)
    profile_pic = db.URLField()


# class Professor(db.Document):
#     professor_id = db.IntField(required=True, unique=True)
#     first_name = db.StringField(required=True)
#     last_name = db.StringField(required=True)
#     field = db.StringField(required=True)
#     profile_pic = db.URLField()
