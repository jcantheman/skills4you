from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.fields.core import  IntegerField, SelectField
from wtforms.fields.simple import FileField
from wtforms.validators import InputRequired, Email
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.fields.html5 import DateField





class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    password=PasswordField("Password", validators=[InputRequired()])
    address=StringField("Address", validators=[InputRequired()])
    contact=StringField("Contact Number", validators=[InputRequired()])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")



class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')

ALLOWED_FILE = {'PNG','JPG','png','jpg'}
choices = ["", "Art", "Cooking", "Fitness", "Technology"]

class CreateForm(FlaskForm):
  title = StringField('Event Name:', validators=[InputRequired()])
  description = TextAreaField('Event Description:', validators=[InputRequired()])
  image = FileField('Destination Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports jpeg, png,jpg,JPG,PNG')])  
  date = DateField('Date', validators=[InputRequired()])
  location = StringField('Event Location:', validators=[InputRequired()])
  category = SelectField('Category', choices = choices, validators=[InputRequired()])
  tickets = StringField('Maximum Ticket Amount:', validators=[InputRequired()])
  submit = SubmitField("Create Event")

class BookingForm(FlaskForm):
  ticketbook = StringField('Enter a Ticket Amount', validators=[InputRequired()])
  submit = SubmitField("Confirm Booking")

class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')