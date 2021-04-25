from flask_mongoengine import MongoEngine
from flask_bcrypt import generate_password_hash, check_password_hash

db = MongoEngine()

def initialize_db(app):
    db.init_app(app)