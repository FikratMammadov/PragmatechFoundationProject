from app import app
from app.models import Slider
from flask import render_template,redirect,request

@app.route('/')
def main_index():
    slides = Slider.query.all()
    return render_template('main/index.html',slides=slides)

@app.route('/about')
def main_about():
   return render_template('main/about.html')