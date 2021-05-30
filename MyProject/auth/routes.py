from app import app
from flask import render_template, request, redirect, url_for, make_response
from app import db
from datetime import datetime
from app import bc

loginData={
    'username':'admin',
    'password':'admin'
}

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method=='POST':
        if request.form['username']==loginData['username'] and request.form['password']==loginData['password']:
            resp = make_response(redirect(url_for('admin_index')))
            resp.set_cookie('adminLoginStatus','beli')
            return resp
        else:
            return render_template('auth/login.html')
    return render_template('auth/login.html')