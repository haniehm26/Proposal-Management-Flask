from flask_admin.contrib.mongoengine import ModelView

from database.models import User, Student
from app import admin


class AdminViews(ModelView):
    admin.add_view(ModelView(User))
    admin.add_view(ModelView(Student))
