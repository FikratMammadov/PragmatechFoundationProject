from flask import Flask,render_template,redirect,request

app=Flask(__name__)
id=1
users=[]
class User():
    def __init__(self,_id,_name):
        self.id=_id
        self.ad=_name



@app.route('/')
def index():
    return render_template('index.html',istifadeciler=users)

@app.route('/add',methods=['GET','POST'])
def add():
    global id
    if request.method=='POST':
        if len(users)==0:
            id=1
        user=User(id,request.form['ad'])
        users.append(user)
        id+=1
        return redirect('/')
     
    return render_template('add.html')

@app.route('/delete/<int:id>')
def delete(id):
    for user in users:
        if user.id==id:
            users.remove(user)
            return redirect('/')
    return redirect('/')



if __name__=='__main__':
    app.run(debug=True)