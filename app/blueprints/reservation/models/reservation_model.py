from ....extensions import db, Column, Integer, UUID, orm, ForeignKey

class Reservation(db.Model):
    __tablename__ = 'reservationtbl'

    bookingid = Column(Integer, ForeignKey('bookingtbl.bookingid', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    roomid = Column(Integer, ForeignKey('roomstbl.roomid', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    roomqty = Column(Integer, nullable=False, name='roomqty')
    adults = Column(Integer, nullable=False, name='adults')
    children = Column(Integer, name='children')


    # Relationships
    booking = orm.relationship('Booking', back_populates='reservations')
    room = orm.relationship('Room', back_populates='reservations')
