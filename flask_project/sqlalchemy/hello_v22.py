from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relation_hello_v22.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

student_identifier = db.Table('student_identifier',
    db.Column('class_id', db.Integer, db.ForeignKey('classes.class_id')),
    db.Column('user_id', db.Integer, db.ForeignKey('students.user_id'))
)

class Student(db.Model):
    __tablename__ = 'students'
    user_id = db.Column(db.Integer, primary_key=True)
    user_fistName = db.Column(db.String(64))
    user_lastName = db.Column(db.String(64))
    user_email = db.Column(db.String(128), unique=True)


class Class(db.Model):
    __tablename__ = 'classes'
    class_id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(128), unique=True)
    students = db.relationship("Student",
                               secondary=student_identifier)




# s = Student()
# c = Class()
# c.students.append(s)
# db.session.add(c)
# db.session.commit()