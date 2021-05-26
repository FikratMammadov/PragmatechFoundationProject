from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FileField,IntegerField,FloatField,TextAreaField,SelectField

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