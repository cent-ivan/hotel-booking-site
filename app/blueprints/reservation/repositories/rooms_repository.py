from datetime import datetime
from ..models.room_type_model import RoomType
from ..models.rooms_model import Room
from ..models.booking_model import Booking
from ..models.customer_model import Customer
from ..models.reservation_model import Reservation
from ....extensions import db, SQLAlchemyError, select, update

class ReservationRepository:
    #--READ ---------------------------------------------------------
    @staticmethod
    def retrieve_room_types() -> list:
        try:
            room_types = RoomType.query.all()
            res = [room_type for room_type in room_types]
            return res
        except SQLAlchemyError as err:
            raise err

    @staticmethod
    def retrieve_room_details(room_types : list) -> list:
        qry = select(RoomType).where(RoomType.name.in_(room_types))
        qry_res = db.session.execute(qry).fetchall() #returns [(Object), (Object)]
        data = [room[0] for room in qry_res] #List[Object]
        return data
    
    @staticmethod
    def count_rooms(typeid) -> int:
        try:
            '''SELECT COUNT(status) FROM roomstbl 
            INNER JOIN roomtypestbl ON roomstbl.room_typeid = roomtypestbl.room_typeid WHERE status='available' AND roomtypestbl.room_typeid=4'''
            results = db.session.query(Room.status).join(RoomType, Room.room_typeID == RoomType.room_typeID).filter(Room.room_typeID==typeid, Room.status=='available').count()
            if results != 0:
                return results #returns Ex. 2 or 0
            else:
                return 0
        except SQLAlchemyError as err:
            raise err
    
    #ASSIGN ROOM NUMBER
    @staticmethod
    def check_available(typeid): #returns assigned room number
        try:
            '''SELECT roomtypestbl.name, roomstbl.roomnumber, status FROM roomstbl 
            INNER JOIN roomtypestbl ON roomstbl.room_typeid = roomtypestbl.room_typeid WHERE status='available' AND roomtypestbl.room_typeid=4 LIMIT 1;'''
            results = db.session.query(Room.roomID, Room.roomnumber, RoomType.name, RoomType.price).join(RoomType, Room.room_typeID == RoomType.room_typeID).filter(Room.room_typeID==typeid, Room.status=='available').first()
            if results is not None:
                ReservationRepository.update_occupied(results[1]) #change to occupied
                return tuple(results) #returns Ex. (1, 401, Deluxe Room, 3500)
            else:
                return None
        except SQLAlchemyError as err:
            raise err
    
    #GET customer ID
    @staticmethod
    def retrieve_customerID(uid) -> int:
        try:
            customerID = db.session.query(Customer.customerID).filter(Customer.publicuuid==uid).first()
            if customerID is not None:
                return customerID[0]
            return 0
        except SQLAlchemyError as err:
            raise err
        
    @staticmethod
    def retrieve_bookingID(uid) -> int:
        try:
            bookingID = db.session.query(Booking.bookingID).filter(Booking.publicuuid==uid).first()
            if bookingID is not None:
                return bookingID[0]
            return 0
        except SQLAlchemyError as err:
            raise err

    #---INSERT DATA-------------------------------------------
    @staticmethod
    def register_customer(**customer_information) -> str:
        try:
            customer = Customer(
                publicuuid=customer_information['customer_data']['uid'], # type: ignore
                firstname=customer_information['customer_data']['firstname'],  # type: ignore
                lastname=customer_information['customer_data']['lastname'],  # type: ignore
                gender=customer_information['customer_data']['gender'],  # type: ignore
                contactnumber=customer_information['customer_data']['contact'],  # type: ignore
                email=customer_information['customer_data']['email'],  # type: ignore
                address=customer_information['customer_data']['address'],  # type: ignore
                country=customer_information['customer_data']['country']  # type: ignore
            )
            db.session.add(customer)
            db.session.commit()
            return 'Success'
        except SQLAlchemyError as err:
            raise err
        

    @staticmethod
    def register_booking(**booking_information):
        try:
            bookIDs = []

            date = datetime.now().strftime('%Y-%m-%d')
            customerid = ReservationRepository.retrieve_customerID(booking_information['customer_data']['uid'])
            for room in booking_information['customer_data']['room_data']:
                #checks promo
                promo_value = booking_information['customer_data']['promo']
                promo_value = promo_value if promo_value.strip() else None
                booking = Booking(
                    publicuuid=booking_information['customer_data']['uid'],  # type: ignore
                    customerID=customerid, # type: ignore
                    checkin=booking_information['customer_data']['checkin'],  # type: ignore
                    checkout=booking_information['customer_data']['checkout'],  # type: ignore
                    request=booking_information['customer_data']['note'],  # type: ignore
                    promoID=promo_value,  # type: ignore
                    totalprice=booking_information['total_price'],  # type: ignore
                    createdon=date  # type: ignore
                )
                db.session.add(booking) #ORM API
                db.session.commit()
                bookingID = ReservationRepository.retrieve_bookingID(booking_information['customer_data']['uid'])
                bookIDs.append(bookingID)

            #add reservation
            iter = list(zip(bookIDs,  booking_information['selected_room'], booking_information['customer_data']['room_data'],)) 
            #[bookingID=1, (id=1, roomnum=101, roomname=Standard Room, price=2500), (qty, roomtypeID, adult, children)]
            for bookingID, room, selected_room in iter:
                roomID = int(room[0])
                qty = int(selected_room[0])
                adults=int(selected_room[2])
                children=int(selected_room[3])
                ReservationRepository.register_reservation(bookingID, roomID, qty, adults, children)
            return 'Success'
        except SQLAlchemyError as err:
            raise err



    @staticmethod
    def register_reservation(bookingID:int, roomsID:int, qty:int, adults:int, children:int) -> None:
        try:
            reservation = Reservation(
                bookingid = bookingID, # type: ignore
                roomid=roomsID, # type: ignore
                roomqty=qty, # type: ignore
                adults=adults, # type: ignore
                children=children # type: ignore
            )
            db.session.add(reservation)
            db.session.commit()
        except SQLAlchemyError as err:
            raise err
        

    #--UPDATE DATA--------------------------------------------
    @staticmethod
    def update_occupied(roomnumber): #update room status
        try:
            update_room = update(Room).values(status='occupied').where(Room.roomnumber==int(roomnumber))
            db.session.execute(update_room)
            db.session.commit()
        except SQLAlchemyError as err:
            raise err 
        
    @staticmethod
    def update_available(roomnumber):
        try:
            update_room = update(Room).values(status='available').where(Room.roomnumber==int(roomnumber))
            db.session.execute(update_room)
            db.session.commit()
        except SQLAlchemyError as err:
            raise err 
        

