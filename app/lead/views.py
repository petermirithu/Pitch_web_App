from flask import render_template,redirect,request,url_for,abort
from . import lead
from flask_login import login_required,current_user
from ..db_class import User,Pitch
from .forms import UpdateProfile,PitchForm
from .. import db,photos


@lead.route('/')
def index():
  '''
  view root page function that returns index page
  '''
  title='Pitches'

  return render_template('index.html',title=title)

@lead.route('/pitch/<category>')
def pitch(category):
  '''
  view function that renders pich template with pitches for that category
  '''
  title=category
  pitches=Pitch.get_pitches(category)
  
  return render_template('pitch.html',title=title,pitches=pitches)

@lead.route('/user/<name>')  
def profile(name):
  '''
  view function to direct users to their profiles
  '''
  user=User.query.filter_by(username=name).first()

  if user is None:
    abort(404)

  return render_template("profile/profile.html",user=user)

@lead.route('/user/<name>/update', methods=['GET','POST'])  
@login_required
def update_profile(name):
  '''
  view function that render an update form to update profile page
  '''
  user = User.query.filter_by(username=name).first()
  if user is None:
    abort(404)  
  form = UpdateProfile()

  if form.validate_on_submit():
    user.bio = form.bio.data

    db.session.add(user)  
    db.session.commit()

    return redirect(url_for('.profile',name=user.username))

  return render_template('profile/update.html',form=form)  


@lead.route('/user/<name>/update/pic',methods=["POST"])
@login_required
def update_pic(name):
  '''
  view function that saves an uploaded photo
  '''
  user=User.query.filter_by(username=name).first()
  if 'photo' in request.files:
    filename=photos.save(request.files['photo'])
    path=f'photos/{filename}'
    user.profile_pic_path = path

    db.session.commit()

  return redirect(url_for('lead.profile',name=name))  

@lead.route('/pitch/new/<category>', methods = ['GET','POST'])
@login_required
def new_pitch(category):
  form=PitchForm()

  category=category
  if form.validate_on_submit():
    p_title=form.p_title.data
    pitch_it=form.pitch_it.data
    username=current_user.username

    print(f'**************************{username}******************')
    new_pitch=Pitch(category=category,p_title=p_title,pitch_it=pitch_it,poster_name=username)
    
    new_pitch.save_pitch()
    return redirect(url_for('.pitch',category = category))

  title="{category}"  
  return render_template('new_pitch.html',title=title,PitchForm=form)

