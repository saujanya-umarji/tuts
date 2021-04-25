from flask import Response, request,jsonify,json,render_template
from flask_jwt_extended import create_access_token,jwt_required
from backend.models import UsersData
from flask_restful import Resource
import datetime
import os
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from backend.errors import SchemaValidationError, UsersDataAlreadyExistsError, InternalServerError, EmailDoesnotExistsError,UpdatingUsersDataError, DeletingUsersDataError, UsersDataNotExistsError
from services.mail_services import send_email 
from services.sms_services import send_sms





class LoginApi(Resource):
    def post(self):
            try:
                body = request.get_json()
                email=body.get("email")
                print(email)
                users = UsersData.objects.get(email=email)
                #users = UsersData.objects.get(email=body.get('email'))
                print(jsonify(users))
                authorized = users.check_password(body.get('password'))
                if not authorized:
                    return {'error': 'Email or password invalid'}, 401
                else:
                    print("login successful")
                
                print(os.urandom(16))
                expires = datetime.timedelta(days=7)
                access_token = create_access_token(identity=str(users.id), expires_delta=expires)
                send_email('tuts application login',recipients=[email],text_body='this mail is sent by saujanya from tuts application!! thenk you for joining our team!',html_body="""<html><head><title>tuts mail services</title></head><body><p>tuts mail is working</p></body></html>""")
                sms = send_sms()
                print("sms printed!!!")
                return {'token': access_token}, 200
            except (FieldDoesNotExist,ValidationError):
                raise SchemaValidationError
            except NotUniqueError:
                raise UsersDataAlreadyExistsError
            except EmailDoesnotExistsError:
                raise EmailDoesnotExistsError
            except Exception:
                raise InternalServerError
        

class ForgotPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'
        try:
            body = request.get_json()
            email=body.get("email")
            print(email)
            if not email:
                raise SchemaValidationError
            users = UsersData.objects.get(email=email)
            if not users:
                raise EmailDoesnotExistsError
            expires = datetime.timedelta(hours=24)
            reset_token = create_access_token(identity=str(users.id), expires_delta=expires)
            return send_email('tuts application login',recipients=[email],text_body='this mail is sent by saujanya from tuts application!! your password reset can be done !',html_body="""<html><head><title>tuts mail services</title></head><body><p>tuts mail is working</p></body></html>""")
        except SchemaValidationError:
            raise SchemaValidationError
        except EmailDoesnotExistsError:
            raise EmailDoesnotExistsError
        except Exception as e:
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

            user_id = decode_token(reset_token)['identity']

            users= User.objects.get(id=user_id)

            users.modify(password=password)
            users.hash_password()
            users.save()

            return send_email('[tuts] Password reset successful',
                              recipients=[users.email],
                              text_body='Password reset was successful',
                              html_body='<p>Password reset was successful</p>')

        except SchemaValidationError:
            raise SchemaValidationError
        except ExpiredSignatureError:
            raise ExpiredTokenError
        except (DecodeError, InvalidTokenError):
            raise BadTokenError
        except Exception as e:
            raise InternalServerError

