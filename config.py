import os

class Config:
  '''
  Class with general configuratiobs for the app
  '''
  

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

  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://pyra:lotus@localhost/pitch'

class TestConfig(Config):
  '''
  test class for running tests
  '''
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://pyra:lotus@localhost/pitch_test'

#------------------------------------------------------------------------------------------------------------------------------------- 
config_options={
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
}

