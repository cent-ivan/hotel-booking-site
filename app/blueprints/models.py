from .reservation.models.booking_model import Booking
from .reservation.models.children_model import Children
from .reservation.models.customer_model import Customer
from .reservation.models.employee_model import Employee
from .reservation.models.promo_model import Promo
from .reservation.models.reservation_model import Reservation
from .reservation.models.room_type_model import RoomType
from .reservation.models.rooms_model import Room

__all__ = [
    'Booking',
    'Children',
    'Customer',
    'Employee',
    'Promo',
    'Reservation',
    'RoomType',
    'Room'
]

all_models = [
    Booking,
    Children,
    Customer,
    Employee,
    Promo,
    Reservation,
    RoomType,
    Room
]