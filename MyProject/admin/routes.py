from app import app
from flask import render_template,request,redirect
from app import db
from app.models import ShopContact

@app.route('/admin')
def admin_index():
    return render_template('admin/index.html')

@app.route('/admin/shop_contact',methods = ['GET','POST'])
def admin_shop_contact():
    shopContacts = ShopContact.query.all()
    if request.method=='POST':
        shopContact = ShopContact(
            contact_icon = request.form['contact_icon'],
            contact_detail=request.form['contact_detail']
        )
        db.session.add(shopContact)
        db.session.commit()
        return redirect('/admin/shop_contact')
    return render_template('admin/shop_contact.html',shopContacts=shopContacts)

@app.route('/admin/shop_contact/delete/<int:id>')
def delete_admin_shop_contact(id):
    shopContact=ShopContact.query.get(id)
    db.session.delete(shopContact)
    db.session.commit()
    return redirect('/admin/shop_contact')

@app.route('/admin/shop_contact/update/<int:id>',methods=['GET','POST'])
def update_admin_shop_contact(id):
    shopContact=ShopContact.query.get(id)
    if request.method=='POST':
        shopContact.contact_icon=request.form['contact_icon']
        shopContact.contact_detail = request.form['contact_detail']
        db.session.commit()
        return redirect('/admin/shop_contact')
    return render_template('admin/shop_contact_update.html',shopContact=shopContact)

