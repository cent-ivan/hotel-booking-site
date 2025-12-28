from flask import session
from ....extensions import Redis, DataError
from ....configs.flask_configs import RedisConfig

class RedisRepository:
    r = Redis(**RedisConfig.to_dict())

    #--UUID---------------------------------
    @classmethod
    def register_uuid_redis(cls,uuid) -> None:
        try:
            uid = str(uuid)
            cls.r.hset(f'hotelreservation:guest:{uid}',mapping={
                'UID':uid 
            })
            days = 60 * 24 * 72 #3days
            cls.r.hexpire("guest:{uid}", days, "UID" , nx=True)
        except ConnectionError as conn_err:
            raise ConnectionError('Connection Error') from conn_err
        except DataError as data_err:
            raise data_err

    @classmethod  
    def retrieve_uuid(cls, uuid):
        uid = cls.r.hget(F'hotelreservation:guest:{uuid}','UID')
        return uid

    #--Room Selection------------------------------
    @classmethod 
    def register_selected_room(cls,uuid, room):
        try:
            cls.r.sadd(f'hotelreservation:rooms:{uuid}', room)
            days = 60 * 24 * 72 #3days
            cls.r.expire(f'hotelreservation:rooms:{uuid}' ,days, nx=True)
        except ConnectionError as conn_err:
            raise ConnectionError('Connection Error') from conn_err
        except DataError as data_err:
            raise data_err

    @classmethod 
    def delete_selected_room(cls, uuid, room):
        try:
            cls.r.srem(f'hotelreservation:rooms:{uuid}', room)
        except ConnectionError as conn_err:
            raise ConnectionError('Connection Error') from conn_err
        except DataError as data_err:
            raise data_err

    @classmethod 
    def retrieve_selected_rooms(cls, uuid) -> list: 
        try:
            rooms_set = cls.r.smembers(f'hotelreservation:rooms:{uuid}')
            return [room.decode('utf-8') for room in rooms_set] # type: ignore
        except ConnectionError as conn_err:
            raise ConnectionError('Connection Error') from conn_err
        except DataError as data_err:
            raise data_err
        except:
            return ['Error']
        


    #--utility-------------------------------------
    @classmethod
    def is_in_redis(cls, uuid) -> bool:
        if cls.r.exists(str(uuid)):
            return True
        return False
    
    #Delete the cache and session
    @classmethod
    def delete_cache(cls, uid) -> int:
        if cls.r.exists(f'hotelreservation:guest:{uid}'):
            res = cls.r.delete(f'hotelreservation:guest:{uid}', f'hotelreservation:rooms:{uid}')
            session.clear()
            return res # type: ignore
        return 0
