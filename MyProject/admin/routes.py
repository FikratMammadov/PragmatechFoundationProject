from app import app
from flask import render_template, request, redirect, url_for
from app import db
import os
from admin.forms import LogosForm, LogoUpdateForm,PaymentCardsForm,SocialMediasForm,SalesForm,EmployeesForm
from app.models import ShopContact, Features, Logos,PaymentCards,SocialMedias,Sales,Employees


@app.route('/admin')
def admin_index():
    return render_template('admin/index.html')

# ShopContact routes


@app.route('/admin/shop_contact', methods=['GET', 'POST'])
def admin_shop_contact():
    shopContacts = ShopContact.query.all()
    if request.method == 'POST':
        shopContact = ShopContact(
            contact_icon=request.form['contact_icon'],
            contact_detail=request.form['contact_detail'],
            contact_link=request.form['contact_link']
        )
        db.session.add(shopContact)
        db.session.commit()
        return redirect('/admin/shop_contact')
    return render_template('admin/shop_contact.html', shopContacts=shopContacts)


@app.route('/admin/shop_contact/delete/<int:id>')
def delete_admin_shop_contact(id):
    shopContact = ShopContact.query.get(id)
    db.session.delete(shopContact)
    db.session.commit()
    return redirect('/admin/shop_contact')


@app.route('/admin/shop_contact/update/<int:id>', methods=['GET', 'POST'])
def update_admin_shop_contact(id):
    shopContact = ShopContact.query.get(id)
    if request.method == 'POST':
        shopContact.contact_icon = request.form['contact_icon']
        shopContact.contact_detail = request.form['contact_detail']
        shopContact.contact_link = request.form['contact_link']
        db.session.commit()
        return redirect('/admin/shop_contact')
    return render_template('admin/shop_contact_update.html', shopContact=shopContact)

# Features routes


@app.route('/admin/features', methods=['GET', 'POST'])
def admin_features():
    features = Features.query.all()
    if request.method == 'POST':
        file = request.files['features_image']
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        feature = Features(
            features_image=filename,
            features_title=request.form['features_title'],
            features_content=request.form['features_content']
        )
        db.session.add(feature)
        db.session.commit()
        return redirect('/admin/features')
    return render_template('admin/features.html', features=features)


@app.route('/admin/features/delete/<int:id>')
def delete_admin_features(id):
    feature = Features.query.get(id)
    db.session.delete(feature)
    db.session.commit()
    return redirect('/admin/features')


@app.route('/admin/features/update/<int:id>', methods=['GET', 'POST'])
def update_admin_features(id):
    feature = Features.query.get(id)

    if request.method == 'POST':
        file = request.files['features_image']
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        feature.features_image = filename
        feature.features_title = request.form['features_title']
        feature.features_content = request.form['features_content']
        db.session.commit()
        return redirect('/admin/features')
    return render_template('admin/features_update.html', feature=feature)


# Logos routes

@app.route('/admin/logos', methods=['GET', 'POST'])
def admin_logos():
    logos = Logos.query.all()
    form = LogosForm()
    if request.method == 'POST':
        file = form.l_image.data
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        logo = Logos(
            l_image=filename
        )
        db.session.add(logo)
        db.session.commit()
        return redirect('/admin/logos')
    return render_template('admin/logos.html', form=form, logos=logos)


@app.route('/admin/logos/delete/<int:id>')
def delete_admin_logos(id):
    logo = Logos.query.get(id)
    db.session.delete(logo)
    db.session.commit()
    return redirect('/admin/logos')


@app.route('/admin/logos/update/<int:id>', methods=['GET', 'POST'])
def update_admin_logos(id):
    logo = Logos.query.get(id)
    form = LogoUpdateForm()

    if request.method == 'POST':
        file = form.l_image.data
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        logo.l_image = filename
        db.session.commit()
        return redirect('/admin/logos')

    return render_template('admin/logos_update.html', logo=logo, form=form)

# Payment Cards routes

@app.route('/admin/cards',methods=['GET','POST'])
def admin_cards():
    cards = PaymentCards.query.all()
    form = PaymentCardsForm()
    if request.method=='POST':
        file = form.card_image.data
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        card = PaymentCards(
            card_image=filename
        )
        db.session.add(card)
        db.session.commit()
        return redirect(url_for('admin_cards'))
    return render_template('admin/payment_cards.html',form = form,cards=cards)

