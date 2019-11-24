from flask import render_template,redirect,request,url_for,abort
from . import lead
from flask_login import login_required,current_user
from ..db_class import User,Pitch,Comment
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db,photos
import markdown2



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
  view function that renders comment template with pitches for that category
  '''
  title=category
  pitches=Pitch.get_pitches(category)
  
  return render_template('pitch.html',title=title,pitches=pitches)

@lead.route('/pitch/comment/<id>')
def comment(id):
  '''
  view function that renders comment template with comments for that pitch
  '''
  pitch=Pitch.query.filter_by(id=id).first()
  pitch_id=pitch.id
  
  title='Comment'
  # comments=Comment.get_comments(id)
    
  return render_template('comment.html',title=title,pitch_id=pitch_id)

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
  '''
  view function that posts a new pitch to a specific category
  '''
  form=PitchForm()

  category=category
  if form.validate_on_submit():
    p_title=form.p_title.data    
    pitch_it=form.pitch_it.data
    pitch_format=markdown2.markdown(pitch_it,extras=["code-friendly", "fenced-code-blocks"])
    username=current_user.username
    
    new_pitch=Pitch(category=category,p_title=p_title,pitch_it=pitch_format,posted_by=username)
    
    new_pitch.save_pitch()
    return redirect(url_for('.pitch',category = category))

  title=category
  return render_template('new_pitch.html',title=title,PitchForm=form)

@lead.route('/pitch/comment/new/<id>')
@login_required
def new_comment(id):
  '''
  view function that registers new comments for a pitch
  '''  
  form=CommentForm()

  if form.validate_on_submit():    
    p_comment=form.p_comment.data

    new_comment=Comment(pitch_id=id,p_comment=p_comment,comment_by=current_user.username)

    new_comment.save_comment()

    return redirect(url_for('lead.index',id=id))

  title='Comment'
  return render_template('new_comment.html',title=title,CommentForm=form)  
