from run import app
from flask import render_template,redirect,request
@app.route('/')
def main_index():
   return render_template('app/index.html')