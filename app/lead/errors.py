from flask import render_template
from . import lead

@lead.app_errorhandler(404)
def four_ow_four(error):
  '''
  renders 404 page
  '''
  return render_template('fourowfour.html'),404

@lead.app_errorhandler(500)
def internal_server(error):
  '''
  renders sign in page
  '''
  return render_template('internalServer.html'),500
