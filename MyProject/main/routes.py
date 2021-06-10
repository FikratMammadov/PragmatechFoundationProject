from app import app
from flask import render_template, request, redirect, url_for, make_response
from sqlalchemy import desc
from app import db
from datetime import datetime
from app.models import ShopContact, Features, Logos, PaymentCards, SocialMedias, Sales, Employees, User, Product, ProductImage, Blog, BlogSocial, Comment, ProductCategory, FAQ,ProductType,ProductAvailability,Shipping,Country,Menu,ProductBrand
from app import bc

def commonVariables():
    global shopContacts, cards, socialMedias, loginStat, users, loginId
    shopContacts = ShopContact.query.all()
    cards = PaymentCards.query.all()
    socialMedias = SocialMedias.query.all()
    loginStat = request.cookies.get('loginStatus')
    users = User.query.all()
    loginId = 'salam'
    for user in users:
        if str(user.id) == loginStat:
            loginId = str(user.id)
    print(loginId)

# Sorting common func
def sortBy(_sortingName,_products):
    commonVariables()
    products = _products
    images = ProductImage.query.all()
    categories = ProductCategory.query.all()
    brands = ProductBrand.query.all()
    sortingName = _sortingName
    return render_template('main/shop.html', shopContacts=shopContacts, cards=cards,
                           socialMedias=socialMedias, loginStat=loginStat, loginId=loginId, products=products,
                           images=images, ProductImage=ProductImage,categories=categories,brands=brands,
                           sortingName=sortingName)

# index route

@app.route('/')
def main_index():
    features = Features.query.all()
    logos = Logos.query.all()
    blogs = Blog.query.all()
    faqs = FAQ.query.all()
    menus = Menu.query.all()
    commonVariables()
    return render_template('main/index.html', shopContacts=shopContacts, features=features, logos=logos,
                           cards=cards, socialMedias=socialMedias, loginStat=loginStat, loginId=loginId, 
                           blogs=blogs, faqs=faqs, FAQ=FAQ,menus=menus,Comment=Comment)


# collection route
@app.route('/collections')
def main_collections():
    commonVariables()
    return render_template('main/collection.html', shopContacts=shopContacts, cards=cards, socialMedias=socialMedias, loginStat=loginStat, loginId=loginId)

# shop route


@app.route('/products')
def main_shop():
    commonVariables()
    products = Product.query.all()
    images = ProductImage.query.all()
    categories = ProductCategory.query.all()
    brands = ProductBrand.query.all()
    sortingName = "Featured"
    return render_template('main/shop.html', shopContacts=shopContacts, cards=cards,
                           socialMedias=socialMedias, loginStat=loginStat, loginId=loginId, products=products,
                           images=images, ProductImage=ProductImage,categories=categories,brands=brands,sortingName=sortingName)

# shop filter by category
@app.route('/products/category/<int:id>')
def main_shop_category(id):
    commonVariables()
    category = ProductCategory.query.get(id)
    products = Product.query.filter_by(p_category_id=category.id)
    categories = ProductCategory.query.all()
    brands = ProductBrand.query.all()
    return render_template('main/shop.html',shopContacts=shopContacts, cards=cards,
                           socialMedias=socialMedias, loginStat=loginStat, loginId=loginId,products=products,
                           ProductImage=ProductImage,categories=categories,brands=brands)

# shop filter by brand
@app.route('/products/brand/<int:id>')
def main_shop_brand(id):
    commonVariables()
    categories = ProductCategory.query.all()
    brands = ProductBrand.query.all()
    brand = ProductBrand.query.get(id)
    products = Product.query.filter_by(p_brand_id=brand.id)
    return render_template('main/shop.html',shopContacts=shopContacts, cards=cards,
                           socialMedias=socialMedias, loginStat=loginStat, loginId=loginId,products=products,
                           ProductImage=ProductImage,categories=categories,brands=brands)

# shop filter by price
@app.route('/products/price/0-100')
def main_shop_price_1():
    commonVariables()
    categories = ProductCategory.query.all()
    brands = ProductBrand.query.all()
    products = Product.query.filter((Product.p_price>0)& (Product.p_price<100))
    return render_template('main/shop.html',shopContacts=shopContacts, cards=cards,
                           socialMedias=socialMedias, loginStat=loginStat, loginId=loginId,products=products,
                           ProductImage=ProductImage,categories=categories,brands=brands)

