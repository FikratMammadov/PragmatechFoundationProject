from app import app
from flask import render_template, request, redirect, url_for
from app import db
import os
from admin.forms import LogosForm, LogoUpdateForm, PaymentCardsForm, SocialMediasForm, SalesForm, EmployeesForm, ProductSizeForm, ProductForm, ProductAvailabilityForm,ProductCategoryForm,ProductTypeForm,ProductBrandForm,ProductImageForm
from app.models import ShopContact, Features, Logos, PaymentCards, SocialMedias, Sales, Employees, Product, ProductSize, ProductAvailability,ProductCategory,ProductType,ProductBrand,ProductImage


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


@app.route('/admin/cards', methods=['GET', 'POST'])
def admin_cards():
    cards = PaymentCards.query.all()
    form = PaymentCardsForm()
    if request.method == 'POST':
        file = form.card_image.data
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        card = PaymentCards(
            card_image=filename
        )
        db.session.add(card)
        db.session.commit()
        return redirect(url_for('admin_cards'))
    return render_template('admin/payment_cards.html', form=form, cards=cards)


@app.route('/admin/cards/delete/<int:id>')
def delete_admin_cards(id):
    card = PaymentCards.query.get(id)
    db.session.delete(card)
    db.session.commit()
    return redirect(url_for('admin_cards'))


@app.route('/admin/cards/update/<int:id>', methods=['GET', 'POST'])
def update_admin_cards(id):
    card = PaymentCards.query.get(id)
    form = PaymentCardsForm()
    if request.method == 'POST':
        file = form.card_image.data
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        card.card_image = filename
        db.session.commit()
        return redirect(url_for('admin_cards'))
    return render_template('admin/payment_cards_update.html', form=form)


# Social Medias routes

@app.route('/admin/social_medias', methods=['GET', 'POST'])
def admin_social_medias():
    socialMedias = SocialMedias.query.all()
    form = SocialMediasForm()
    if request.method == 'POST':
        socialMedia = SocialMedias(
            social_icon=form.social_icon.data,
            social_url=form.social_url.data
        )
        db.session.add(socialMedia)
        db.session.commit()
        return redirect(url_for('admin_social_medias'))
    return render_template('admin/social_medias.html', form=form, socialMedias=socialMedias)


@app.route('/admin/social_medias/delete/<int:id>')
def delete_admin_social_medias(id):
    socialMedia = SocialMedias.query.get(id)
    db.session.delete(socialMedia)
    db.session.commit()
    return redirect(url_for('admin_social_medias'))


@app.route('/admin/social_medias/update/<int:id>', methods=['GET', 'POST'])
def update_admin_social_medias(id):
    socialMedia = SocialMedias.query.get(id)
    form = SocialMediasForm()
    if request.method == 'POST':
        socialMedia.social_icon = form.social_icon.data
        socialMedia.social_url = form.social_url.data
        db.session.commit()
        return redirect(url_for('admin_social_medias'))
    return render_template('admin/social_medias_update.html', form=form, socialMedia=socialMedia)


# Sales routes

@app.route('/admin/sales', methods=['GET', 'POST'])
def admin_sales():
    sales = Sales.query.all()
    form = SalesForm()
    if request.method == 'POST':
        sale = Sales(
            sales_name=form.sales_name.data,
            sales_icon=form.sales_icon.data,
            sales_number=form.sales_number.data
        )
        db.session.add(sale)
        db.session.commit()
        return redirect(url_for('admin_sales'))
    return render_template('admin/sales.html', form=form, sales=sales)


@app.route('/admin/sales/delete/<int:id>')
def delete_admin_sales(id):
    sale = Sales.query.get(id)
    db.session.delete(sale)
    db.session.commit()
    return redirect(url_for('admin_sales'))


@app.route('/admin/sales/update/<int:id>', methods=['GET', 'POST'])
def update_admin_sales(id):
    sale = Sales.query.get(id)
    form = SalesForm()
    if request.method == 'POST':
        sale.sales_name = form.sales_name.data
        sale.sales_icon = form.sales_icon.data
        sale.sales_number = form.sales_number.data
        db.session.commit()
        return redirect(url_for('admin_sales'))
    return render_template('admin/sales_update.html', form=form, sale=sale)


# Employees routes

@app.route('/admin/employees', methods=['GET', 'POST'])
def admin_employees():
    employees = Employees.query.all()
    form = EmployeesForm()
    if request.method == 'POST':
        file = form.e_image.data
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        employee = Employees(
            e_fullname=form.e_fullname.data,
            e_image=filename,
            e_profession=form.e_profession.data
        )
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('admin_employees'))
    return render_template('admin/employees.html', form=form, employees=employees)


@app.route('/admin/employees/delete/<int:id>')
def delete_admin_employees(id):
    employee = Employees.query.get(id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('admin_employees'))


