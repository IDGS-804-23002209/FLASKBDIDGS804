import os

from sqlalchemy import create_engine

<<<<<<< HEAD
class Config(object):
    SECRET_KEY = "ClaveSecreta"
    SESION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
=======
class config(object):
    SECRET_KAY ="ClaveSecreta"
    SESSION_COOKIE_SECURE= False

class DevelopmentConfig(config):
    Debug = True
>>>>>>> 5d0e5cb02d7b8789d994332094f5671803e63677
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/bdidgs804'
    SQLALCHEMY_TRACK_MODIFICATIONS = False