from ..repositories.table_repository import TableRepository

class DashboardService:
    @staticmethod
    def retrieve_customers() -> list:
        return TableRepository.retrieve_guests()
    
    @staticmethod
    def get_details(uuid) -> dict:
        results = TableRepository.retrieve_guest_details(uuid)
        if results:
            data = {
                'bookingid': results[0], 
                'roomid': results[1],
                'roomqty': results[2],
                'adults': results[3], 
                'children': results[4],
                'public_uuid': results[5],
                'checkin': results[6],
                'checkout': results[7],
                'request': results[8],
                'promoid': results[9],
                'totalprice': results[10],
                'status': results[11],
                'createdon': results[12],
                'firstname': results[13],
                'lastname': results[14],
                'gender': results[15],
                'contactnumber': results[16],
                'email': results[17],
                'address': results[18],
                'country': results[19],
                'roomnumber': results[20],
                'room_status': results[21],
                'room_typeid': results[22],
                'room_type_name': results[23],
                'room_type_price': results[24] 
            }
            return data
        return {}
    
    #--Employee CRUD--
    @staticmethod
    def retrieve_employee_details(uid):
        return TableRepository.retrieve_employee_details(uid)

    @staticmethod
    def retrieve_employees() -> list:
        return TableRepository.retrieve_employees()
    
    @staticmethod
    def add_employee(**data) -> int:
        return TableRepository.add_employee(**data)
    
    @staticmethod
    def delete_employee(uid) -> int:
        return TableRepository.remove_employee(uid)

    @staticmethod
    def update_employee(**data) -> int:
        return TableRepository.update_employee(**data)
    
    
    

    