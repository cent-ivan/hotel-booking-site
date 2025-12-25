from flask import Blueprint

front_bp = Blueprint('employee', __name__, template_folder='templates')

from . import frondesk_views