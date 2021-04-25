class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class UsersDataAlreadyExistsError(Exception):
    pass

class UpdatingUsersDataError(Exception):
    pass

class DeletingUsersDataError(Exception):
    pass

class UsersDataNotExistsError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

class BadTokenError(Exception):
    pass

class EmailDoesnotExistsError(Exception):
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
     "UsersDataAlreadyExistsError": {
         "message": "data with given name already exists",
         "status": 400
     },
     "UpdatingUsersDataError": {
         "message": "Updating data added by other is forbidden",
         "status": 403
     },
     "DeletingUsersDataError": {
         "message": "Deleting data added by other is forbidden",
         "status": 403
     },
     "UsersDataNotExistsError": {
         "message": "data with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     },
     "EmailDoesnotExistsError": {
         "message": "Couldn't find the user with given email address",
         "status": 400
     },
     "BadTokenError": {
         "message": "Invalid token",
         "status": 403
      }
}