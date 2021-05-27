from app import app
from flask import render_template, request, redirect, url_for,make_response
from app import db
from datetime import datetime
from app.models import ShopContact, Features, Logos, PaymentCards, SocialMedias,Sales,Employees,User,Product,ProductImage,Blog,BlogSocial,Comment,ProductCategory,FAQ
def commonVariables():
    global shopContacts,cards,socialMedias,loginStat,users,loginId
    shopContacts = ShopContact.query.all()
    cards = PaymentCards.query.all()
    socialMedias = SocialMedias.query.all()
    loginStat = request.cookies.get('loginStatus')
    users = User.query.all()
    loginId='salam' 
    for user in users:
        if str(user.id)==loginStat:
            loginId = str(user.id)
    print(loginId)
        
 
    

# index route

@app.route('/')
def main_index():
    features = Features.query.all()
    logos = Logos.query.all()
    blogs = Blog.query.all()
    faqs = FAQ.query.all()
    commonVariables()
    return render_template('main/index.html', shopContacts=shopContacts, features=features, logos=logos,
     cards=cards, socialMedias=socialMedias,loginStat=loginStat,loginId=loginId,blogs=blogs,faqs=faqs,FAQ=FAQ)


# collection route
@app.route('/collections')
def main_collections():
    commonVariables()
    return render_template('main/collection.html', shopContacts=shopContacts, cards=cards, socialMedias=socialMedias,loginStat=loginStat,loginId=loginId)

# shop route


@app.route('/collections/all')
def main_shop():
    commonVariables()
    products = Product.query.all()
    images = ProductImage.query.all()
    return render_template('main/shop.html',shopContacts=shopContacts, cards=cards,
     socialMedias=socialMedias,loginStat=loginStat,loginId=loginId,products=products,
     images=images,ProductImage=ProductImage)

# cookies cakes route


@app.route('/collection/best')
def main_cookies():
    commonVariables()
    products = Product.query.all()
    images = ProductImage.query.all()
    bestProducts = Product.query.filter_by(p_category_id=ProductCategory.query.filter_by(cat_name='Best').first().id)

    return render_template('main/cookies.html', shopContacts=shopContacts, cards=cards,
     socialMedias=socialMedias,loginStat=loginStat,loginId=loginId,products=products,
     images=images,ProductImage=ProductImage,bestProducts=bestProducts)

# wedding cakes route


@app.route('/collections/wedding')
def main_wedding():
    commonVariables()
    weddingProducts = Product.query.filter_by(p_category_id=ProductCategory.query.filter_by(cat_name='Wedding').first().id)
    return render_template('main/wedding.html', shopContacts=shopContacts, cards=cards, socialMedias=socialMedias,
    loginStat=loginStat,loginId=loginId,weddingProducts=weddingProducts,ProductImage=ProductImage)

# cup cakes route


@app.route('/collections/chocalate')
def main_cupcakes():
    commonVariables()
    cupProducts = Product.query.filter_by(p_category_id=ProductCategory.query.filter_by(cat_name='Cup').first().id)
    return render_template('main/cupcakes.html', shopContacts=shopContacts, cards=cards, socialMedias=socialMedias,
    loginStat=loginStat,loginId=loginId,ProductImage=ProductImage,cupProducts=cupProducts)

# # pages route


@app.route('/pages/aboutus')
def main_aboutus():
    commonVariables()
    sales = Sales.query.all()
    employees = Employees.query.all()
    return render_template('main/pages.html', shopContacts=shopContacts, cards=cards, socialMedias=socialMedias,sales=sales,employees=employees,loginStat=loginStat,loginId=loginId)

# account page

@app.route('/account/<id>')
def main_account(id):
    commonVariables()
    user = User.query.get(id)
    if loginStat == str(user.id):     
        return render_template('main/account.html',user=user, shopContacts=shopContacts, cards=cards, socialMedias=socialMedias,loginStat=loginStat,loginId=loginId)
    else:
        return redirect('/account/login')


# login page route 
    
@app.route('/account/login',methods=['GET','POST'])
def main_login():
    shopContacts = ShopContact.query.all()
    cards = PaymentCards.query.all()
    socialMedias = SocialMedias.query.all()
    loginStat = request.cookies.get('loginStatus')
    users = User.query.all()
    loginId='salam'
    for user in users:
        if str(user.id)==loginStat:
            loginId = str(user.id)
    if request.method =='POST':
        for user in users:
            if user.email==request.form['email']:
                if user.password == request.form['password']:
                    loginId = str(user.id)
                    loginStat = loginId
                    resp = make_response(render_template('main/account.html',user=user, shopContacts=shopContacts,socialMedias=socialMedias, cards=cards,loginStat=loginStat,loginId=loginId))
                    resp.set_cookie('loginStatus', str(user.id))
                    return resp
                else:
                    return redirect('/account/login')
            
        if request.form['email']=='admin@gmail.com':
            if request.form['password']=='admin':
                return render_template('admin/index.html')

    return render_template('main/log-in.html', shopContacts=shopContacts, cards=cards, socialMedias=socialMedias,loginStat=loginStat,loginId=loginId)


# register page
@app.route('/account/register',methods = ['GET','POST'])
def main_register():
    commonVariables()

    if request.method =='POST':
        user = User(
            firstName = request.form['firstName'],
            lastName = request.form['lastName'],
            email = request.form['email'],
            password = request.form['password']
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main_login'))
    return render_template('main/register.html', shopContacts=shopContacts, cards=cards, socialMedias=socialMedias,loginStat=loginStat,loginId=loginId)

# logout 
@app.route('/logout',methods=['GET','POST'])
def logout():
    features = Features.query.all()
    logos = Logos.query.all()
    shopContacts = ShopContact.query.all()
    cards = PaymentCards.query.all()
    socialMedias = SocialMedias.query.all()
    loginStat = request.cookies.get('loginStatus')
    users = User.query.all()
    loginId=''
    for user in users:
        if user.id==loginStat:
            loginId = str(loginStat)
    resp = make_response(render_template('main/index.html', shopContacts=shopContacts, features=features, logos=logos, cards=cards, socialMedias=socialMedias,loginStat=loginStat,loginId=loginId ))
    resp.set_cookie('loginStatus', 'logout')
    return resp



# Blog Page Routes

@app.route('/blog/<int:id>',methods = ['GET','POST'])
def main_blog(id):
    commonVariables()
    blog = Blog.query.get(id)
    smedias = BlogSocial.query.all()
    # comments = Comment.query.all()
    if request.method=='POST':
        comment = Comment(
            c_name = request.form['c_name'],
            c_email = request.form['c_email'],
            c_msg = request.form['c_msg'],
            c_date = datetime.now(),
            blog_id = id
        )
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main_blog', id=id))
    return render_template('main/blog.html', shopContacts=shopContacts, cards=cards, socialMedias=socialMedias,
    loginStat=loginStat,loginId=loginId,blog=blog,smedias=smedias,BlogSocial = BlogSocial,Comment = Comment)
