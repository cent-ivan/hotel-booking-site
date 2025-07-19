from flask import render_template, redirect, url_for

from . import auth_bp

@auth_bp.route('/signin/')
def signin():
    return render_template('signin.html')