from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
UPLOAD_FOLDER = 'app/static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db=SQLAlchemy(app)

#models

from app.models import *


#admin routes

from admin.routes import *


#main routes

from main.routes import *

