from flask_login import LoginManager, UserMixin
from flask_bcrypt import Bcrypt
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import insert, select, update, orm, ForeignKey, Column, Integer, String, Date, Numeric, ARRAY, Text, UUID
from sqlalchemy.exc import SQLAlchemyError, ProgrammingError
from redis import Redis, DataError


db = SQLAlchemy()
login_manager = LoginManager()
bycrypt = Bcrypt()