from app import db
class Slider(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    s_title = db.Column(db.String(50))
    s_header = db.Column(db.String(50))
    s_url = db.Column(db.String(50))
    s_photo =db.Column(db.String(50))

class Categories(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    cat_name = db.Column(db.String(50))