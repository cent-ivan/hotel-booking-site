from ....extensions import bycrypt

class FrontDeskValidators:    
    @staticmethod
    def is_number(number) -> bool:
        try:
            number = int(number)
            return True
        except ValueError as err:
            return False

    @staticmethod
    def check_password(password,entered_pass ) -> bool:
        if bycrypt.check_password_hash(password, entered_pass):
            return True
        return False