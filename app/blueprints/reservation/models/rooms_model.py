from ....extensions import db, Column, Integer, String, orm, ForeignKey
from flask import json

class Room(db.Model):
    __tablename__ = 'roomstbl'

    roomID = Column(Integer, primary_key=True, name='roomid')
    room_typeID = Column(Integer, ForeignKey('roomtypestbl.room_typeid'), nullable=False, name='room_typeid')
    roomnumber = Column(Integer, nullable=False, name='roomnumber')
    status = Column(String(50), default='available')

    roomtype = orm.relationship('RoomType', back_populates='rooms')

    #many-to-many
    reservations = orm.relationship('Reservation', back_populates='room')
    bookings =  orm.relationship('Booking',secondary='reservationtbl', back_populates='rooms')

    #from Model to json
    def to_json(self):
        return json.dumps({
            'roomid':self.roomID,
            'room_typeid':self.room_typeID,
            'roomnumber':self.roomnumber,
            'status':self.status
        })

    #from json to Model
    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        room = Room()
        room.roomID = data.get('roomid')
        room.room_typeID = data.get('room_typeid')
        room.roomnumber = data.get('roomnumber')
        room.status = data.get('status', 'available')
        return room