from flask import render_template, redirect, url_for, request
from flask import jsonify
from flask import session
import uuid

from . import room_bp

from .services.date_services import DateServices
from ..utils.validators import Validators
from .services.checkout_services import CheckoutServices
from .services.booking_reserve_service import BookingService

@room_bp.route('/', methods=['GET'])
def index():
    #retrieve room types details
    room_types = CheckoutServices.get_room_types()  

    #url params, SHWOWS if the user pressed the 'Check Availability, checks session first
    checkin = request.args.get('checkin')
    checkout = request.args.get('checkout')
    promocode = request.args.get('promocode')

    #assigns a uuid for the guest. 1.) If no UUID yet generates and creates uuid session
    if 'uuid' not in session:
        generated_uuid = uuid.uuid4()
        session['uuid'] = str(generated_uuid)
        CheckoutServices.add_uuid_redis(generated_uuid)

    #CASE: adds the uuid in redis cache
    guest_uuid = session['uuid']
    if not CheckoutServices.in_redis(guest_uuid):
        CheckoutServices.add_uuid_redis(guest_uuid)

    #retrieve the rooms in user cache
    selected = CheckoutServices.get_selected_rooms(guest_uuid)
    
    #check first if the user entered a checkin and checkout date
    if Validators.is_empty(checkin):
        #if the user saved a checkin date
        if 'checkin' not in session:
            return render_template('rooms.html',checkin=DateServices.today(), checkout=DateServices.next_day(), promocode='', room_types=room_types, guest_uuid = guest_uuid, selected=selected) #CASE: initial open of a new user
        return render_template('rooms.html',checkin=session['checkin'], checkout=session['checkout'], promocode='', room_types=room_types, guest_uuid = guest_uuid, selected=selected) #CASE: when the user exits and comebacls again
        
    #CASE: user has search room availability | save booking preference
    session['checkin'] = checkin
    session['checkout'] = checkout

    return render_template('rooms.html', checkin=checkin, checkout=checkout, promocode=promocode, room_types=room_types, guest_uuid = guest_uuid, selected=selected)


#-caching selected rooms---------
@room_bp.route('/add/<string:uuid>/<string:room>')
def add_room(uuid, room):
    CheckoutServices.register_room_type(uuid, room) #uploads to cache the room
    return redirect(url_for('rooms.index'))

@room_bp.route('/delete/<string:uuid>/<string:room>')
def delete_room(uuid, room):
    CheckoutServices.delete_room_type(uuid, room) #delete in redis
    return redirect(url_for('rooms.index'))
#------------------------------------

@room_bp.route('/checkout', methods=['GET'])
def checkout():
    data = request.args #gets the url parameters
    total_nights = DateServices.calculate_total_nights(data.get('checkin'), checkout=data.get('checkout'))

    #CASE: if url param uid is not equal to session and not in then it will retrieve the real
    if data.get('uid') != session['uuid']:
        #resets the wrong url param uid
        uid = CheckoutServices.get_uuid_from_redis(session['uuid'])
        return redirect(url_for('rooms.checkout', checkin=data.get('checkin'), checkout=data.get('checkout'), uid=uid))
        
    room_details = CheckoutServices.get_room_type_details(session['uuid'])
    return render_template(
        'checkout.html', 
        checkin=data.get('checkin'), checkout=data.get('checkout'), guest_uuid=data.get('uid'), total_nights=total_nights, rooms=room_details
    )


@room_bp.route('/confirmation', methods=['GET','POST']) # type: ignore because it is always 
def confirmation():
    #-ROOM
    qty = request.form.getlist('qty')
    room_id = request.form.getlist('room-type-id')
    adults = request.form.getlist('adults')
    children = request.form.getlist('children')
    room_data = list(zip(qty, room_id, adults, children)) #[(qty, roomtypeID, adult, children)]

    #convert to dict
    data = {
        'firstname' : request.form.get('firstname'),
        'lastname' : request.form.get('lastname'),
        'gender' : request.form.get('gender'),
        'contact' : request.form.get('tel'),
        'email' : request.form.get('email'),
        'address' : request.form.get('address'),
        'country' : request.form.get('country'),
        
        #-BOOKING--
        'uid' : request.form.get('uid'),
        'note' : request.form.get('request'),
        'promo' : request.form.get('promocode'),
        'checkin' : request.form.get('checkin'),
        'checkout' : request.form.get('checkout'),

        'room_data': room_data #[(qty, roomtypeID, adult, children)]
    }

    if request.method == 'POST': #UPLOADS booking details
        result = BookingService.reserve_roomnum(**data) #Ex. [{total_price:value, customer_data:form, room:[()]}]
        delete = BookingService.delete_client_uid(request.form.get('uid'))
        if delete > 0:
            session.clear()
        return render_template('confirmation.html', result = result)



#--FILTERS-----------------------------
@room_bp.app_template_filter('format_date')
def format_date(date):
    todaySplit = date.split('-')
    year = int(todaySplit[0])
    month = int(todaySplit[1])
    day = int(todaySplit[2])

    formatted_date = f"{str(month).rjust(2,'0')}-{str(day).rjust(2,'0')}-{year}"
    return formatted_date