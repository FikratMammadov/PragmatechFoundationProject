from app import app
from app import db
from app.models import Slider
import os
from flask import render_template,request,redirect

@app.route('/admin')
def admin_index():
    return render_template('admin/index.html')

# slider routes

@app.route('/admin/slider',methods = ['GET','POST'])
def admin_slider():
    slides = Slider.query.all()
    if request.method=='POST':
        file = request.files['s_photo']
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        slide = Slider(
            s_title = request.form['s_title'],
            s_header = request.form['s_header'],
            s_url = request.form['s_url'],
            s_photo = filename
        )

        db.session.add(slide)
        db.session.commit()
        return redirect('/admin/slider')
    return render_template('admin/slider.html',slides = slides)