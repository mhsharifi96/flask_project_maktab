# pip install flask-sqlalchemy
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relation_hello_v15.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
  
    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name




# python 
# import application then create db with create_db
# if you need drop db just run drop_db 
# import your model (Post/Category)
# e.x : 
# maktab_cat = Category(name='maktab52')
# lang_cat = Category()
# lang_cat.name = "python"
# 
# db.session.add(maktab_cat) 
# db.session.add(lang_cat)
# db.session.commit()
# 
# Category.query.filter_by(name="python").first()
# Category.query.filter_by(name="maktab52").one()
# print(Category.query.filter_by(name="maktab52")) #show raw query
# Category.query.filter(Category.name == "python").all()

# first_post = Post(title= 'fist post for test',body="hi")
# db.session.add(first_post)
# db.session.commit()    #OOPPPPSSS :|

# first_post = Post(title= 'fist post for test',body="hi",category_id = 1)

# python_cat = Category.query.filter_by(name="python").first()
# second_post = Post()
# second_post.title = "second"
# second_post.body = "second"
# second_post.category = python_cat
# db.session.add(second_post)
# db.session.commit()   #OOPPPPSSS :|

