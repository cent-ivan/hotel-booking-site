from datetime import timedelta

from ....extensions import Redis, RedisError
from ....configs.flask_configs import RedisConfig

from ..employee_model import Employee

class AuthRedis:
    @staticmethod
    def retrieve_user(id): #return must be an ORM
        try:
            r = Redis(**RedisConfig.to_dict())
            key = f'hotelreservation:employee:{id}'

            #1.) Try Redis first
            user = r.get(key)
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
        except RedisError as err:
            raise err
 