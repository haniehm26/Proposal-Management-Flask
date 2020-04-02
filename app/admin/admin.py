from flask_admin.contrib.mongoengine import ModelView
from database.models import User
from app import admin


class AdminViews(ModelView):
    admin.add_view(ModelView(User))
