import os

from sqlalchemy import create_engine

class config(object):
    SECRET_KAY ="ClaveSecreta"
    SESSION_COOKIE_SECURE= False

class DevelopmentConfig(config):
    Debug = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/bdidgs804'
    SQLALCHEMY_TRACK_MODIFICATIONS = False