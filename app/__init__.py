from flask import Flask
from flask_bootstrap import Bootstrap


bootstrap=Bootstrap()

# register function
def create_app(config_name):

  app=Flask(__name__)

  from .lead import lead as lead_blueprint
  app.register_blueprint(lead_blueprint)

  return app

