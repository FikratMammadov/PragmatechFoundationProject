from flask import Flask,render_template,request,redirect

app = Flask(__name__)

students=[]
class Student():
    def __init__(self,_name,_surname):
        self.ad = _name
        self.soyad = _surname

# students.append(Student('Mehdi','Suleymanov'))
# students.append(Student('Fikret','Memmedov'))
# students.append(Student('Nicat','Ceferov'))

aboutData={
    'title':'About Page',
    'content':'Lorem ipsum dolor sit amet'
}

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        _ad = request.form['ad']
        _soyad = request.form['soyad']
        students.append(Student(_ad,_soyad))
        return redirect('/about')
    return render_template('index.html',stud = students)

@app.route('/about')
def about():
    return render_template('about.html',stud=students)

@app.route('/contact')
def contact():
    return 'contact page'

if __name__=='__main__':
    app.run(debug=True)
