from ...extensions import UserMixin, db, Column, Integer, String, Date
from flask import json

class Employee(db.Model, UserMixin):
    __tablename__ = 'employeetbl'

    employeeID = Column(String, primary_key=True, name='employeeid')
    firstname =  Column(String(50), nullable=False, name='firstname' )
    lastname =  Column(String(50), nullable=False, name='lastname' )
    gender = Column(String(20), nullable=False, name='gender')
    contactnumber = Column(String(20), nullable=False, name='contactnumber')
    email = Column(String(50), nullable=False, name='email')
    address = Column(String(50), nullable=False, name='address')
    role = Column(String(20), nullable=False, name='role')
    password = Column(String(255), nullable=False, unique=True, name='password')
    createdon = Column(Date, nullable=False, name='createdon')

    def get_id(self):
        return str(self.employeeID)

    #from Model to json
    def to_json(self):
        return json.dumps({
            'employeeid' : self.employeeID,
            'firstname' : self.firstname,
            'lastname' : self.lastname,
            'gender':self.gender,
            'contactnumber':self.contactnumber,
            'email':self.email,
            'address':self.address,
            'role':self.role,
            'password':self.password,
            'createdon':self.createdon
        })

    #from json to Model
    @staticmethod
    def from_json(json_data):
        data = json.loads(json_data)
        employee = Employee()
        employee.employeeID = data['employeeid']
        employee.firstname = data['firstname']
        employee.lastname = data['lastname']
        employee.gender = data['gender']
        employee.contactnumber = data['contactnumber']
        employee.email = data['email']
        employee.address = data['address']
        employee.role = data['role']
        employee.password = data['password']
        employee.createdon = data['createdon']
        return employee