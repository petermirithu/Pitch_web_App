from . import db
from flask_login import UserMixin
from datetime import datetime

# /////////////////////////////////////////////////////////////////////////
class User(UserMixin,db.Model):
  '''
  class with a table defining all the properties for a user
  '''
  __tablename__='usertable'

  id=db.Column(db.Integer, primary_key=True)
  username=db.Column(db.String(20))
  email=db.Column(db.String(30),unique=True,index=True)
  pass_word=db.Column(db.String(20))
  bio=db.Column(db.String(100))
  profile_pic_path=db.Column(db.String())
  post_user=db.Column(db.DateTime,default=datetime.utcnow)
  
  role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
  pitch_id=db.Column(db.Integer,db.Foreignkey('pitchtable.id'))
  comment_id=db.Column(db.Integer,db.ForeignKey('commenttable.id'))


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
