from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relation_hello_v22.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

registrations = db.Table('registrations',
        db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
        db.Column('class_id', db.Integer, db.ForeignKey('class.id'))
    )
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    classes = db.relationship('Class',secondary=registrations,backref=db.backref('students', lazy='dynamic'),lazy='dynamic')

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


# from hello_v23 import  Class ,Student 

# s = Student(name='mohammad')
# c = Class(name='maktab')
# s.classes.append(c)
# db.session.add(s)
# s2 = Student(name='sh')
# c.students.append(s2)
# db.session.add(c)
# db.session.commit

# q_c = Class.query.first()
# q_c.students
# q_c.students.all()

# q_s = Student.query.first()
# q_s.classes.all()

# ref : https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/