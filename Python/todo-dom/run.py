from flask import Flask,request,render_template,redirect

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    formData=''
    if request.method=='POST':
        name=request.form['ad']
        formData=name
        return render_template('index.html',data=formData)
    return render_template('index.html',data=formData)

@app.route("/about",methods=['GET','POST'])
def about():
    return render_template('about.html',data='This is about page')

if __name__ == '__main__':
    app.run(debug=True)
