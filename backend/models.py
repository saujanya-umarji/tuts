from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class UsersData(db.Document):
    userid = db.StringField(required=True, unique=True)
    name = db.StringField(required=True, max_length=70)
    age = db.StringField(required=True, max_length=70)
    username = db.StringField(required=True, max_length=70)
    phone = db.StringField(required=True, max_length=70)
    password = db.StringField(required=True, max_length=70)
    email = db.StringField(required=True, max_length=70,unique=True)
    userbio = db.StringField(required=True, max_length=70)
    document = db.StringField(required=True, max_length=70)
    payments = db.StringField(required=True, max_length=70)
    photo = db.StringField(required=True, max_length=70)

    def hash_password(self):
         self.password = generate_password_hash(self.password).decode('utf8')
 
    def check_password(self, password):
         return check_password_hash(self.password, password)