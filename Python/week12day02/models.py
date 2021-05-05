from run import db

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    post_title = db.Column(db.String(50))
    post_img=db.Column(db.String(50))
    post_info=db.Column(db.String(50))
