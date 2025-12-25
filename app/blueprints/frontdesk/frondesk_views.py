from flask import render_template, url_for, redirect, flash
from flask import request
from flask_login import login_required, current_user
from .services.overview_services import DashboardService
from ..utils.validators import Validators #grlobal utils validators
from .services.validators import FrontDeskValidators #current directory Validotor

from . import front_bp

@front_bp.route('/overview/')
@login_required
def index():
    user = current_user
    return render_template('index.html',user=user)

@front_bp.route('/guests/')
@login_required
def guests():
    user = current_user
    customers = DashboardService.retrieve_customers()
    return render_template('guests.html', customers=customers,user=user)

@front_bp.route('/guests/<string:uuid>')
@login_required
def guest_details(uuid):
    guest = DashboardService.get_details(uuid)
    return render_template('view_guest.html', guest=guest)


@front_bp.route('/employees/')
@login_required
def employees_page():
    user = current_user
    employees = DashboardService.retrieve_employees()
    return render_template('employee/employees.html', employees=employees,user=user)

#--EMPLOYEE CRUD Operations---------------------
@front_bp.route('/add-employee', methods=['POST'])
@login_required
def add_employee():
    id = request.form.get('employee-id')
    firstname = request.form.get('employee-firstname')
    lastname = request.form.get('employee-lastname')
    contact = request.form.get('employee-contact')
    email = request.form.get('employee-email')
    address = request.form.get('employee-address')
    gender = request.form.get('employee-gender')
    role = request.form.get('employee-role')
    password = request.form.get('employee-password')

    if not FrontDeskValidators.is_number(contact):
        flash('Make sure the contact form is a number')
        return redirect(url_for('employee.employees_page'))

    if not Validators.is_empty(id) and not Validators.is_empty(firstname) and not Validators.is_empty(lastname) and not Validators.is_empty(contact) and not Validators.is_empty(email) and not Validators.is_empty(address) and not Validators.is_empty(gender) and not Validators.is_empty(role) and not Validators.is_empty(password):
        status = DashboardService.add_employee(
            employeeID=id,
            firstname = firstname,
            lastname=lastname,
            contactnumber=contact,
            email=email,
            address=address,
            gender=gender,
            role=role,
            password=password,
        )
        if status == 200:
            return redirect(url_for('employee.employees_page'))
        else:
            flash('Error 500: Try again or check your connection')
            return redirect(url_for('employee.employees_page'))
    flash('Make sure the forms are not empty')
    return redirect(url_for('employee.employees_page'))

#Confirmation screen serve as ajunction page for the endpoints
@front_bp.route('/confirm-deletion/<string:uid>')
@login_required
def confirm_deletion(uid):
    user = current_user
    return render_template('employee/delete_screen.html', uid=uid, user=user)

@front_bp.route('/delete/<string:uid>', methods=['POST'])
@login_required
def delete_employee(uid):
    password = request.form.get('user-password')
    if FrontDeskValidators.check_password(current_user.password, password):
        status =DashboardService.delete_employee(uid)
        
        if status == 200:
            flash('Employee successfully removed')
        else:
            flash('Delete not successful. Try again later')
        return redirect(url_for('employee.employees_page'))
    
    flash('Delete not successful. Password may be incorrect')
    return redirect(url_for('employee.employees_page'))


@front_bp.route('/update-page/<string:uid>')
@login_required
def update_page(uid):
    user = current_user
    employee_details = DashboardService.retrieve_employee_details(uid)
    return render_template('employee/update_screen.html', employee=employee_details,user=user)


@front_bp.route('/update/<string:uid>', methods=['POST'])
def update_employee(uid):
    id = request.form.get('employee-id')
    firstname = request.form.get('employee-firstname')
    lastname = request.form.get('employee-lastname')
    contact = request.form.get('employee-contact')
    email = request.form.get('employee-email')
    address = request.form.get('employee-address')
    gender = request.form.get('employee-gender')
    role = request.form.get('employee-role')
    password = request.form.get('employee-password')


    if Validators.is_empty(id) or Validators.is_empty(firstname) or Validators.is_empty(lastname) or  Validators.is_empty(contact) or Validators.is_empty(email) or Validators.is_empty(address) or Validators.is_empty(gender) or  Validators.is_empty(role):
        flash('Make sure to fill in all of the fields. The Password is optional')
        return redirect(url_for('employee.update_page'))
    
    status = 0 #variable placeholder for status
    if Validators.is_empty(password):  
        status = DashboardService.update_employee(
            employeeID=id,
            firstname = firstname,
            lastname=lastname,
            contactnumber=contact,
            email=email,
            address=address,
            gender=gender,
            role=role,
            password=''
        )
    else:
        status = DashboardService.update_employee(
            employeeID=id,
            firstname = firstname,
            lastname=lastname,
            contactnumber=contact,
            email=email,
            address=address,
            gender=gender,
            role=role,
            password=password,
        )
    if status == 200:
        #Detect if current user change details
        user_id = current_user.employeeID
        if user_id == id:
            flash('Current user change details. Logging out')
            return redirect(url_for('auth.logout'))
        flash('Employee Details updated')
        return redirect(url_for('employee.employees_page'))
    else:
        flash('Error 500: Try again or check your connection')
        return redirect(url_for('employee.update_page'))

    
#sample,
@front_bp.route('/sample-signup/', methods=['GET', 'POST'])
def sample_signup():
    if request.method == 'GET':
        return render_template('employee/add_sample.html')
    else:
        id = request.form.get('employee-id')
        firstname = request.form.get('employee-firstname')
        lastname = request.form.get('employee-lastname')
        contact = request.form.get('employee-contact')
        email = request.form.get('employee-email')
        address = request.form.get('employee-address')
        gender = request.form.get('employee-gender')
        role = request.form.get('employee-role')
        password = request.form.get('employee-password')

        if not FrontDeskValidators.is_number(contact):
            flash('Make sure the contact form is a number')
            return redirect(url_for('employee.employees_page'))

        if not Validators.is_empty(id) and not Validators.is_empty(firstname) and not Validators.is_empty(lastname) and not Validators.is_empty(contact) and not Validators.is_empty(email) and not Validators.is_empty(address) and not Validators.is_empty(gender) and not Validators.is_empty(role) and not Validators.is_empty(password):
            status = DashboardService.add_employee(
                employeeID=id,
                firstname = firstname,
                lastname=lastname,
                contactnumber=contact,
                email=email,
                address=address,
                gender=gender,
                role=role,
                password=password,
            )
            if status == 200:
                return redirect(url_for('auth.login'))
            else:
                flash('Error 500: Try again or check your connection')
                return redirect(url_for('auth.login'))
        flash('Make sure the forms are not empty')
        return redirect(url_for('auth.login'))

@front_bp.errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html'),403

@front_bp.errorhandler(404)
def not_found(e):
    return render_template('errors/404.html'),404

@front_bp.errorhandler(500)
def internal_error(e):
    return render_template('errors/500.html', error=e),500

#--FILTERS---
@front_bp.app_template_filter('get_initial')
def get_initial(name:str):
    return name[0].upper()