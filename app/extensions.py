from flask_login import LoginManager, UserMixin
from flask_bcrypt import Bcrypt
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import insert, select, update, orm, ForeignKey, Column, Integer, String, Date, Numeric, ARRAY, Text, UUID
from sqlalchemy.exc import SQLAlchemyError, ProgrammingError
import psycopg
from psycopg import Error
from typing import LiteralString, cast
from redis import Redis, DataError, RedisError


db = SQLAlchemy()
login_manager = LoginManager()
bycrypt = Bcrypt()  