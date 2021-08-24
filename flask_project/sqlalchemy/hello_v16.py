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
    category = db.relationship('Category',backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    # __tablename__ = category
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name


# The first argument to db.relationship() indicates what model is on the other
# side of the relationship. The model class can be provided as a string if the class is
# defined later in the module.
# The backref argument to db.relationship() defines the reverse direction of the
# relationship, by adding a role attribute to the User model. This attribute can be used
# on any instance of User instead of the role_id foreign key to access the Role model
# as an object.


#  py = Category(name='Python')
#  Post(title='Hello Python!', body='Python is pretty cool', category=py)
#  p = Post(title='Snakes', body='Ssssssss')
#  py.posts.append(p)
#  db.session.add(py)
#  py.posts

#  from sqlalchemy.orm import joinedload
#  query = Category.query.options(joinedload('posts'))
#  for category in query:
# ...     print category, category.posts
#  Post.query.with_parent(py).filter(Post.title != 'Snakes').all()


# >>> from sqlalchemy import desc,asc
# >>> Category.query.order_by(desc('name')).all()
# >>> Category.query.order_by(asc('name')).all()
# >>> Category.query.order_by(asc('id')).all()
# >>> Category.query.order_by(desc('id')).all()
# >>> Category.query.order_by(asc(Category.name)).all()
# >>> Category.query.order_by(desc(Category.name)).all()


# Category.query.get(1)  #primary key

#Post.query.filter_by(title='python').first_or_404()


# db.session.delete(py) #delete records on db

# category = Category.query.get(1)
# category.posts query here has a small problem
# category.posts.order_by(desc('id'))

# search = "%{}%".format('p')
posts = Post.query.filter(Post.title.like(search)).all()


# ref : https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/

# SQLAlchemy’s “Lazy” Parameter
# https://medium.com/@ns2586/sqlalchemys-relationship-and-lazy-parameter-4a553257d9ef#:~:text=lazy%20%3D%20'subquery'%20and%20lazy,they%20joins%20the%20tables%20differently.


#what is diff between filter and filter_by ?
# https://stackoverflow.com/questions/2128505/difference-between-filter-and-filter-by-in-sqlalchemy


# Object Relational Tutoria
#   https://docs.sqlalchemy.org/en/14/orm/tutorial.html#common-filter-operators
