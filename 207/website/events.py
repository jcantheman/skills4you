from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import event, user, booking, comment
from .forms import CreateForm, BookingForm, CommentForm
from . import db
from flask_login import login_required, current_user
from website.users import get_current_user
import os
from werkzeug.utils import secure_filename

bp = Blueprint('events', __name__)

def check_upload_file(form):
  #get file data from form  
  fp=form.image.data
  filename=fp.filename
  BASE_PATH=os.path.dirname(__file__)
  upload_path = os.path.join(BASE_PATH,'website\static\img', secure_filename(filename))
  db_upload_path = 'website\static\img' + secure_filename(filename)
  fp.save(db_upload_path)
  return db_upload_path

@bp.route('/<id>')
def show(id):
    destination = event.query.filter_by(id=id).first()
    cform = CommentForm()    
    return render_template('booking.html', event=event, form=cform)

@bp.route('/eventcreation', methods=['GET', 'POST'])
@login_required
def creation():
    print('Method type: ', request.method)
    form = CreateForm()
    if form.validate_on_submit():
        db_file_path = check_upload_file(form)
        create=event(ownerid=get_current_user(), title=form.title.data, description=form.description.data, 
        image=db_file_path, date=form.date.data, location=form.location.data,
        category=form.category.data, tickets=form.tickets.data, status="Upcoming")
        db.session.add(create)
        db.session.commit()
        flash('Your Event Has Been Created!')
        return redirect(url_for('events.creation'))

    return render_template('create.html', form=form)

@bp.route('/eventmanage', methods=['GET', 'POST'])
@login_required
def manage():
    events = event.query.all()
    users = user.query.all()
    get_current_event()
    return render_template('manage.html', events=events, users=users)

@bp.route('/eventbooking', methods=['GET', 'POST'])
def booking():
    print('Method type: ', request.method)
    form = BookingForm()
    if form.validate_on_submit():
        bookings = booking(ticket=form.ticketbook.data
        , emailid=get_current_user)
        db.session.add(bookings)
        db.session.commit()
        return redirect(url_for('events.booking'))
    return render_template('booking.html', form=form)

@bp.route('/<eventdetails>/comment', methods = ['GET', 'POST'])
@login_required
def details(event):  
    form = CommentForm()  
    event_obj = event.query.filter_by(id=event).first()  
    if form.validate_on_submit():  
      Comment = comment(text=form.text.data,  
                        evenmt=event_obj,
                        user=current_user) 
      db.session.add(Comment) 
      db.session.commit() 
      print('Your comment has been added', 'success') 
    return redirect(url_for('details.html', id=event))


def get_current_event():
    if request.method == 'POST':
        currentevent = request.form['submit_button']
        print('nice one man')
        return currentevent

# @bp.route('/eventdetails')
# def details():
    # return render_template('details.html')

@bp.route('/bookinghistory')
def history():
    return render_template('history.html')

@bp.route('/<id>')
def edit():
    return render_template('edit.html')
