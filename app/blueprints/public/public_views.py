from flask import render_template, redirect, url_for,request
from ..utils.validators import Validators
from ..reservation.services.checkout_services import CheckoutServices
from . import public_bp

@public_bp.route('/')
def index():
    room_types = CheckoutServices.get_room_types()
    return render_template('landing_page.html', room_types=room_types)


@public_bp.route('/about')
def about():
    return render_template('about.html')

@public_bp.route('/contact')
def contact():
    return render_template('contact.html')

@public_bp.route('/error/<int:error_status>')
def error_handler(error_status):
    error_header = ''
    error_message = ''
    match error_status:
        case 403:
            error_header = 'Forbidden'
            error_header = 'You have access rights to enter this content.'
        case 404:
            error_header = 'Content not Found'
            error_header = 'The server cannot find the requested resource.  URL is not recognized or content not available'
        case 500:
            error_header = 'Internal Server Error'
            error_message = 'The server has encountered a situation it does not know how to handle. There might a problem accessing the database'
        case _:
            error_header = 'Unkown Error'
            error_header = 'The server encountered an unknown error. Please contact the developer'
 
    return render_template('error.html', header=error_header, message=error_message)


#--Jinja template------
@public_bp.app_template_filter('format_date')
def format_date(date):
    if not Validators.is_empty(date):
        months = {
            1: "Jan",
            2: "Feb",
            3: "Mar",
            4: "Apr",
            5: "May",
            6: "Jun",
            7: "Jul",
            8: "Aug",
            9: "Sep",
            10: "Oct",
            11: "Nov",
            12: "Dec"
        
        }
        month_split :list  = date.split('-')
        month_split[0] = months[int(month_split[0])] #converts number montoint
        return f"{month_split[0]} {month_split[1]}, {month_split[2]}"
    else:
        return date
    