@app.route('/products/price/100-200')
def main_shop_price_2():
    commonVariables()
    categories = ProductCategory.query.all()
    brands = ProductBrand.query.all()
    products = Product.query.filter((Product.p_price>100)& (Product.p_price<200))
    return render_template('main/shop.html',shopContacts=shopContacts, cards=cards,
                           socialMedias=socialMedias, loginStat=loginStat, loginId=loginId,products=products,
                           ProductImage=ProductImage,categories=categories,brands=brands)


@app.route('/products/price/200-300')
def main_shop_price_3():
    commonVariables()
    categories = ProductCategory.query.all()
    brands = ProductBrand.query.all()
    products = Product.query.filter((Product.p_price>200)& (Product.p_price<300))
    return render_template('main/shop.html',shopContacts=shopContacts, cards=cards,
                           socialMedias=socialMedias, loginStat=loginStat, loginId=loginId,products=products,
                           ProductImage=ProductImage,categories=categories,brands=brands)

# sort by price
@app.route('/products/min')
def main_shop_min():
    return sortBy("Price, low to high",Product.query.order_by(Product.p_price))

@app.route('/products/max')
def main_shop_max():
    return sortBy("Price, high to low",Product.query.order_by(desc(Product.p_price)))

@app.route('/products/alp/asc')
def main_shop_alp_asc():
    return sortBy("A-Z",Product.query.order_by(Product.p_name))

@app.route('/products/alp/desc')
def main_shop_alp_desc():
    return sortBy("Z-A",Product.query.order_by(desc(Product.p_name)))

@app.route('/products/date/asc')
def main_shop_date_asc():
    return sortBy("Date, old to new",Product.query.all())

@app.route('/products/date/decs')
def main_shop_date_desc():
    return sortBy("Date, new to old",Product.query.order_by(desc(Product.id)))

# cookies cakes route
@app.route('/collection/best')
def main_cookies():
    commonVariables()
    products = Product.query.all()
    images = ProductImage.query.all()
    bestProducts = Product.query.filter_by(
        p_category_id=ProductCategory.query.filter_by(cat_name='Best').first().id)

    return render_template('main/cookies.html', shopContacts=shopContacts, cards=cards,
                           socialMedias=socialMedias, loginStat=loginStat, loginId=loginId, products=products,
                           images=images, ProductImage=ProductImage, bestProducts=bestProducts)

# wedding cakes route


@app.route('/collections/wedding')
def main_wedding():
    commonVariables()
    weddingProducts = Product.query.filter_by(
        p_category_id=ProductCategory.query.filter_by(cat_name='Wedding').first().id)
    return render_template('main/wedding.html', shopContacts=shopContacts, cards=cards, socialMedias=socialMedias,
                           loginStat=loginStat, loginId=loginId, weddingProducts=weddingProducts, ProductImage=ProductImage)

# cup cakes route


@app.route('/collections/chocalate')
def main_cupcakes():
    commonVariables()
    cupProducts = Product.query.filter_by(
        p_category_id=ProductCategory.query.filter_by(cat_name='Cup').first().id)
    return render_template('main/cupcakes.html', shopContacts=shopContacts, cards=cards, socialMedias=socialMedias,
                           loginStat=loginStat, loginId=loginId, ProductImage=ProductImage, cupProducts=cupProducts)

# # pages route


@app.route('/pages/aboutus')
def main_aboutus():
    commonVariables()
    sales = Sales.query.all()
    employees = Employees.query.all()
    return render_template('main/pages.html', shopContacts=shopContacts, cards=cards, socialMedias=socialMedias, sales=sales, employees=employees, loginStat=loginStat, loginId=loginId)

# account page


@app.route('/account/<id>')
def main_account(id):
    commonVariables()
    user = User.query.get(id)
    if loginStat == str(user.id):
        return render_template('main/account.html', user=user, shopContacts=shopContacts, cards=cards, socialMedias=socialMedias, loginStat=loginStat, loginId=loginId)
    else:
        return redirect('/account/login')


