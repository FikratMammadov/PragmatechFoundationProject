from app import app
from flask import render_template, request, redirect, url_for,make_response
from app import db
from app.models import ShopContact, Features, Logos, PaymentCards, SocialMedias,Sales,Employees,User

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
    commonVariables()
    return render_template('main/index.html', shopContacts=shopContacts, features=features, logos=logos, cards=cards, socialMedias=socialMedias,loginStat=loginStat,loginId=loginId)


# collection route
@app.route('/collections')
def main_collections():
    commonVariables()
    return render_template('main/collection.html', shopContacts=shopContacts, cards=cards, socialMedias=socialMedias,loginStat=loginStat,loginId=loginId)

# shop route


@app.route('/collections/all')
def main_shop():
    commonVariables()
    return render_template('main/shop.html',shopContacts=shopContacts, cards=cards, socialMedias=socialMedias,loginStat=loginStat,loginId=loginId)

# cookies cakes route


@app.route('/collection/best')
def main_cookies():
    commonVariables()
    return render_template('main/cookies.html', shopContacts=shopContacts, cards=cards, socialMedias=socialMedias,loginStat=loginStat,loginId=loginId)

# wedding cakes route


@app.route('/collections/wedding')
def main_wedding():
    commonVariables()
    return render_template('main/wedding.html', shopContacts=shopContacts, cards=cards, socialMedias=socialMedias,loginStat=loginStat,loginId=loginId)

# cup cakes route


@app.route('/collections/chocalate')
def main_cupcakes():
    commonVariables()
    return render_template('main/cupcakes.html', shopContacts=shopContacts, cards=cards, socialMedias=socialMedias,loginStat=loginStat,loginId=loginId)

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
    commonVariables()
    users=User.query.all()
    if request.method =='POST':
        for user in users:
            if user.email==request.form['email']:
                if user.password == request.form['password']:
                    resp = make_response(render_template('main/account.html',user=user, shopContacts=shopContacts, cards=cards,loginStat=loginStat,loginId=loginId))
                    resp.set_cookie('loginStatus', str(user.id))
                    return resp
                else:
                    return redirect('/account/login')
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

# , shopContacts=shopContacts, features=features, logos=logos, cards=cards, socialMedias=socialMedias,loginStat=loginStat,loginId=loginId