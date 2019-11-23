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
  username=db.Column(db.String(20),unique=True,index = True)
  email=db.Column(db.String(30),unique=True,index=True)
  pass_word=db.Column(db.String(20))
  bio=db.Column(db.String(100))
  profile_pic_path=db.Column(db.String())
  post_user=db.Column(db.DateTime,default=datetime.utcnow)
  
  role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
  pitch_id=db.Column(db.Integer,db.ForeignKey('pitchtable.id'))
  comment_id=db.Column(db.Integer,db.ForeignKey('commenttable.id'))

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
    self.pass_word=generate_password_hash(password)  

  def verify_password(self,password):
    '''
    function that compares a hashed password and a un hashed password to see if they are same
    '''
    return check_password_hash(self.pass_word,password)



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
  name=db.Column(db.String(20))

  users_A=db.relationship('User',backref='role',lazy="dynamic")

# /////////////////////////////////////////////////////////////////////////
class Pitch(db.Model):
  '''
  class that defines all the properties a pitch should have
  '''
  __tablename__='pitchtable'
  id=db.Column(db.Integer,primary_key=True)
  category=db.Column(db.String(20))
  p_title=db.Column(db.String(100))
  pitch_it=db.Column(db.String(255))
  post=db.Column(db.DateTime,default=datetime.utcnow)
  upvote=db.Column(db.Integer)
  downvote=db.Column(db.Integer)

  user_B=db.relationship('User',backref='pitch',lazy="dynamic")

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
  pitch_id=db.Column(db.Integer)
  pitch_title=db.Column(db.String(100))
  p_comment=db.Column(db.String(200))
  post_com=db.Column(db.DateTime,default=datetime.utcnow)

  user_c=db.relationship('User',backref='comment',lazy="dynamic")

  def __repr__(self):
    '''
    function that basically helps in debugging
    '''
    return f'Comment {self.username}'
# /////////////////////////////////////////////////////////////////////////
