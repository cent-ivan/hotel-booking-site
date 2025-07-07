from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = os.getenv('SECRET_KEY')
    PERMANENT_SESSION_TIME = timedelta(hours=24)

    #--database configuraion--
    #SQLALCHEMY_DATABASE_URI = ''