@app.route('/admin/employees/update/<int:id>', methods=['GET', 'POST'])
def update_admin_employees(id):
    employee = Employees.query.get(id)
    form = EmployeesForm()
    if request.method == 'POST':
        file = form.e_image.data
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        employee.e_fullname = form.e_fullname.data
        employee.e_image = filename
        employee.e_profession = form.e_profession.data
        db.session.commit()
        return redirect(url_for('admin_employees'))
    return render_template('admin/employees_update.html', form=form, employee=employee)


# Product Routes
@app.route('/admin/product', methods=['GET', 'POST'])
def admin_product():
    form = ProductForm()
    productSizes = ProductSize.query.all()
    products = Product.query.all()
    avas = ProductAvailability.query.all()
    categories = ProductCategory.query.all()
    types = ProductType.query.all()
    brands = ProductBrand.query.all()
    if request.method == 'POST':
        file = form.p_img.data
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        product = Product(
            p_name=form.p_name.data,
            p_price=form.p_price.data,
            p_quantity=form.p_quantity.data,
            p_content=form.p_content.data,
            p_img = filename,
            p_size_id=request.form['p_size_id'],
            p_availability_id = request.form['p_availability_id'],
            p_category_id= request.form['p_category_id'],
            p_type_id=request.form['p_type_id'],
            p_brand_id=request.form['p_brand_id']
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('admin_product'))
    return render_template('admin/product.html', form=form, productSizes=productSizes, products=products,
     ProductSize=ProductSize, avas=avas, ProductAvailability=ProductAvailability,categories=categories,
     ProductCategory=ProductCategory,types=types,ProductType=ProductType,brands=brands,ProductBrand=ProductBrand)


@app.route('/admin/product/delete/<int:id>')
def delete_admin_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('admin_product'))


@app.route('/admin/product/update/<int:id>', methods=['GET', 'POST'])
def update_admin_product(id):
    product = Product.query.get(id)
    form = ProductForm()
    productSizes = ProductSize.query.all()
    avas = ProductAvailability.query.all()
    categories = ProductCategory.query.all()
    types = ProductType.query.all()
    brands = ProductBrand.query.all()
    if request.method == 'POST':
        file = form.p_img.data
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        product.p_name = form.p_name.data
        product.p_price = form.p_price.data
        product.p_quantity = form.p_quantity.data
        product.p_content = form.p_content.data
        product.p_img = filename
        product.p_size_id = request.form['p_size_id']
        product.p_availability_id=request.form['p_availability_id']
        product.p_category_id=request.form['p_category_id']
        product.p_type_id=request.form['p_type_id']
        product.p_brand_id=request.form['p_brand_id']
        db.session.commit()
        return redirect(url_for('admin_product'))
    return render_template('admin/product_update.html', form=form, product=product,
     productSizes=productSizes,avas=avas,categories=categories,types=types,brands=brands)


# Product Size Routes
@app.route('/admin/product/size', methods=['GET', 'POST'])
def admin_product_size():
    form = ProductSizeForm()
    productSizes = ProductSize.query.all()
    if request.method == 'POST':
        size = ProductSize(
            s_name=form.s_name.data
        )
        db.session.add(size)
        db.session.commit()
        return redirect(url_for('admin_product_size'))
    return render_template('admin/product_size.html', form=form, productSizes=productSizes)


@app.route('/admin/product/size/delete/<int:id>')
def delete_admin_product_size(id):
    productSize = ProductSize.query.get(id)
    db.session.delete(productSize)
    db.session.commit()
    return redirect(url_for('admin_product_size'))


@app.route('/admin/product/size/update/<int:id>', methods=['GET', 'POST'])
def update_admin_product_size(id):
    productSize = ProductSize.query.get(id)
    form = ProductSizeForm()
    if request.method == 'POST':
        productSize.s_name = form.s_name.data
        db.session.commit()
        return redirect(url_for('admin_product_size'))
    return render_template('admin/product_size_update.html', form=form, productSize=productSize)

# Product Availability Routes


@app.route('/admin/product/availability', methods=['GET', 'POST'])
def admin_product_availability():
    form = ProductAvailabilityForm()
    avas = ProductAvailability.query.all()
    if request.method == 'POST':
        ava = ProductAvailability(
            pa_name=form.pa_name.data
        )
        db.session.add(ava)
        db.session.commit()
        return redirect(url_for('admin_product_availability'))
    return render_template('admin/product_availability.html', form=form, avas=avas)


@app.route('/admin/product/availability/delete/<int:id>')
def delete_admin_product_availability(id):
    ava = ProductAvailability.query.get(id)
    db.session.delete(ava)
    db.session.commit()
    return redirect(url_for('admin_product_availability'))


