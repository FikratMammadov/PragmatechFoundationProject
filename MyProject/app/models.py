from app import db

class ShopContact(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    contact_icon = db.Column(db.String(100))
    contact_detail = db.Column(db.String(100))
    contact_link = db.Column(db.String(150))

class Features(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    features_image = db.Column(db.String(100))
    features_title = db.Column(db.String(100))
    features_content = db.Column(db.String(100))

class Logos(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    l_image=db.Column(db.String(100))

class PaymentCards(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    card_image=db.Column(db.String(100))

class SocialMedias(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    social_icon=db.Column(db.String(100))
    social_url=db.Column(db.String(100))

class Sales(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    sales_name = db.Column(db.String(50))
    sales_icon = db.Column(db.String(50))
    sales_number = db.Column(db.String(50))
