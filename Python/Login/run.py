from enum import unique
from flask import Flask, render_template, redirect, request, url_for,make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    fullname = db.Column(db.String(100))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    users=User.query.all()
    if request.method =='POST':
        for user in users:
            if user.username==request.form['username']:
                if user.password == request.form['password']:
                    resp = make_response(render_template('profile.html',user=user))
                    resp.set_cookie('loginStatus', str(user.id))
                    return resp
                else:
                    return redirect('/login')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(
            username=request.form['username'],
            password=request.form['password'],
            email=request.form['email'],
            fullname=request.form['fullname']
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')


@app.route('/profile/<id>')
def profile(id):
    loginStat = request.cookies.get('loginStatus')
    user = User.query.get(id)
    if loginStat == str(user.id):     
        return render_template('profile.html',user=user)
    else:
        return redirect('/login')

@app.route('/logout',methods=['GET','POST'])
def logout():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('loginStatus', 'logout')
    return resp
    

# db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
