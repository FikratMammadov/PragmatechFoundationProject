from app import db

class ShopContact(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    contact_icon = db.Column(db.String(100))
    contact_detail = db.Column(db.String(100))
    contact_link = db.Column(db.String(150))

class Features(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    features_image = db.Column(db.String(100))
    features_title = db.Column(db.String(100))
    features_content = db.Column(db.String(100))

class Logos(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    l_image=db.Column(db.String(100))

class PaymentCards(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    card_image=db.Column(db.String(100))

class SocialMedias(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    social_icon=db.Column(db.String(100))
    social_url=db.Column(db.String(100))

class Sales(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    sales_name = db.Column(db.String(50))
    sales_icon = db.Column(db.String(50))
    sales_number = db.Column(db.String(50))

class Employees(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    e_image = db.Column(db.String(100))
    e_fullname = db.Column(db.String(100))
    e_profession = db.Column(db.String(100))

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    firstName = db.Column(db.String(50),nullable=False)
    lastName = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(100), unique=True,nullable=False)
    password = db.Column(db.String(50),nullable=False)

class ProductSize(db.Model):
    __tablename__='ProductSize'
    id = db.Column(db.Integer,primary_key=True)
    s_name = db.Column(db.String(50),nullable=False)
    sizes = db.relationship('Product', backref = 'ProductSize',lazy = True)

class ProductAvailability(db.Model):
    __tablename__='ProductAvailability'
    id = db.Column(db.Integer,primary_key=True)
    pa_name = db.Column(db.String(50),nullable=False)
    availabilities=db.relationship('Product',backref='ProductAvailability',lazy=True)

class ProductCategory(db.Model):
    __tablename__='ProductCategory'
    id = db.Column(db.Integer,primary_key=True)
    cat_name = db.Column(db.String(50),nullable=False)
    categories = db.relationship('Product',backref = 'ProductCategory',lazy=True)

class ProductType(db.Model):
    __tablename__='ProductType'
    id = db.Column(db.Integer,primary_key=True)
    type_name = db.Column(db.String(50),nullable=False)
    types = db.relationship('Product',backref='ProductType',lazy=True)

class ProductBrand(db.Model):
    __tablename__='ProductBrand'
    id = db.Column(db.Integer,primary_key=True)
    brand_name = db.Column(db.String(50),nullable=False)

class Product(db.Model):
    __tablename__='Product'
    id = db.Column(db.Integer,primary_key=True)
    p_name = db.Column(db.String(50),nullable=False)
    p_price = db.Column(db.Float,nullable=False)
    p_quantity = db.Column(db.Integer,nullable=False)
    p_content = db.Column(db.Text)
    p_img = db.Column(db.String(100))
    p_size_id = db.Column(db.Integer,db.ForeignKey('ProductSize.id'),nullable = False)
    p_availability_id = db.Column(db.Integer,db.ForeignKey('ProductAvailability.id'))
    p_category_id = db.Column(db.Integer,db.ForeignKey('ProductCategory.id'),nullable = False)
    p_type_id = db.Column(db.Integer,db.ForeignKey('ProductType.id'),nullable = False)
    p_brand_id = db.Column(db.Integer,db.ForeignKey('ProductBrand.id'),nullable = False)
    images = db.relationship('ProductImage',backref='Product',lazy=True)

class ProductImage(db.Model):
    __tablename__='ProductImage'
    id = db.Column(db.Integer,primary_key=True)
    img_url = db.Column(db.String(50),nullable=False)
    product_id = db.Column(db.Integer,db.ForeignKey('Product.id'),nullable = False)

class Post(db.Model):
    __tablename__='Post'
    id = db.Column(db.Integer,primary_key=True)
    post_image = db.Column(db.String(100),nullable=False)
    post_title = db.Column(db.String(50),nullable=False)
    post_content = db.Column(db.Text)
    postImages = db.relationship('PostImage',backref = 'Post',lazy=True)
    postTransports = db.relationship('PostTransport',backref = 'Post',lazy=True)

class PostImage(db.Model):
    __tablename__='PostImage'
    id = db.Column(db.Integer,primary_key=True)
    post_img_url = db.Column(db.String(100),nullable=False)
    post_id = db.Column(db.Integer,db.ForeignKey('Post.id'),nullable = False)

class PostTransport(db.Model):
    __tablename__='PostTransport'
    id = db.Column(db.Integer,primary_key=True)
    tp_name = db.Column(db.String(50),nullable=False)
    tp_icon = db.Column(db.String(50),nullable=False)
    post_id=db.Column(db.Integer,db.ForeignKey('Post.id'),nullable = False)

class Blog(db.Model):
    __tablename__='Blog'
    id = db.Column(db.Integer,primary_key=True)
    b_date = db.Column(db.DateTime,nullable=False)
    b_title = db.Column(db.String(50),nullable=False)
    b_content = db.Column(db.Text)
    b_img = db.Column(db.String(50))
    smedias = db.relationship('BlogSocial',backref = 'Blog',lazy=True)
    comments = db.relationship('Comment',backref = 'Blog',lazy=True)
     

class BlogSocial(db.Model):
    __tablename__='BlogSocial'
    id = db.Column(db.Integer,primary_key=True)
    social_icon = db.Column(db.String(50),nullable=False)
    social_link = db.Column(db.String(50),nullable=False)
    blog_id = db.Column(db.Integer,db.ForeignKey('Blog.id'),nullable = False)

class Comment(db.Model):
    __tablename__='Comment'
    id = db.Column(db.Integer,primary_key=True)
    c_name = db.Column(db.String(50),nullable=False)
    c_email = db.Column(db.String(50),nullable=False)
    c_msg = db.Column(db.Text)
    c_date = db.Column(db.DateTime)
    blog_id = db.Column(db.Integer,db.ForeignKey('Blog.id'),nullable = False)





 
        

