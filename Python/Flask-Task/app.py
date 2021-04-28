from flask import Flask,render_template,request,redirect

app = Flask(__name__)

users=[]
class User():
    def __init__(self,_name,_surname,_email,_city):
        self.ad=_name
        self.soyad = _surname
        self.email = _email
        self.seher = _city

# users.append(User('Fikret','Memmedov','fikret@mail.ru'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add",methods=['GET','POST'])
def add():
    if request.method=='POST':
        _ad = request.form['ad']
        _soyad = request.form['soyad']
        _email = request.form['email']
        _seher=request.form['seher']
        users.append(User(_ad,_soyad,_email,_seher))
        return redirect('/show')
    return render_template('add.html',usr = users)

@app.route("/show")
def show():
    return render_template('show.html',usr = users)

if __name__=='__main__':
    app.run(debug=True)
