from flask import render_template, redirect, url_for,request
from ..utils.validators import Validators
from . import public_bp

@public_bp.route('/')
def index():
    return render_template('landing_page.html')


@public_bp.route('/about')
def about():
    return render_template('about.html')

@public_bp.route('/contact')
def contact():
    return render_template('contact.html')


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