# login page route

@app.route('/account/login', methods=['GET', 'POST'])
def main_login():
    shopContacts = ShopContact.query.all()
    cards = PaymentCards.query.all()
    socialMedias = SocialMedias.query.all()
    loginStat = request.cookies.get('loginStatus')
    users = User.query.all()
    loginId = 'salam'
    for user in users:
        if str(user.id) == loginStat:
            loginId = str(user.id)
    if request.method == 'POST':
        for user in users:
            if user.email == request.form['email']:
                if bc.check_password_hash( user.password,request.form['password']):
                    loginId = str(user.id)
                    loginStat = loginId
                    resp = make_response(render_template('main/account.html', user=user, shopContacts=shopContacts,
                                         socialMedias=socialMedias, cards=cards, loginStat=loginStat, loginId=loginId))
                    resp.set_cookie('loginStatus', str(user.id))
                    return resp
                else:
                    return redirect('/account/login')

    return render_template('main/log-in.html', shopContacts=shopContacts, cards=cards, socialMedias=socialMedias, loginStat=loginStat, loginId=loginId)


# register page
@app.route('/account/register', methods=['GET', 'POST'])
def main_register():
    commonVariables()

    if request.method == 'POST':
        user = User(
            firstName=request.form['firstName'],
            lastName=request.form['lastName'],
            email=request.form['email'],
            password=bc.generate_password_hash(request.form['password'])
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main_login'))
    return render_template('main/register.html', shopContacts=shopContacts, cards=cards, socialMedias=socialMedias, loginStat=loginStat, loginId=loginId)

# logout


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    features = Features.query.all()
    logos = Logos.query.all()
    shopContacts = ShopContact.query.all()
    cards = PaymentCards.query.all()
    socialMedias = SocialMedias.query.all()
    loginStat = request.cookies.get('loginStatus')
    users = User.query.all()
    loginId = ''
    for user in users:
        if user.id == loginStat:
            loginId = str(loginStat)
    resp = make_response(render_template('main/index.html', shopContacts=shopContacts, features=features,
                         logos=logos, cards=cards, socialMedias=socialMedias, loginStat=loginStat, loginId=loginId))
    resp.set_cookie('loginStatus', 'logout')
    return resp


# Blog Page Routes

@app.route('/blog/<int:id>', methods=['GET', 'POST'])
def main_blog(id):
    commonVariables()
    blog = Blog.query.get(id)
    smedias = BlogSocial.query.all()
    # comments = Comment.query.all()
    if request.method == 'POST':
        comment = Comment(
            c_name=request.form['c_name'],
            c_email=request.form['c_email'],
            c_msg=request.form['c_msg'],
            c_date=datetime.now(),
            blog_id=id
        )
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main_blog', id=id))
    return render_template('main/blog.html', shopContacts=shopContacts, cards=cards, socialMedias=socialMedias,
                           loginStat=loginStat, loginId=loginId, blog=blog, smedias=smedias, BlogSocial=BlogSocial, Comment=Comment)

# Product Self Routes 
@app.route('/products/<int:id>')
def main_product(id):
    product = Product.query.get(id)
    images = ProductImage.query.filter_by(product_id=product.id)
    commonVariables()
    return render_template('main/product_self.html', shopContacts=shopContacts, cards=cards,
                           socialMedias=socialMedias, loginStat=loginStat, loginId=loginId,product=product,
                           ProductType=ProductType,ProductAvailability=ProductAvailability,images=images)

@app.route('/information/<int:id>',methods = ['GET','POST'])
def main_info(id):
    countries = Country.query.all()
    product = Product.query.get(id)
    if request.method=='POST':
        shippingInfo = Shipping(
            f_name = request.form['f_name'],
            l_name = request.form['l_name'],
            email = request.form['email'],
            address = request.form['address'],
            apartment = request.form['apartment'],
            city = request.form['city'],
            postal_code = request.form['postal_code'],
            product_id = id,
            country_id = request.form['country_id']
        )
        db.session.add(shippingInfo)
        db.session.commit()
        return redirect(url_for('main_shop'))
    return render_template('main/information.html',product=product,countries=countries,id=id)



