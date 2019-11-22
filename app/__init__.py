from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy



bootstrap=Bootstrap()

db=SQLAlchemy()

# register function
def create_app(config_name):

  app=Flask(__name__)

  bootstrap.init_app(app)
  db.init_app(app)
  
  
  app.config.from_object(config_options[config_name])

  from .lead import lead as lead_blueprint
  app.register_blueprint(lead_blueprint)

  return app