@app.route('/admin/cards/delete/<int:id>')
def delete_admin_cards(id):
    card = PaymentCards.query.get(id)
    db.session.delete(card)
    db.session.commit()
    return redirect(url_for('admin_cards'))

@app.route('/admin/cards/update/<int:id>',methods=['GET','POST'])
def update_admin_cards(id):
    card = PaymentCards.query.get(id)
    form = PaymentCardsForm()
    if request.method=='POST':
        file = form.card_image.data
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        card.card_image = filename
        db.session.commit()
        return redirect(url_for('admin_cards'))
    return render_template('admin/payment_cards_update.html',form = form)


# Social Medias routes

@app.route('/admin/social_medias',methods = ['GET','POST'])
def admin_social_medias():
    socialMedias = SocialMedias.query.all()
    form = SocialMediasForm()
    if request.method=='POST':
        socialMedia = SocialMedias(
            social_icon=form.social_icon.data,
            social_url=form.social_url.data
        )
        db.session.add(socialMedia)
        db.session.commit()
        return redirect(url_for('admin_social_medias'))
    return render_template('admin/social_medias.html',form=form,socialMedias=socialMedias)

@app.route('/admin/social_medias/delete/<int:id>')
def delete_admin_social_medias(id):
    socialMedia=SocialMedias.query.get(id)
    db.session.delete(socialMedia)
    db.session.commit()
    return redirect(url_for('admin_social_medias'))

@app.route('/admin/social_medias/update/<int:id>',methods=['GET','POST'])
def update_admin_social_medias(id):
    socialMedia=SocialMedias.query.get(id)
    form = SocialMediasForm()
    if request.method=='POST':
        socialMedia.social_icon=form.social_icon.data
        socialMedia.social_url=form.social_url.data
        db.session.commit()
        return redirect(url_for('admin_social_medias'))
    return render_template('admin/social_medias_update.html',form=form,socialMedia=socialMedia)


# Sales routes

@app.route('/admin/sales',methods=['GET','POST'])
def admin_sales():
    sales = Sales.query.all()
    form = SalesForm()
    if request.method=='POST':
        sale = Sales(
            sales_name = form.sales_name.data,
            sales_icon = form.sales_icon.data,
            sales_number = form.sales_number.data
        )
        db.session.add(sale)
        db.session.commit()
        return redirect(url_for('admin_sales'))
    return render_template('admin/sales.html',form=form,sales=sales)

@app.route('/admin/sales/delete/<int:id>')
def delete_admin_sales(id):
    sale = Sales.query.get(id)
    db.session.delete(sale)
    db.session.commit()
    return redirect(url_for('admin_sales'))

@app.route('/admin/sales/update/<int:id>',methods= ['GET','POST'])
def update_admin_sales(id):
    sale = Sales.query.get(id)
    form = SalesForm()
    if request.method=='POST':
        sale.sales_name = form.sales_name.data
        sale.sales_icon = form.sales_icon.data
        sale.sales_number = form.sales_number.data
        db.session.commit()
        return redirect(url_for('admin_sales'))
    return render_template('admin/sales_update.html',form=form,sale=sale)
    

# Employees routes

@app.route('/admin/employees',methods=['GET','POST'])
def admin_employees():
    employees = Employees.query.all()
    form = EmployeesForm()
    if request.method == 'POST':       
        file = form.e_image.data
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        employee = Employees(
            e_fullname = form.e_fullname.data,
            e_image = filename,
            e_profession = form.e_profession.data
        )
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('admin_employees'))
    return render_template('admin/employees.html',form = form,employees=employees)

@app.route('/admin/employees/delete/<int:id>')
def delete_admin_employees(id):
    employee = Employees.query.get(id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('admin_employees'))

@app.route('/admin/employees/update/<int:id>',methods = ['GET','POST'])
def update_admin_employees(id):
    employee = Employees.query.get(id)
    form = EmployeesForm()
    if request.method=='POST':
        file = form.e_image.data
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        employee.e_fullname = form.e_fullname.data
        employee.e_image = filename
        employee.e_profession = form.e_profession.data
        db.session.commit()
        return redirect(url_for('admin_employees'))
    return render_template('admin/employees_update.html',form=form,employee=employee)