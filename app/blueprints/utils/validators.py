class Validators:
    @staticmethod
    def is_empty(data) -> bool: #check empty string
        if data == '' or data == None:
            return True
        else:
            return False