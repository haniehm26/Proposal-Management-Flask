from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail

from resources.errors import errors
from database.db import initialize_db

app = Flask(__name__)

# use this before running project in windows
# set ENV_FILE_LOCATION=./.env
app.config.from_envvar('ENV_FILE_LOCATION')
# -------------------------------------------------------------- #

# this is for mail service, used in forgot and reset password.
mail = Mail(app)
# -------------------------------------------------------------- #

# because of circular import it is imported here.
# do not change it.
from resources.routes import initialize_routes
# -------------------------------------------------------------- #

# some errors are defined in app/resources/error.py, set here
api = Api(app, errors=errors)
# -------------------------------------------------------------- #

bcrypt = Bcrypt(app)

# this is used for generate user token
jwt = JWTManager(app)
# -------------------------------------------------------------- #

# definition of database
app.config['MONGO_DBNAME'] = 'proposal-management'
app.config['MONGO_URI'] = 'mongodb://localhost/proposal-management'
initialize_db(app)
# -------------------------------------------------------------- #

initialize_routes(api)
