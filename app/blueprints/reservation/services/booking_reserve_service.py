from ..repositories.rooms_repository import ReservationRepository #Postgres
from ..repositories.redis_repo import RedisRepository
from .date_services import DateServices


class BookingService:
    @staticmethod
    def compute_price(qty, price, nights):
        total = (int(qty) * price) * nights
        return total
    

    @staticmethod
    def reserve_roomnum(**form) -> dict:
        room = []
        total_price = 0
        rooms:list = form['room_data'] # type: ignore [(qty, roomtypeID, adult, children), (qty, roomtypeID, adult, children)]
        for room_details in rooms:
            id = int(room_details[1]) 
            res = ReservationRepository.check_available(id) #Ex. (id=1, roomnum=101, roomname=Standard Room, price=2500)
            if res is not None:
                total_nights = DateServices.calculate_total_nights(form['checkin'], form['checkout'])
                price = BookingService.compute_price(qty=room_details[0], price=res[3], nights=total_nights) # type: ignore
                total_price += price
                room.append(res)
        

        data = {
            'total_price': total_price, # type: ignore
            'customer_data': form, #{uuid, firstname, lastname, gender, room_data=[(qty, roomtypeID, adult, children),]}
            'selected_room': room #[(id=1, roomnum=101, roomname=Standard Room, price=2500),]
        }
        return BookingService.add_customer(**data) #Process -> Add Customer - Add Booking -> Add bookingid and roomid in Reservation

    #1.) Store the customer data then retrieve the ID
    @staticmethod
    def add_customer(**customer_information):
        customer = ReservationRepository.register_customer(**customer_information)
        if customer == 'Success': #calls the add booking
            return BookingService.add_booking(**customer_information)
        else:
            raise ConnectionError

    #2.) Store the booking data then adds to the Reservation Table
    @staticmethod
    def add_booking(**booking_information):
        booking =  ReservationRepository.register_booking(**booking_information) #auto adds the rooms
        if booking ==  'Success':
            return booking_information
        else:
            return {}

    #3.) delete uid in client
    @staticmethod
    def delete_client_uid(uid) -> int:
        result = RedisRepository.delete_cache(uid)
        return result
 