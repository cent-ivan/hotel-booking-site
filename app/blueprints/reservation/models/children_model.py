from ....extensions import db, Column, Integer, orm, ForeignKey
from flask import json 

class Children(db.Model):
    __tablename__ = 'childrentbl'

    childrenID = Column(Integer, primary_key=True, name='childrenid')
    bookingID = Column(Integer, ForeignKey('bookingtbl.bookingid'))
    age = Column(Integer, name='age')

    # bookings = orm.relationship('Booking', back_populates='children')