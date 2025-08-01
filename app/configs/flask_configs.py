from datetime import timedelta
from flask import redirect, url_for
from dotenv import load_dotenv
from redis import Redis
import os

load_dotenv()

class RedisConfig:
    host = os.getenv('REDIS_DOCKER_HOST','localhost') #change to REDIS_HOST for local config, REDIS_DOCKER_HOST for docker
    port = os.getenv('REDIS_PORT', 6379)
    db = os.getenv('REDIS_DB', 0)
    
    @classmethod
    def to_dict(cls):
        return {
            'host':cls.host,
            'port':cls.port,
            'db':cls.db
        }

class Config:
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = os.getenv('SECRET_KEY')
    PERMANENT_SESSION_TIME = timedelta(days=3)

    #--database configuraion--
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #--session----
    SESSION_TYPE = 'redis'
    SESSION_REDIS = Redis(**RedisConfig.to_dict())

class ProductionConfig:
    TESTING=False
    SECRET_KEY = os.getenv('SECRET_KEY')
    PERMANENT_SESSION_TIME = timedelta(days=3)

    #--database configuraion--
    SQLALCHEMY_DATABASE_URI = os.getenv('DOCKER_DATABASE_URI') #change to DATABASE_URI for local development, DOCKER_DATABASE_URI for docker
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #--session----
    SESSION_TYPE = 'redis'
    SESSION_REDIS = Redis(**RedisConfig.to_dict())


class PyscopgConfig:
    def __init__(self) -> None:
        self.HOST = os.getenv('DOCKER_HOST') #change to HOST for local development, DOCKER_HOST for docker
        self.USER = os.getenv('DB_USER')
        self.PASSWORD = os.getenv('PASSWORD')
        self.PORT = os.getenv('PORT')
        self.DATABASE_NAME = os.getenv('DATABASE_NAME')

    def to_dict(self) -> dict:
        return {
            'host': self.HOST,
            'dbname': self.DATABASE_NAME,
            'password':self.PASSWORD,
            'user': self.USER,
            'port': self.PORT
        }
