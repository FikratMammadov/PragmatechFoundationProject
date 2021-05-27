from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FileField,IntegerField,FloatField,TextAreaField,DateField

class LogosForm(FlaskForm):
    l_image = FileField('l_name')
    submit=SubmitField()

class LogoUpdateForm(FlaskForm):
    l_image = FileField('l_name')
    submit=SubmitField()

class PaymentCardsForm(FlaskForm):
    card_image=FileField('card_image')
    submit = SubmitField()

class SocialMediasForm(FlaskForm):
    social_icon=StringField('social_icon')
    social_url=StringField('social_url')
    submit=SubmitField()

class SalesForm(FlaskForm):
    sales_name = StringField('sales_name')
    sales_icon=StringField('sales_icon')
    sales_number=IntegerField('sales_number')
    submit=SubmitField()

class EmployeesForm(FlaskForm):
    e_fullname = StringField('e_fullname')
    e_image = FileField('e_image')
    e_profession = StringField('e_profession')
    submit = SubmitField()

class ProductForm(FlaskForm):
    p_name=StringField('p_name')
    p_price=FloatField('p_price')
    p_quantity = IntegerField('p_quantity')
    p_content = TextAreaField('p_content')
    p_img = FileField('p_img')
    submit = SubmitField()

class ProductSizeForm(FlaskForm):
    s_name = StringField('s_name')
    submit = SubmitField()

class ProductAvailabilityForm(FlaskForm):
    pa_name = StringField('pa_name')
    submit = SubmitField()

class ProductCategoryForm(FlaskForm):
    cat_name = StringField('cat_name')
    submit = SubmitField()

class ProductTypeForm(FlaskForm):
    type_name=StringField('type_name')
    submit = SubmitField()

class ProductBrandForm(FlaskForm):
    brand_name=StringField('brand_name')
    submit = SubmitField()

class ProductImageForm(FlaskForm):
    img_url = FileField('img_url')
    submit=SubmitField()

class PostForm(FlaskForm):
    post_image = FileField('post_image')
    post_title = StringField('post_title')
    post_content = TextAreaField('post_content')
    submit = SubmitField()

class PostImageForm(FlaskForm):
    post_img_url = FileField('post_img_url')
    submit = SubmitField()

class PostTransportForm(FlaskForm):
    tp_name = StringField('tp_name')
    tp_icon = StringField('tp_icon')
    submit = SubmitField()

class BlogForm(FlaskForm):
    b_title = StringField('b_title')
    b_content = TextAreaField('b_content')
    b_img = FileField('b_img')
    submit = SubmitField()

class BlogSocialForm(FlaskForm):
    social_icon = StringField('social_icon')
    social_link = StringField('social_link')
    submit = SubmitField()

class FAQForm(FlaskForm):
    question = TextAreaField('question')
    answer = TextAreaField('answer')
    submit = SubmitField()

class FAQImageForm(FlaskForm):
    faq_img = FileField('faq_img')
    submit = SubmitField()

class MenuForm(FlaskForm):
    m_title = StringField('m_title')
    m_price = FloatField('m_price')
    m_content = TextAreaField('m_content')
    m_img = FileField('m_img')
    submit = SubmitField()