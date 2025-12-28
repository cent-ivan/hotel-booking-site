from flask import Blueprint

room_bp = Blueprint('rooms', __name__, template_folder='templates')

from . import rooms_views