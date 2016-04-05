import datetime

from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), index = True)
    email = db.Column(db.String(255), index = True)
    password = db.Column(db.String(128))

    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_on = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)
