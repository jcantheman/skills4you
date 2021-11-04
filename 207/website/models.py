from . import db
from flask_login import UserMixin
from datetime import datetime


class user(db.Model, UserMixin):
    __tablename__='user' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(100), index=True, unique=False, nullable=False)
    contact = db.Column(db.Integer, index=True, unique=False, nullable=False)


class event(db.Model):
    __tablename__ = 'event'
    id= db.Column(db.Integer, primary_key=True)
    ownerid= db.Column(db.String(100), db.ForeignKey('user.emailid'))
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    image= db.Column(db.String(500))
    date = db.Column(db.Integer)
    location = db.Column(db.String(100))
    category = db.Column(db.String(100))
    tickets = db.Column(db.Integer)
    status = db.Column(db.String(100))

class booking(db.Model):
    __tablename__ = 'booking'
    id= db.Column(db.Integer, primary_key=True)
    ticket= db.Column(db.Integer, db.ForeignKey('event.tickets'))
    eventid= db.Column(db.Integer, db.ForeignKey('event.id'))
    emailid= db.Column(db.String(100), db.ForeignKey('event.ownerid'))

class comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))

