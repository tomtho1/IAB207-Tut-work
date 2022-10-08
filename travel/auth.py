#from crypt import methods
from email import header
import imp
from tabnanny import check
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import LoginForm, RegisterForm
from flask_login import login_user, login_required, logout_user
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    error = None
    if loginForm.validate_on_submit():
        user_name = loginForm.user_name.data
        password = loginForm.password.data
        user = User.query.filter_by(name=user_name).first()
        if user is None:
            error = 'incorrect username or password'
        elif not check_password_hash(user.password_hash, password):
            error = 'incorrect username or password'
        if error is None:
            login_user(user)
            print('Logged in successfully')
            flash('Logged in successfully')
        return redirect(url_for('main.index'))
    return render_template('user.html', form=loginForm, heading='Login')

@bp.route('/register', methods=['GET','POST'])
def register():
    registerForm = RegisterForm()
    if registerForm.validate_on_submit():
        username = register.user_name.data
        password = register.password.data
        email = register.email.data

        user = User.query.filter_by(name=username).first()
        if user: 
            flash('Username already exists!')
            return redirect(url_for('auth.login'))

        password_hash = generate_password_hash(password)
        new_user = User(name=username, password_hash = password_hash, emailid=email)
        db.session.add(new_user)
        db.session.commit()

        print('Succesfully Registered')
        return redirect(url_for('auth.login'))
    else:
        return render_template('user.html', form=registerForm, heading='Register')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You have been logged out'
    return redirect(url_for('main.index'))