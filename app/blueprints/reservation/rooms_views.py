from flask import render_template, redirect, url_for, request
from . import room_bp
from .services.date_services import today, next_day
from ..utils.validators import Validators

@room_bp.route('/', methods=['POST', 'GET'])
def index():
    room_types = [
            {
                "room_typeID": 1,
                "name": "Deluxe Room",
                "price": 3200.00,
                "description": "A spacious room with balcony and garden view.",
                "note": "No smoking allowed.",
                "size": 25.500,
                "capacity": "2",
                "bedtype": "Queen Bed",
                "amenities": ["WiFi", "Air Conditioning", "Hot Shower", "Flat TV", "Mini Fridge"],
                "imageurl": "https://example.com/images/deluxe.jpg"
            },
            {
                "room_typeID": 2,
                "name": "Family Suite",
                "price": 5200.00,
                "description": "Ideal for families, includes a living area and two beds.",
                "note": "Extra bed optional.",
                "size": 40.750,
                "capacity": "4",
                "bedtype": "2 Double Beds",
                "amenities": ["WiFi", "Air Conditioning", "Bathtub", "Kitchenette", "Balcony"],
                "imageurl": "https://example.com/images/family-suite.jpg"
            },
    ]
    if request.method == 'POST':
        checkin = request.args.get('checkin')
        checkout = request.args.get('checkout')
        promocode = request.args.get('promocode')

        
        if Validators.is_empty(checkin) and Validators.is_empty(checkout):
            return render_template('rooms.html',checkin=checkin, checkout=checkout, promocode=promocode, room_types=room_types)
        return render_template('rooms.html',checkin=checkin, checkout=checkout, promocode=promocode, room_types=room_types)
    else:
        checkin = request.args.get('checkin')
        checkout = request.args.get('checkout')
        promocode = request.args.get('promocode')

        #check first if the user entered a checkin and checkout date
        if Validators.is_empty(checkin):
            return render_template('rooms.html',checkin=today(), checkout=next_day(), promocode='', room_types=room_types)
        return render_template('rooms.html', checkin=checkin, checkout=checkout, promocode=promocode, room_types=room_types)

@room_bp.route('/checkout/<string:type>')
def checkout(type):
    return render_template('checkout.html', type = type)