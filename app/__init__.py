from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_simplemde import SimpleMDE
from flask_mail import Mail


login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='verify.login'

photos=UploadSet('photos',IMAGES)

simple=SimpleMDE()

mail=Mail()


bootstrap=Bootstrap()

db=SQLAlchemy()

# register function
def create_app(config_name):
  '''
  function that registers all blueprints and instances of imports
  '''
  app=Flask(__name__)

  app.config.from_object(config_options[config_name])


  bootstrap.init_app(app)

  db.init_app(app)

  login_manager.init_app(app)
  
  configure_uploads(app,photos)

  simple.init_app(app)

  mail.init_app(app)

  from .lead import lead as lead_blueprint
  app.register_blueprint(lead_blueprint)

  from .verify import verify as verify_blueprint
  app.register_blueprint(verify_blueprint,url_prefix='/authenticate')


  return app

