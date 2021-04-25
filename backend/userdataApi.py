from flask import Response, request,jsonify,json
from flask_jwt_extended import create_access_token,jwt_required
from backend.models import UsersData
from flask_restful import Resource
import datetime
import os
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from backend.errors import SchemaValidationError, UsersDataAlreadyExistsError, InternalServerError, EmailDoesnotExistsError,UpdatingUsersDataError, DeletingUsersDataError, UsersDataNotExistsError
from services.mail_services import send_email


class UserApi(Resource):

  @jwt_required()
  def get(self):
    try:
      users = UsersData.objects().to_json()
      return Response(users, mimetype="application/json", status=200)
    except Exception:
      raise InternalServerError
    

  @jwt_required()
  def post(self):
    try:
      body = request.get_json()
      users = UsersData(**body)
      users.hash_password()
      users.save()
      id = users.userid
      return {'id': str(id)}, 200
    except (FieldDoesNotExist, ValidationError):   
      raise SchemaValidationError
    except NotUniqueError:
      raise UsersDataAlreadyExistsError
    except Exception as e:
      raise InternalServerError
 

class UsersApi(Resource):
  @jwt_required()
  def put(self, id):
    try:
      body = request.get_json()
      UsersData.objects.get(id=id).update(**body)
      return '', 200
    except InvalidQueryError:
      raise SchemaValidationError
    except DoesNotExist:
      raise UpdatingUsersDataError
    except Exception:
      raise InternalServerError
 

  @jwt_required()
  def delete(self, id):
    try:
      users = UsersData.objects.get(id=id).delete()
      return '', 200
    except DoesNotExist:
      raise DeletingUsersDataError
    except Exception:
      raise InternalServerError


  @jwt_required()
  def get(self, id):
    try:
      users = UsersData.objects.get(id=id).to_json()
      return Response(users, mimetype="application/json", status=200)
    except DoesNotExist:
      raise UsersDataNotExistsError
    except Exception:
      raise InternalServerError


# class LoginApi(Resource):
#   def post(self):
#     try:
#       body = request.get_json()
#       email=body.get("email")
#       print(email)
#       users = UsersData.objects.get(email=email)
#       #users = UsersData.objects.get(email=body.get('email'))
#       print(jsonify(users))
#       authorized = users.check_password(body.get('password'))
#       if not authorized:
#         return {'error': 'Email or password invalid'}, 401
#       else:
#         print("login successful")
      
#       print(os.urandom(16))
#       expires = datetime.timedelta(days=7)
#       access_token = create_access_token(identity=str(users.id), expires_delta=expires)
#       send_email('tuts application login',recipients=[email],text_body='this mail is sent by saujanya from tuts application!! thenk you for joining our team!',html_body="""<html><head><title>tuts mail services</title></head><body><p>tuts mail is working</p></body></html>""")
#       sms = send_sms()
#       print("sms printed!!!")
#       return {'token': access_token}, 200
#     except (FieldDoesNotExist,ValidationError):
#       raise SchemaValidationError
#     except NotUniqueError:
#       raise UsersDataAlreadyExistsError
#     except EmailDoesnotExistsError:
#       raise EmailDoesnotExistsError
#     except Exception:
#       raise InternalServerError