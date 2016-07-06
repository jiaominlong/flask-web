from app import app
from app.models import db, User
from flask_script import Manager
import datetime

manager = Manager(app)

@manager.command
def test():
    print('Hello World!')


@manager.command
def init_db():
    db.create_all()

@manager.command
def drop_db():
    db.drop_all()

@manager.command
def save():
    user = User(username='jiaominlong', password="jiaominlong", time=datetime.datetime.now())
    db.session.add(user)
    db.session.commit()



if __name__ == '__main__':
    manager.run()