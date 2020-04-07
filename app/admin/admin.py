from flask_admin.contrib.mongoengine import ModelView

from database.models import User, Student, Professor, DefendDay, Proposal, FreeTimes, \
    Document, Checking, Council, Modification
from app import admin


class AdminViews(ModelView):
    admin.add_view(ModelView(User))
    admin.add_view(ModelView(Student))
    admin.add_view(ModelView(Professor))
    admin.add_view(ModelView(DefendDay))
    admin.add_view(ModelView(Proposal))
    admin.add_view(ModelView(FreeTimes))
    admin.add_view(ModelView(Document))
    admin.add_view(ModelView(Checking))
    admin.add_view(ModelView(Council))
    admin.add_view(ModelView(Modification))
