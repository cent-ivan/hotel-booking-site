from .auth import auth_bp
from .public import public_bp
from .reservation import room_bp

all_blueprints = [
    (public_bp, '/'),
    (auth_bp, '/auth'),
    (room_bp, '/rooms')
]