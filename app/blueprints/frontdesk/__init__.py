from flask import Blueprint

front_bp = Blueprint('front', __name__, template_folder='templates')

from . import frondesk_views