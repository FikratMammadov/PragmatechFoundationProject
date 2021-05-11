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
