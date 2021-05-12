from app import app
from flask import render_template, request, redirect, url_for
from app import db
import os
from admin.forms import LogosForm, LogoUpdateForm,PaymentCardsForm
from app.models import ShopContact, Features, Logos,PaymentCards


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
def main_cards():
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
        return redirect(url_for('main_cards'))
    return render_template('admin/payment_cards.html',form = form,cards=cards)

@app.route('/admin/cards/delete/<int:id>')
def delete_main_cards(id):
    card = PaymentCards.query.get(id)
    db.session.delete(card)
    db.session.commit()
    return redirect(url_for('main_cards'))

@app.route('/admin/cards/update/<int:id>',methods=['GET','POST'])
def update_main_cards(id):
    card = PaymentCards.query.get(id)
    form = PaymentCardsForm()
    if request.method=='POST':
        file = form.card_image.data
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        card.card_image = filename
        db.session.commit()
        return redirect(url_for('main_cards'))
    return render_template('admin/payment_cards_update.html',form = form)
