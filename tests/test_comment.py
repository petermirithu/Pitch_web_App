import unittest
from app.db_class import Comment,Pitch
from app import db

class commentTest(unittest.TestCase):
  '''
  class that tests all functions that relate to pitch
  '''
  def setUp(self):
    '''
    testcase that creates an object pitch
    '''    
    self.new_pitch=Pitch(category='lifestyle',p_title='Life is great',pitch_it='Life is good enjoy it to tha fullest',post='saturday',posted_by='pyra',upvote=20,downvote=10)
    self.new_comment=Comment(id=1,p_comment='Nice work',post_com=2019-3-12,comment_by='pyra',pitch_id=4,PITCHID=4)
  def tearDown(self):
    '''
    testcase that deletes any added object after every test
    '''
    Pitch.query.delete()
    Comment.query.delete()

  def test_check_instanse(self):
    '''
    testcase to check instanses
    '''
    self.assertEquals(self.new_comment.id,1)
    self.assertEquals(self.new_comment.p_comment,'Nice work')
    self.assertEquals(self.new_comment.post_com,2019-3-12)
    self.assertEquals(self.new_comment.comment_by,'pyra')
    self.assertEquals(self.new_comment.pitch_id,4)
    self.assertEquals(self.new_comment.pitchID,4)

    self.assertEquals(self.new_comment.pitch_id,self.new_pitch.id)

  def test_save(self):
    '''
    testcase that tests if objects are being saved
    '''
    self.new_comment.save_comment()
    self.assertTrue(len(Comment.query.all()>0))

  def test_get_comment(self):
    '''
    testcase to check if one can get a comment based on picth_id
    '''
    self.new_comment.save_comment()
    got_comment=Comment.get_comments('4')
    self.assertTrue(len(got_comment)==4)

    

