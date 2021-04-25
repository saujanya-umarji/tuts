from flask import Flask
from flask_bcrypt import Bcrypt
from os import environ
from flask_jwt_extended import JWTManager
from backend.db import initialize_db
from flask_restful import Api
from backend.errors import errors
from flask_mail import Mail,Message

app = Flask(__name__)
app.config.from_pyfile('config.py')
mail = Mail(app)

from backend.router import initialize_routes
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/tuts?readPreference=primary&appname=MongoDB%20Compass&ssl=false'
}

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'saujanyapumarji@gmail.com'
# app.config['MAIL_PASSWORD'] = 'GoldaUmarji@97'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True


initialize_db(app)
initialize_routes(api)



