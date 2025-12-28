from ....extensions import db, Column, Integer, String, Date, Numeric, UUID, orm, ForeignKey
from datetime import datetime, timezone
from flask import json 

class Booking(db.Model):
    __tablename__ = 'bookingtbl'

    bookingID =  Column(Integer, primary_key=True, name='bookingid')
    publicuuid = Column(UUID, nullable=False, name='public_uuid')
    customerID = Column(Integer, ForeignKey('customertbl.customerid'), nullable=False, name='customerid')
    checkin = Column(Date, nullable=False, name='checkin')
    checkout = Column(Date, nullable=False, name='checkout')
    request = Column(String, name='request')
    promoID = Column(String, ForeignKey('promotbl.promoid'), nullable=True, name='promoid')
    totalprice = Column(Numeric(8,2), nullable=False, name='totalprice')
    status = Column(String, nullable=False, default='PENDING', name='status')
    createdon = Column(Date, nullable=False, default=datetime.now(timezone.utc), name='createdon')

    customers = orm.relationship('Customer', back_populates='bookings')
    promos = orm.relationship('Promo', back_populates='bookings')   
    #children = orm.relationship('Children', back_populates='bookings')

    #many-to-many
    reservations = orm.relationship('Reservation', back_populates='booking')
    rooms = orm.relationship('Room', secondary='reservationtbl', back_populates='bookings')

    #from Model to json
    def to_json(self):
        return json.dumps({
            'bookingid': self.bookingID,
            'publicuuid' : self.publicuuid,
            'customerid': self.customerID,
            'checkin': self.checkin,
            'checkout': self.checkout,
            'request': self.request,
            'promoid': self.promoID,
            'totalprice': self.totalprice,
            'status': self.status,
            'createdon': self.createdon,
        })
    
    #from json to Model
    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        booking = Booking()
        booking.bookingID = data.get('bookingid')
        booking.publicuuid = data.get('publicuuid')
        booking.customerID = data.get('customerid')
        booking.checkin = data.get('checkin')
        booking.checkout = data.get('checkout')
        booking.request = data.get('request')
        booking.promoID = data.get('promoid')
        booking.totalprice = data.get('totalprice')
        booking.status = data.get('status')
        booking.createdon = data.get('createdon')
        return booking