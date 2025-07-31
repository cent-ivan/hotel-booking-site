from .validators import Validators
from ..repositories.auth_redis_repo import AuthRedis

class AuthService:
    @staticmethod
    def check_user(id, password):
        #Check redis first
        user = AuthRedis.retrieve_user(id)
        if user is None:
            return None
        
        if not Validators.check_password(user.password, password): # type: ignore
            return None
        
        return user
