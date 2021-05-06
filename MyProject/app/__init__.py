from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db = SQLAlchemy(app)

# models

from app.models import *

# main routes

from main.routes import *

# admin routes

from admin.routes import *




