import os


class Config(object):
    DEBUG = False
    SECRET_KEY = 'develop'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///genten.db'
