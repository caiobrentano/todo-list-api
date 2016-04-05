import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'super-dooper-secret'
USE_TOKEN_AUTH = False

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'api.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = True
