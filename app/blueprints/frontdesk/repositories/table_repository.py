from flask import abort
from datetime import datetime

from ....configs.flask_configs import PyscopgConfig
from ...models import Customer, Booking, Employee
from ....extensions import SQLAlchemyError, db, psycopg, Error,  cast, LiteralString, bycrypt, select, update
from .front_redis_repository import FrontRedisRepository

class TableRepository:
    @staticmethod
    def retrieve_guests() -> list: 
        try:
            customers = db.session.query(
                Booking.bookingID, 
                Customer.customerID, 
                Customer.publicuuid,
                Customer.firstname, 
                Customer.lastname,
                Customer.email,
                Customer.address,
                Booking.createdon,
                Booking.checkin,
                Booking.checkout,
                Booking.status
            ).join(Customer, Booking.customerID==Customer.customerID).all()
            result = [customer for customer in customers]
            return result
        except SQLAlchemyError as err:
            abort(500)
    
    #gets the long query
    @staticmethod
    def load_query(filename):
        with open(f'sql/select/{filename}', 'r') as sql:
            return cast(LiteralString, sql.read())
        
    @staticmethod
    def retrieve_guest_details(uuid):
        try:
            result = ()
            with psycopg.connect(**PyscopgConfig().to_dict()) as conn:
                with conn.cursor() as cur:
                    qry = TableRepository.load_query('reservation_details.sql')
                    cur.execute(qry, (uuid, ))
                    result = cur.fetchone()
            return result
        except Error as err:
            abort(500)

    
    #-Employee Repo Code--
    @staticmethod
    def add_employee(**data) -> int:
        date = datetime.now().strftime('%Y-%m-%d')
        try:
            hashed_password = bycrypt.generate_password_hash(data['password']).decode('utf-8')
            employee = Employee(
                employeeID=data['employeeID'],  # type: ignore
                firstname=data['firstname'], # type: ignore
                lastname=data['lastname'], # type: ignore
                gender=data['gender'], # type: ignore
                contactnumber=data['contactnumber'], # type: ignore
                email=data['email'], # type: ignore
                address=data['address'], # type: ignore
                role=data['role'], # type: ignore
                password=hashed_password, # type: ignore
                createdon=date # type: ignore
            )
            db.session.add(employee)
            db.session.commit()
            return 200
        except SQLAlchemyError as err:
            abort(500)

    @staticmethod
    def retrieve_employee_details(uid):
        try:
            employee = Employee.query.get(uid)
            return employee
        except SQLAlchemyError as err:
            abort(500)
    
    @staticmethod
    def retrieve_employees() -> list:
        try:
            employees = Employee.query.all()

            return employees
        except SQLAlchemyError as err:
            abort(500)
    
    '''Remove data from cache -> if no password changes update other details but not password, if user input new password, 
    '''
    @staticmethod
    def update_employee(**data) ->int:
        try:
            date = datetime.now().strftime('%Y-%m-%d') #Update when it was modified
            status = FrontRedisRepository.remove_employee_cache(data['employeeID']) #remove cache before in the db
            if data['password'] == '':
                if status == 200 or status == 0:
                    #-No password parameter
                    update_qry = update(Employee).values(
                        employeeID=data['employeeID'], 
                        firstname=data['firstname'], 
                        lastname=data['lastname'], 
                        gender=data['gender'], 
                        contactnumber=data['contactnumber'], 
                        email=data['email'], 
                        address=data['address'], 
                        role=data['role'],  
                        createdon=date 
                    ).where(Employee.employeeID == data['employeeID'])  
                    db.session.execute(update_qry)
                    db.session.commit()
                    return 200
            
            hashed_password = bycrypt.generate_password_hash(data['password']).decode('utf-8')
            if status == 200 or status == 0:
                update_qry = update(Employee).values(
                    employeeID=data['employeeID'], 
                    firstname=data['firstname'], 
                    lastname=data['lastname'], 
                    gender=data['gender'], 
                    contactnumber=data['contactnumber'], 
                    email=data['email'], 
                    address=data['address'], 
                    role=data['role'], 
                    password=hashed_password, 
                    createdon=date 
                ).where(Employee.employeeID == data['employeeID'])
                db.session.execute(update_qry)
                db.session.commit()
                return 200
            return 500
        except SQLAlchemyError as err:
            return 500
    
    

    @staticmethod
    def remove_employee(uid) -> int:
        try:
            status = FrontRedisRepository.remove_employee_cache(uid) #remove cache before in the db
            if status == 200 or status == 0:
                sql_stmnt = select(Employee).where(Employee.employeeID == uid) 
                user = db.session.execute(sql_stmnt).scalar_one()
                        
                db.session.delete(user)
                db.session.commit()
                return 200
            return 500
        except SQLAlchemyError as err:
            return 500
        
