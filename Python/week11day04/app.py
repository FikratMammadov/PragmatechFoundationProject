from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db=SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    f_name=db.Column(db.String(50))
    l_name=db.Column(db.String(50))

# id,f_name,l_name

@app.route('/')
def index():
    #select * from user
    users=User.query.all()

    return render_template('index.html',users=users)

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        user = User(
            f_name = request.form['f_name'],
            l_name = request.form['l_name']
        )
        db.session.add(user) # user obyektini table a eleva etdik
        db.session.commit() # yazilan emrlerin database-e tetbiqi
        return redirect('/')
    return render_template('add.html')

@app.route('/delete/<id>')
def delete(id):
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/')

@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
    user=User.query.get(id)
    if request.method=='POST':
        user.f_name = request.form['f_name']
        user.l_name = request.form['l_name']
        db.session.commit()
        return redirect('/')
    return render_template('update.html',user=user)

if __name__=='__main__':
    app.run(debug=True)