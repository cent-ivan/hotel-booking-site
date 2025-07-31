from flask import abort
from ....extensions import Redis, RedisError
from ....configs.flask_configs import RedisConfig

from ...auth.employee_model import Employee

class FrontRedisRepository:
    @staticmethod
    def remove_employee_cache(uid) -> int:
        try:
            r = Redis(**RedisConfig.to_dict())
            key = f'hotelreservation:employee:{uid}'
            check = r.keys(key)
            if check:
                r.delete(key)
                return 200
            else:
                return 0
        except RedisError as err:
            return 500