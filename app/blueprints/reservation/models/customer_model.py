from ....extensions import db, Column, Integer, String, UUID, orm
from flask import json 

class Customer(db.Model):
    __tablename__ = 'customertbl'
    customerID = Column(Integer, primary_key=True, name='customerid')
    publicuuid = Column(UUID, nullable=False, name='public_uuid')
    firstname =  Column(String(50), nullable=False, name='firstname' )
    lastname =  Column(String(50), nullable=False, name='lastname' )
    gender = Column(String(20), nullable=False, name='gender')
    contactnumber = Column(String(20), nullable=False, name='contactnumber')
    email = Column(String(50), nullable=False, name='email')
    address = Column(String(50), nullable=False, name='address')
    country = Column(String(50), nullable=False, name="country")

    bookings = orm.relationship('Booking', back_populates='customers')

    #from Model to json converter
    def to_json(self):
        return json.dumps({
            'customerID':self.customerID,
            'publicuuid' : self.publicuuid,
            'firstname' : self.firstname,
            'lastname' : self.lastname,
            'gender':self.gender,
            'contactnumber':self.contactnumber,
            'email': self.email,
            'address':self.address,
            'country':self.country
        })
    
    #from json to Model Object
    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        customer = Customer()
        customer.customerID = data['customerID']
        customer.publicuuid = data['publicuuid']
        customer.firstname = data['firstname']
        customer.lastname = data['lastname']
        customer.gender = data['gender']
        customer.contactnumber = data['contactnumber']
        customer.email = data['email']
        customer.address = data['address']
        customer.country = data['country']
        return customer