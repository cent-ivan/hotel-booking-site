from ....extensions import bycrypt

class Validators:
    @staticmethod
    def check_password(password,entered_pass ) -> bool:
        if bycrypt.check_password_hash(password, entered_pass):
            return True
        return False