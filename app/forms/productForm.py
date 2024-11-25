from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length

class ProductForm(FlaskForm):
    """Form for product operations."""
    name = StringField('Product Name', validators=[DataRequired(), Length(max=100)])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0)])
    stock = IntegerField('Stock', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Add Product')