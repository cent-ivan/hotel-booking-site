from flask import render_template, redirect, url_for
from flask import request, flash
from flask_login import login_user, logout_user

from . import auth_bp
from .services.auth_services import AuthService

@auth_bp.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form.get('id')
        password = request.form.get('password')

        user = AuthService.check_user(id, password) #checks if the credential are correct or the user exists
        if user is None:
            flash('No user found. Either incorrect credentials or the user is not registered')
            return redirect(url_for('auth.login'))
        
        login_user(user)
        return redirect(url_for('employee.index'))
 
@auth_bp.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth_bp.route('/signup/')
def signin():
    return render_template('signin.html')   