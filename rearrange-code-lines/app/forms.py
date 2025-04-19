''' Forms for when User has to enter details '''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, EqualTo, Length, Regexp
from app.constants import *

class RegistrationForm(FlaskForm):
	id = StringField('ID', validators=[InputRequired(), Regexp(r"20\d\dA\d\d?[PT]S\d\d\d\dU")])
	username = StringField('Username (use your name)', validators=[InputRequired(), Length(min=4, max=30)])
	language = SelectField('Programming Language', coerce=str, choices=list(SUPPORTED_LANGS), validate_choice=False)
	password = PasswordField('Password', validators=[InputRequired(), Length(min=6)])
	confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
	submit = SubmitField('Register')

class LoginForm(FlaskForm):
	id = StringField('ID', validators = [InputRequired()])
	password = PasswordField('Password', validators = [InputRequired()])
