#pylint: skip-file
from . import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager

# /////////////////////////////////////////////////////////////////////////
@login_manager.user_loader
def load_user(user_id):
  '''
  function that queries the database and gets a User with that id
  '''
  return User.query.get(int(user_id))

# /////////////////////////////////////////////////////////////////////////
class User(UserMixin,db.Model):
  '''
  class with a table defining all the properties for a user
  '''
  __tablename__='usertable'

  id=db.Column(db.Integer, primary_key=True)
  username=db.Column(db.String(255),index = True)
  email=db.Column(db.String(255),unique=True,index=True)
  pass_hash=db.Column(db.String())
  bio=db.Column(db.String(255))
  profile_pic_path=db.Column(db.String())
  post_user=db.Column(db.DateTime,default=datetime.utcnow)
  site=db.Column(db.String())
  role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
  pitch=db.relationship('Pitch',backref = 'pitch',lazy='dynamic')
  
  @property
  def password(self):
    '''
    function that raises an attribute error when one tries accesing a password    
    '''
    raise AttributeError('You cannot read the password')

  @password.setter
  def password(self,password):
    '''
    function that generates a hashed password and saves it in the database
    '''
    self.pass_hash=generate_password_hash(password)  

  def verify_password(self,password):
    '''
    function that compares a hashed password and a un hashed password to see if they are same
    '''
    return check_password_hash(self.pass_hash,password)



  def __repr__(self):
    '''
    function that basically helps in debugging
    '''
    return f'User {self.username}'
# /////////////////////////////////////////////////////////////////////////
class Role(db.Model):
  '''
  class that defines role for each user
  '''
  __tablename__='roles'
  id=db.Column(db.Integer, primary_key=True)
  name=db.Column(db.String(255))

  users_A=db.relationship('User',backref='role',lazy="dynamic")

# /////////////////////////////////////////////////////////////////////////
class Pitch(db.Model):
  '''
  class that defines all the properties a pitch should have
  '''
  __tablename__='pitchtable'
  id=db.Column(db.Integer,primary_key=True)
  category=db.Column(db.String())
  p_title=db.Column(db.String())
  pitch_it=db.Column(db.String())
  post=db.Column(db.DateTime,default=datetime.utcnow)
  posted_by=db.Column(db.String())
  upvote=db.Column(db.Integer)
  downvote=db.Column(db.Integer)


  user_id=db.Column(db.Integer,db.ForeignKey("usertable.id"))

  comment=db.relationship('Comment',backref='comment',lazy='dynamic')
  
  def save_pitch(self):
    '''
    function tha saves a new pitch
    '''
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_pitches(cls,category):
    '''
    function that retrives pitches from database
    '''    
    pitches= Pitch.query.filter_by(category=category).all()
    return pitches

  @classmethod
  def get_person_pitches(cls,posted_by):
    '''
    function that returns pitches posted by someone
    '''
    personal_pitch=Pitch.query.filter_by(posted_by=posted_by)
    return personal_pitch
  
    
  def __repr__(self):
    '''
    function that basically helps in debugging
    '''
    return f'Pitch {self.username}'

# /////////////////////////////////////////////////////////////////////////
class Comment(db.Model):
  '''
  class that defines all properties for a comment
  '''
  __tablename__='commenttable'

  id=db.Column(db.Integer,primary_key=True)  
  p_comment=db.Column(db.String(255))
  post_com=db.Column(db.DateTime,default=datetime.utcnow)
  comment_by=db.Column(db.String(255))
  pitch_id=db.Column(db.String(255))
  pitchID=db.Column(db.Integer,db.ForeignKey("pitchtable.id"))

  def save_comment(self):
    '''
    function tha saves a new comment
    '''
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_comments(cls,id):
    '''
    function that retrives comment from database
    '''    
    comments= Comment.query.filter_by(pitch_id=id).all()

    return comments

  def __repr__(self):
    '''
    function that basically helps in debugging
    '''
    return f'Comment {self.username}'
# /////////////////////////////////////////////////////////////////////////
