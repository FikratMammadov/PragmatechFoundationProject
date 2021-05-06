from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class CategoryForm(FlaskForm):
    cat_name=StringField('cat_name')
    submit=SubmitField()
