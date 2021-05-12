from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FileField

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