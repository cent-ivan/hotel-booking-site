from ....extensions import db, Column, Integer, String, Numeric, ARRAY, Text, orm
from flask import json

class RoomType(db.Model):
    __tablename__ = 'roomtypestbl'

    room_typeID = Column(Integer, primary_key=True, name='room_typeid')
    name = Column(String(50), nullable=False, name='name')
    price = Column(String(50), nullable=False, name='price')
    description = Column(String(255), nullable=False, name='description')
    note = Column(String, name='note')
    size = Column(Numeric(8,2), nullable=False, name='size')
    capacity = Column(Integer, nullable=False, name='capacity')
    capacitytype = Column(String, name='capacitytype')
    childrencapacity = Column(Integer, nullable=False, name='childrencapacity')
    bedtype = Column(String(25), nullable=False, name='bedtype')
    amenities = Column(ARRAY(String), name='amenities')
    imgurl = Column(Text,nullable=False, name='imageurl')

    rooms = orm.relationship('Room', back_populates= 'roomtype') 
    
    #from Model to dictionary
    def to_dict(self):
        return {
            'room_typeID': self.room_typeID,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'note': self.note,
            'size': self.size,
            'capacity': self.capacity,
            'capacitytype':self.capacitytype,
            'childrencapacity': self.childrencapacity,
            'bedtype': self.bedtype,
            'amenities': self.amenities,
            'imgurl': self.imgurl
        }

    #from Model to json
    def to_json(self):
        return json.dumps({
            'room_typeID': self.room_typeID,
            'name': self.name,
            'price': self.price,
            'description':self.description,
            'note': self.note,
            'size': self.size,
            'capacity': self.capacity,
            'capacitytype':self.capacitytype,
            'childrencapacity': self.childrencapacity,
            'bedtype':self.bedtype,
            'amenities':self.amenities,
            'imgurl':self.imgurl
        })
    
    #from json to Model
    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        roomtype = RoomType()
        roomtype.room_typeID = data['room_typeID']
        roomtype.name = data['name']
        roomtype.price = data['price']
        roomtype.description = data['description']
        roomtype.note = data.get('note')
        roomtype.size = data['size']
        roomtype.capacity = data['capacity']
        roomtype.capacitytype = data['capacitytype']
        roomtype.childrencapacity = data['childrencapacity']
        roomtype.bedtype = data['bedtype']
        roomtype.amenities = data.get('amenities')
        roomtype.imgurl = data['imgurl']
        return roomtype