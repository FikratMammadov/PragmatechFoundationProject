from app import app
from flask import render_template,request,redirect
from app import db
from app.models import ShopContact

# index route
@app.route('/')
def main_index():
    shopContacts = ShopContact.query.all()
    return render_template('main/index.html',shopContacts=shopContacts)
