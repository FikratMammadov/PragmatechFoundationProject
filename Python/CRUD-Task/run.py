from flask import Flask,render_template,request,redirect

app = Flask(__name__)

kitablar=[]
id=1

class Kitab():
    def __init__(self,_id,_name,_price,_author):
        self.id=_id
        self.ad=_name
        self.qiymet=_price
        self.yazici=_author

@app.route("/")
def index():
    return render_template('index.html',books=kitablar)

@app.route('/add',methods=['GET','POST'])
def add():
    global id
    if request.method=='POST':
        if len(kitablar)==0:
            id=1
        _ad=request.form['ad']
        _qiymet = request.form['qiymet']
        _yazici=request.form['yazici']
        kitab = Kitab(id,_ad,_qiymet,_yazici)
        kitablar.append(kitab)
        id+=1
        return redirect('/')
    return render_template('add.html')

@app.route('/delete/<int:id>')
def delete(id):
    for kitab in kitablar:
        if kitab.id==id:
            kitablar.remove(kitab)
            return redirect('/')
    return redirect('/')

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    secilmisKitab=None
    for kitab in kitablar:
        if kitab.id==id:
            secilmisKitab = kitab
    if request.method=='POST':
        secilmisKitab.ad=request.form['ad']
        secilmisKitab.qiymet = request.form['qiymet']
        secilmisKitab.yazici=request.form['yazici']
        return redirect('/')
    return render_template('update.html',_secilmisKitab=secilmisKitab)
     
if __name__=='__main__':
    app.run(debug=True)