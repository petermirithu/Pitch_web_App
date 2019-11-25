from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..db_class import User


class SignUpForm(FlaskForm):
  '''
  class containing the fields and validation for the sign up form
  '''
  email = StringField('Enter Email Address',validators=[Required(),Email()])
  username=StringField('Enter a Username',validators=[Required()])
  password=PasswordField('Enter a password',validators=[Required(),EqualTo('password_verify',message='Passwords must match')])
  password_verify=PasswordField('Confirm password',validators=[Required()])
  submit=SubmitField('Sign Up')

  # def validate_email(self,data_field):
  #   '''
  #   function that validates no email duplicates
  #   '''
  #   if User.query.filter_by(email=data_field.data).first():
  #     raise ValidationError('That Email is taken.Please use another email')

  # def validate_username(self,data_field):
  #   '''
  #   function that validates no username duplicates
  #   '''
  #   if User.query.filter_by(username=data_field.data).first():
  #     raise ValidationError('That username is taken.Please be creative')

class SignInForm(FlaskForm):
  '''
  class containing fields for a log in to the app
  '''
  username=StringField('Enter your user_name',validators=[Required()])
  password=PasswordField('Enter your password',validators=[Required()])
  remember=BooleanField('Remember me')
  submit=SubmitField('Sign In')
