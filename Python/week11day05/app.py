from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'

UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

db = SQLAlchemy(app)

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    p_title = db.Column(db.String(100))
    p_content = db.Column(db.Text)
    p_img=db.Column(db.String(100))
    p_date = db.Column(db.String(100))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        file = request.files['p_img']
        file_name=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],file_name))
        post=Post(
            p_title=request.form['p_title'],
            p_content=request.form['p_content'],
            p_img=file_name,
            p_date=request.form['p_date']
        )

        db.session.add(post)
        db.session.commit()
        return redirect('/')
    return render_template('add.html')



if __name__=='__main__':
    app.run(debug=True)