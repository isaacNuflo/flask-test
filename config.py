import os

class Config(object):
    SECRET_KEY = 'my_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABSE_URI = 'mysql://root:@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False