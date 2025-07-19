from ..repositories.rooms_repository import ReservationRepository #Postgres
from ..repositories.redis_repo import RedisRepository

class CheckoutServices:
    @staticmethod
    def count_room_types(typeid) -> int: #get room counts
        count = ReservationRepository.count_rooms(int(typeid))
        return count
    
    @staticmethod
    def get_room_types() -> list: #list down the room types
        result = []
        rooms = ReservationRepository.retrieve_room_types()
        for room in rooms:
            data = {
                'count': CheckoutServices.count_room_types(room.room_typeID),
                'room':room
            }
            result.append(data)
        return result
    
    #retrieve the room details
    @staticmethod
    def get_room_type_details(session_uid) -> list:
        #1. Redis - user preferences
        rooms = RedisRepository.retrieve_selected_rooms(session_uid) #saved rooms

        #2. Postgres - get the room details for price in the RoomType/Convert to Room Type details
        room_details = ReservationRepository.retrieve_room_details(rooms)
        return room_details
    

#--REDIS-----------------------------------
    @staticmethod
    def get_uuid_from_redis(session_uuid): #GETS uuid from cache
        uid = RedisRepository.retrieve_uuid(session_uuid)
        return uid


    #ADDS user uuid in cache
    @staticmethod
    def add_uuid_redis(uuid) -> None:
        RedisRepository.register_uuid_redis(uuid)
    
    #RETRIEVES the user selected rooms in cache
    @staticmethod
    def get_selected_rooms(uuid) -> list:
        return RedisRepository.retrieve_selected_rooms(uuid)

    #ADDS a selected room to Summary Display
    @staticmethod
    def register_room_type(uuid, room) -> None:
        RedisRepository.register_selected_room(uuid, room) #Add to redis

    #DELETES a selected room to Summary Display
    @staticmethod
    def delete_room_type(uuid, room) -> None:
        RedisRepository.delete_selected_room(uuid, room) #delete in redis


    #CHECKS if its in redis
    @staticmethod
    def in_redis(uuid) -> bool:
        return RedisRepository.is_in_redis(uuid)




#--utility----------------------------