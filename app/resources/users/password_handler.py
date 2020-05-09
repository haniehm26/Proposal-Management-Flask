from flask import request, render_template
from flask_jwt_extended import create_access_token, decode_token
from flask_restful import Resource
import datetime
from jwt.exceptions import ExpiredSignatureError, DecodeError, \
    InvalidTokenError

from database.checking import hash_password
from database.db import mongo
from .errors import SchemaValidationError, InternalServerError, \
    EmailDoesNotExistsError, BadTokenError, ExpiredTokenError
from services.mail_service import send_email


class ForgotPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'
        try:
            body = request.get_json()
            email = body.get('email')
            if not email:
                raise SchemaValidationError
            users = mongo.db.users
            user_found = users.find_one({'email': email})
            if not user_found:
                raise EmailDoesNotExistsError

            expires = datetime.timedelta(hours=24)
            reset_token = create_access_token(
                email, expires_delta=expires)

            return send_email('[Proposal-Management] Reset Your Password',
                              sender='support@proposal-management.com',
                              recipients=[email],
                              text_body=render_template(
                                  'email/reset_password.txt', url=url + reset_token),
                              html_body=render_template('email/reset_password.html', url=url + reset_token))
        except SchemaValidationError:
            raise SchemaValidationError
        except EmailDoesNotExistsError:
            raise EmailDoesNotExistsError
        except Exception:
            raise InternalServerError


class ResetPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'
        try:
            body = request.get_json()
            reset_token = body.get('reset_token')
            password = body.get('password')

            if not reset_token or not password:
                raise SchemaValidationError

            user_email = decode_token(reset_token)['identity']

            users = mongo.db.users
            hashed_password = hash_password(body['password'])
            output = users.update({'email': user_email}, {'password': hashed_password})
            return send_email('[Proposal-Management] Password reset successful',
                              sender='support@proposal-management.com',
                              recipients=[user_email],
                              text_body='Password reset was successful',
                              html_body='<p>Password reset was successful</p>')

        except SchemaValidationError:
            raise SchemaValidationError
        except ExpiredSignatureError:
            raise ExpiredTokenError
        except (DecodeError, InvalidTokenError):
            raise BadTokenError
        except Exception:
            raise InternalServerError
