from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db) #new

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))





# export FLASK_APP=<application name>
# export FLASK_APP=hello_v19
# flask db init
# flask db migrate -m "Initial migration."
# flask db upgrade
# flask db --help