@app.route('/admin/product/availability/update/<int:id>', methods=['GET', 'POST'])
def update_admin_product_availability(id):
    form = ProductAvailabilityForm()
    ava = ProductAvailability.query.get(id)
    if request.method == 'POST':
        ava.pa_name = form.pa_name.data
        db.session.commit()
        return redirect(url_for('admin_product_availability'))
    return render_template('admin/product_availability_update.html', form=form, ava=ava)

# Product Category Routes

@app.route('/admin/product/category', methods=['GET', 'POST'])
def admin_product_category():
    form = ProductCategoryForm()
    categories = ProductCategory.query.all()
    if request.method=='POST':
        category = ProductCategory(
            cat_name=form.cat_name.data
        )
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('admin_product_category'))
    return render_template('admin/product_category.html',form=form,categories=categories)

@app.route('/admin/product/category/delete/<int:id>')
def delete_admin_product_category(id):
    category = ProductCategory.query.get(id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('admin_product_category'))

@app.route('/admin/product/category/update/<int:id>', methods=['GET', 'POST'])
def update_admin_product_category(id):
    form = ProductCategoryForm()
    category = ProductCategory.query.get(id)
    if request.method=='POST':
        category.cat_name=form.cat_name.data
        db.session.commit()
        return redirect(url_for('admin_product_category'))
    return render_template('admin/product_category_update.html',form=form,category=category)

# Product Type Routes
@app.route('/admin/product/type', methods=['GET', 'POST'])
def admin_product_type():
    form = ProductTypeForm()
    types = ProductType.query.all()
    if request.method=='POST':
        type = ProductType(
            type_name = form.type_name.data
        )
        db.session.add(type)
        db.session.commit()
        return redirect(url_for('admin_product_type'))
    return render_template('admin/product_type.html',form=form,types=types)

@app.route('/admin/product/type/delete/<int:id>')
def delete_admin_product_type(id):
    type = ProductType.query.get(id)
    db.session.delete(type)
    db.session.commit()
    return redirect(url_for('admin_product_type'))

@app.route('/admin/product/type/update/<int:id>', methods=['GET', 'POST'])
def update_admin_product_type(id):
    type = ProductType.query.get(id)
    form = ProductTypeForm()
    if request.method=='POST':
        type.type_name=form.type_name.data
        db.session.commit()
        return redirect(url_for('admin_product_type'))
    return render_template('admin/product_type_update.html',form=form,type=type)

# Product Brand Routes
@app.route('/admin/product/brand', methods=['GET', 'POST'])
def admin_product_brand():
    form=ProductBrandForm()
    brands = ProductBrand.query.all()
    if request.method=='POST':
        brand=ProductBrand(
            brand_name = form.brand_name.data
        )
        db.session.add(brand)
        db.session.commit()
        return redirect(url_for('admin_product_brand'))
    return render_template('admin/product_brand.html',form=form,brands=brands)

@app.route('/admin/product/brand/delete/<int:id>')
def delete_admin_product_brand(id):
    brand = ProductBrand.query.get(id)
    db.session.delete(brand)
    db.session.commit()
    return redirect(url_for('admin_product_brand'))

@app.route('/admin/product/brand/update/<int:id>', methods=['GET', 'POST'])
def update_admin_product_brand(id):
    brand = ProductBrand.query.get(id)
    form = ProductBrandForm()
    if request.method=='POST':
        brand.brand_name=form.brand_name.data
        db.session.commit()
        return redirect(url_for('admin_product_brand'))
    return render_template('admin/product_brand_update.html',form=form,brand=brand)

@app.route('/admin/product/image',methods = ['GET','POST'])
def admin_product_image():
    form = ProductImageForm()
    products = Product.query.all()
    images = ProductImage.query.all()
    if request.method=='POST':
        file = form.img_url.data
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        img = ProductImage(
            img_url = filename,
            product_id = request.form['product_id']
        )
        db.session.add(img)
        db.session.commit()
        return redirect(url_for('admin_product_image'))

    return render_template('admin/product_image.html',form=form,products=products,images=images,
    Product=Product)

@app.route('/admin/product/image/delete/<int:id>',methods = ['GET','POST'])
def delet_admin_product_image(id):
    image = ProductImage.query.get(id)
    db.session.delete(image)
    db.session.commit()
    return redirect(url_for('admin_product_image'))

@app.route('/admin/product/image/update/<int:id>',methods = ['GET','POST'])
def update_admin_product_image(id):
    image = ProductImage.query.get(id)
    form = ProductImageForm()
    products = Product.query.all()
    if request.method=='POST':
        file = form.img_url.data
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image.img_url=filename
        image.product_id = request.form['product_id']
        db.session.commit()
        return redirect(url_for('admin_product_image'))
    return render_template('admin/product_image_update.html',form=form,image=image,products=products)




