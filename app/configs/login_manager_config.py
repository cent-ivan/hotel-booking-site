from flask import redirect, url_for
from datetime import timedelta

from ..blueprints.models import Employee
from ..extensions import Redis
from .flask_configs import RedisConfig

class LoginManagerConfig:
    @staticmethod
    def configure_login(login_manager): # type: ignore
        r = Redis(**RedisConfig.to_dict())

        '''login to use id, THIS IS IMPORTANT FOR: 
            @login_required,
            current_user
        '''
        @login_manager.user_loader # type: ignore
        def load_user(id):
            key = f'hotelreservation:employee:{id}'
        
            #1.) Try Redis first
            user:bytes = r.get(key) # type: ignore
            if user:
                return Employee.from_json(user.decode('utf-8')) # type: ignore
            
            #2.) Fallback to Postgres
            db_user:Employee = Employee.query.get(id) # type: ignore
            if db_user:
                r.set(f'hotelreservation:employee:{id}', db_user.to_json())
                r.expire(f'hotelreservation:employee:{id}', timedelta(hours=24))
                return db_user
            else:
                return None

        @login_manager.unauthorized_handler # type: ignore
        def unauthorized_callback():
            return redirect(url_for('auth.login'))