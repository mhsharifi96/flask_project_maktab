

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  #current dir
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'hello_v14.sqlite') #current dir
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username



# run python command in terminal/cmd
# and then run below commands :
# from hello_v14 import db
# db.create_all()

# from yourapplication import User
# admin = User(username='admin', email='admin@example.com')
# guest = User(username='guest', email='guest@example.com')


# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()
# User.query.all()
# User.query.filter_by(username='admin').first()