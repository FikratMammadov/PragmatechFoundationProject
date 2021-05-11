from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FileField

class LogosForm(FlaskForm):
    l_image = FileField('l_name')
    submit=SubmitField()

class LogoUpdateForm(FlaskForm):
    l_image = FileField('l_name')
    submit=SubmitField()