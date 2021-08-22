from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relation_hello_v16.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('posts', lazy='dynamic'))  #new

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    # __tablename__ = category
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name



# from hello_v17 import  db,Post,Category
# from sqlalchemy import desc,asc
# cat = Category.query.filter(Category.name.startswith('ma')).first()
# cat.posts
# a.posts.order_by(desc('id')).all()
# a.posts.order_by(desc('id')).limit(1).all()

# >>> cat = Category.query.first()
# >>> cat
# <Category 'Python'>
# >>> cat.posts
# <sqlalchemy.orm.dynamic.AppenderBaseQuery object at 0x7f3aa4840e50>
# >>> cat.posts.all()
# [<Post 'Hello Python!'>, <Post 'Snakes'>]
# >>> cat.posts.first()
# <Post 'Hello Python!'>
# >>> cat.posts.order_by(desc('pub_date'))
# <flask_sqlalchemy.BaseQuery object at 0x7f3aa3ff7d90>
# >>> cat.posts.order_by(desc('pub_date')).all()
# [<Post 'Snakes'>, <Post 'Hello Python!'>]
# >>> cat.posts.order_by(asc('pub_date')).all()


