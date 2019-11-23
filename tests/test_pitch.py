import unittest
from app.db_class import User,Pitch
from app import db

class PitchTest(unittest.TestCase):
  '''
  class that tests all functions that relate to pitch
  '''
  def setUp(self):
    '''
    testcase that creates an object pitch
    '''
    # self.user_pyra=User(username="Pyra",pass_word='Lotus',email='pyra@yahoo.com')
    self.new_pitch=Pitch(category='lifestyle',p_title='Life is great',pitch_it='Life is good enjoy it to tha fullest',post='saturday',upvote=20,downvote=10)

  def tearDown(self):
    '''
    testcase that deletes any added object after every test
    '''
    Pitch.query.delete()
    User.query.delete()

  def test_check_instanse(self):
    '''
    testcase to check instanses
    '''
    self.assertEquals(self.new_pitch.category,'lifestyle')
    self.assertEquals(self.new_pitch.p_title,'Life is great')
    self.assertEquals(self.new_pitch.pitch_it,'Life is good enjoy it to tha fullest')
    self.assertEquals(self.new_pitch.post,'saturday')
    self.assertEquals(self.new_pitch.upvote,20)
    self.assertEquals(self.new_pitch.downvote,10)
    # self.assertEquals(self.new_pitch.user,self.user_pyra)

  def test_save(self):
    '''
    testcase that tests if objects are being saved
    '''
    self.new_pitch.save_pitch()
    self.assertTrue(len(Pitch.query.all()>0))

  def test_get_pitch(self):
    '''
    testcase to check if one can get a pitch based on category
    '''
    self.new_pitch.save_pitch()
    got_pitch=Pitch.get_pitches('lifestyle')
    self.assertTrue(len(got_pitch)==1)

    

