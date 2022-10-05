from ast import Sub
import email
from tokenize import String
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG','JPG','JPEG','png','jpg','jpeg'}



class DestinationForm(FlaskForm):
    name = StringField('Country', validators=[InputRequired()])
    # adding two validators, one to ensure input is entered and other to check if the 
    #description meets the length requirements
    description = TextAreaField('Description', validators=[InputRequired()])
    image = StringField('Upload Image', validators=[FileRequired(),FileAllowed(ALLOWED_FILE)])
    currency = StringField('Currency', validators=[InputRequired()])
    submit = SubmitField("Create")
    
class CommentForm(FlaskForm):
    text = TextAreaField('Comment', validators=[InputRequired()])
    submit = SubmitField('Post')

class LoginForm(FlaskForm):
    user_name = StringField('Username: ', validators=[InputRequired()])
    password = PasswordField('Password: ', validators=[InputRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    user_name = StringField('Username: ', validators=[InputRequired()])
    email = StringField('Email: ', validators=[InputRequired()])
    password = PasswordField('Password: ', validators=[InputRequired(), EqualTo('confirm', message='Passwords dont match! Please try again')])
    confirm = PasswordField('Confirm Password: ')
    submit = SubmitField('Sign Up!')