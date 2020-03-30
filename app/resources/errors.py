class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class UserNotExistsError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "UserNotExistsError": {
        "message": "User with given email doesn't exists",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid email or password",
        "status": 401
    }
}
