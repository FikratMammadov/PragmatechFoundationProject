from app import app
from flask import render_template,request,redirect,url_for
from app import db
from app.models import ShopContact, Features,Logos,PaymentCards

# index route
@app.route('/')
def main_index():
    shopContacts = ShopContact.query.all()
    features = Features.query.all()
    logos = Logos.query.all()
    cards = PaymentCards.query.all()
    return render_template('main/index.html',shopContacts=shopContacts,features = features,logos=logos,cards=cards)


# collection route
@app.route('/collections')
def main_collections():
    shopContacts = ShopContact.query.all()
    cards = PaymentCards.query.all()
    return render_template('main/collection.html',shopContacts=shopContacts)

# shop route
@app.route('/collections/all')
def main_shop():
    shopContacts = ShopContact.query.all()
    return render_template('main/shop.html',shopContacts=shopContacts)

# cookies cakes route
@app.route('/collection/best')
def main_cookies():
    shopContacts = ShopContact.query.all()
    cards = PaymentCards.query.all()
    return render_template('main/cookies.html',shopContacts=shopContacts)

# wedding cakes route

@app.route('/collections/wedding')
def main_wedding():
    shopContacts = ShopContact.query.all()
    cards = PaymentCards.query.all()
    return render_template('main/wedding.html',shopContacts=shopContacts)

# cup cakes route
@app.route('/collections/chocalate')
def main_cupcakes():
    shopContacts = ShopContact.query.all()
    cards = PaymentCards.query.all()
    return render_template('main/cupcakes.html',shopContacts=shopContacts)

# # pages route

@app.route('/pages/aboutus')
def main_aboutus():
    shopContacts = ShopContact.query.all()
    cards = PaymentCards.query.all()
    return render_template('main/pages.html',shopContacts=shopContacts)

