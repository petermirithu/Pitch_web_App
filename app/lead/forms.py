from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,TextAreaField
from wtforms.validators import Required,Email,EqualTo
class UpdateProfile(FlaskForm):
  '''
  class that defines a form to update our profile page
  '''
  bio=TextAreaField('Tell us about you',validators=[Required()])
  submit=SubmitField('Sumbit')