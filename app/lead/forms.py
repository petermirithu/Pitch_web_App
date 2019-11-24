from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,TextAreaField
from wtforms.validators import Required,Email,EqualTo
class UpdateProfile(FlaskForm):
  '''
  class that defines a form to update our profile page
  '''
  bio=TextAreaField('Tell us about you',validators=[Required()])
  submit=SubmitField('Sumbit')

class PitchForm(FlaskForm):
  '''
  class that defines fields for posting new pitch
  '''
  p_title=StringField('Enter Pitch Title',validators=[Required()])
  pitch_it=TextAreaField('Enter your 60 seconds pitch')
  submit=SubmitField('Post')

class CommentForm(FlaskForm):
  '''
  class that defines fields for posting a new comment
  '''
  p_comment=TextAreaField('Enter your comment',validators=[Required()])
  submit=SubmitField('Post')
