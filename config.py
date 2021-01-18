import os


class Config(object):
    DEBUG = False
    PG_PASS = 'EazdJhQW4j'
    PG_USER = 'genten'
    PG_URL = os.environ['DATABASE_URL']
    SECRET_KEY = 'develop'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://genten:develop@localhost/genten'
