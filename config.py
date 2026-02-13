from re import DEBUG
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY="ClaveSecreta"
    SESSION_COOKIE_SECURE=False
    

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://usuario:contrasenia@127.0.0.1/dbidgs803'
    SQLALCHEMY_TRACK_MODIFICATION = False