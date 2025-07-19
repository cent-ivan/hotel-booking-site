from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = os.getenv('SECRET_KEY')
    PERMANENT_SESSION_TIME = timedelta(days=3)

    #--database configuraion--
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')

class RedisConfig:
    host = os.getenv('REDIS_HOST','localhost')
    port = os.getenv('REDIS_PORT', 6379)
    db = os.getenv('REDIS_DB', 0)
    
    @classmethod
    def to_dict(cls):
        return {
            'host':cls.host,
            'port':cls.port,
            'db':cls.db
        }