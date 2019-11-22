import os

class Config:
  '''
  Class with general configuratiobs for the app
  '''
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://pyra:lotus@localhost/pitch'

class ProdConfig(Config):
  '''
  Production configurations child class
  '''
  pass

class DevConfig(Config):
  '''
  Development configuration child class
  '''

  DEBUG=True 

config_options={
  'development':DevConfig,
  'production':ProdConfig  
}

