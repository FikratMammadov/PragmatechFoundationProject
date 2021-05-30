from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,migrate
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='dededed'

UPLOAD_FOLDER = 'app/static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
migrate = Migrate(app,db)

bc = Bcrypt(app)

# models

from app.models import *

# main routes

from main.routes import *

# admin routes

from admin.routes import *

# auth routes
from auth.routes import *


db.create_all()




