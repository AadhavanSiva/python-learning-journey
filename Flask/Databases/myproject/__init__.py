import os
from basicprojects.forms import AddForm, DelForm
from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MOODIFICATION'] = False
SECRET_KEY = "mk"
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)

Migrate(app,db)