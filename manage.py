from app import create_app,db
from flask_script import Manager,Server
from app.db_class import User,Role,Pitch,Comment

app=create_app('development')

manager=Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
  return dict(app=app,db=db,Role=Role,Pitch=Pitch,Comment=Comment)

if __name__=='__main__':
  manager.run()
  

