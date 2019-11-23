from flask import render_template
from . import lead
from flask_login import login_required,current_user


@lead.route('/')
def index():
  '''
  view root page function that returns index page
  '''
  title='Pitches'

  return render_template('index.html',title=title)
  