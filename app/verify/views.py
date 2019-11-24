from flask import render_template,redirect,url_for,request,flash
from . import verify
from .. import db
from ..db_class import User
from .forms import SignUpForm,SignInForm
from flask_login import login_user,logout_user,login_required,current_user
from ..email import mail_message


@verify.route('/signin',methods=["GET","POST"])
def signin():
  '''
  view function that signs in an existing user
  '''
  LogForm=SignInForm()

  if LogForm.validate_on_submit():
    user=User.query.filter_by(username = LogForm.username.data).first()
    
    if user is None:
      flash('Enter a valid Username')

    elif  user is not None and LogForm.password.data==user.pass_word:

      login_user(user,LogForm.remember.data)

      return redirect(request.args.get('next') or url_for('lead.index'))

    flash('Invalid Password')  

  title ="Sign_In"    
  return render_template('verify/signin.html',LogForm=LogForm,title=title)

@verify.route('/signup', methods= ['GET','POST'])
def signup():
  '''
  view function that signs up new users
  '''
  form =SignUpForm()
  if form.validate_on_submit():
    user = User(email = form.email.data, username=form.username.data,pass_word=form.password.data)
    db.session.add(user)
    db.session.commit()

    mail_message("Welcome to Pitch_web_app","email/welcome_user",user.email,user=user)

    return redirect(url_for('verify.signin'))
    
  return render_template('verify/signup.html',SignUpForm=form)

@verify.route('/signout')
@login_required
def signout():
  '''
  view function tha eneable one  to log out of the app
  '''
  logout_user()
  return redirect(url_for('lead.index'))
