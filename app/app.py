from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail

from resources.errors import errors
from database.db import initialize_db

app = Flask(__name__)

# for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.
# (Use this when calling APIs from front-end browser)
CORS(app)

# Windows: Type in this command in 'cmd', before running the project
# $ set ENV_FILE_LOCATION=./.env
# 'ENV_FILE_LOCATION' stands for the relative location of '.env' file in Server directory
app.config.from_envvar('ENV_FILE_LOCATION')

# this is for mail service, used in forgot and reset password.
mail = Mail(app)

# because of circular import it is imported here.
# do not change it.
from resources.routes import initialize_routes

# some errors are defined in app/resources/error.py, set here
api = Api(app, errors=errors)

# this is used to generate hashed passwords
bcrypt = Bcrypt(app)

# this is used for generate user token
jwt = JWTManager(app)

# definition of database
app.config['MONGO_DBNAME'] = 'proposal-management'
app.config['MONGO_URI'] = 'mongodb://localhost/proposal-management'
initialize_db(app)

# initialize api routes
initialize_routes(api)
