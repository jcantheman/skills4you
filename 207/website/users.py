from flask import Blueprint, render_template, redirect,url_for,flash, request
from .forms import LoginForm, RegisterForm
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash,check_password_hash
from .models import user
from . import db

bp = Blueprint('users', __name__ )

@bp.route('/register', methods=['GET', 'POST'])
def register():
    register = RegisterForm()
    if (register.validate_on_submit() == True):
            uname=register.user_name.data
            pwd= register.password.data
            email=register.email_id.data
            address=register.address.data
            contact= register.contact.data
            u1 = user.query.filter_by(name=uname).first()
            if u1:
                flash('User name already exists, please login')
                return redirect(url_for('users.login'))
            pwd_hash = generate_password_hash(pwd)
            new_user = user(name=uname, password_hash=pwd_hash, emailid=email, address=address, contact=contact)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index.run'))
    else:
        return render_template('user.html', form=register, heading='Register')



@bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    error=None
    if(login_form.validate_on_submit()==True):
        user_name = login_form.user_name.data
        password = login_form.password.data
        u1 = user.query.filter_by(name=user_name).first()
        if u1 is None:
            error='Incorrect user name'
        elif not check_password_hash(u1.password_hash, password): 
            error='Incorrect password'
        if error is None:
            login_user(u1)
            get_current_user()
            return redirect(url_for('index.run'))
        else:
            flash(error)
    return render_template('user.html', form=login_form, heading='Login')

def get_current_user():
    currentuser = current_user.get_id()
    return currentuser


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('users.login'))


