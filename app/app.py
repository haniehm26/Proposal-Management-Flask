from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail

from admin.admin import initialize_admin, AdminViews
from resources.errors import errors
from database.db import initialize_db

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

initialize_admin(app)
AdminViews

mail = Mail(app)

from resources.routes import initialize_routes

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/proposal-management'}

initialize_db(app)
initialize_routes(api)
