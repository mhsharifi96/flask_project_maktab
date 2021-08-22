from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relation_hello_v21.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

association_table = db.Table('association', db.Model.metadata,
    db.Column('left_id', db.Integer, db.ForeignKey('left.id')),
    db.Column('right_id', db.Integer, db.ForeignKey('right.id'))
)
class Parent(db.Model):
    __tablename__ = 'left'
    id = db.Column(db.Integer, primary_key=True)
    children = db.relationship("Child",
                    secondary=association_table)

class Child(db.Model):
    __tablename__ = 'right'
    id = db.Column(db.Integer, primary_key=True)


# p = Parent()
# c = Child()
# p.children.append(c)
# db.session.add(p)
# db.session.commit()