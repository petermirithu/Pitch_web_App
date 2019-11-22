import unittest
from app.db_class import User

class UserTest(unittest.TestCase):
  '''
  class with function testing all functions applying to user class in db_class file
  '''
  def setUp(self):
    '''
    creates an object for testing
    '''
    self.new_user=User(password='pyra')

  def test_setting_password(self):
    '''
    testcase for one setting a password
    '''
    self.assertFalse(self.new_user.pass_word is None)

  def test_no_access_to_passwd(self):
    '''
    testcase to see if one can access a password attribute
    '''
    with self.assertRaises(AttributeError):
      self.new_user.pass_word

  def test_password_verify(self):
    '''
    testcase to check verifying of hashed password
    '''
    self.assertTrue(self.new_user.verify_password('pyra'))    

