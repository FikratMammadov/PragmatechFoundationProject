from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db = SQLAlchemy(app)

class Country(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    country_name = db.Column(db.String(50))
    states = db.relationship('State',backref='country',lazy=True)

class State(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    state_name = db.Column(db.String(50))
    country_id = db.Column(db.Integer,db.ForeignKey('country.id'),nullable = False)

# country routes
@app.route('/',methods=['GET','POST'])
def index():
    countries = Country.query.all()
    if request.method=='POST':
        country=request.form['country_name']
        return redirect(f'/show/states/{country}')
    return render_template('index.html',countries=countries)

@app.route('/show/states/<int:id>')
def show_states(id):
    country = Country.query.get(id)
    states=State.query.filter_by(country_id=country.id)
    return render_template('show_states.html',states=states)


# add country

@app.route('/country/add',methods = ['GET','POST'])
def country_add():
    if request.method=='POST':
        country=Country(
            country_name = request.form['country_name']
        )
        db.session.add(country)
        db.session.commit()
        return redirect('/')
    return render_template('add_country.html')

@app.route('/country/delete/<int:id>',methods=['GET','POST'])
def country_delete():
    return 'country delete'

@app.route('/country/update/<int:id>',methods=['GET','POST'])
def country_update():
     return 'country update'

# add state

@app.route('/state/add',methods=['GET','POST'])
def state_add():
    countries = Country.query.all()
    if request.method=='POST':
        state = State(
            state_name = request.form['state_name'],
            country_id = request.form['country_name']
        )
        db.session.add(state)
        db.session.commit()
        return redirect('/')
    return render_template('add_state.html',countries=countries)

@app.route('/state/delete/<int:id>',methods=['GET','POST'])
def state_delete():
    pass

@app.route('/state/update/<int:id>',methods=['GET','POST'])
def state_update():
    pass

# db.create_all()

if __name__=='__main__':
    app.run(debug=True)