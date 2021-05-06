from app import db

class ShopContact(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    contact_icon = db.Column(db.String(100))
    contact_detail = db.Column(db.String(100))
