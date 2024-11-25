from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateTimeField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Length, Email


class BusinessProfileForm(FlaskForm):
    """Form for Business Profile"""
    name = StringField('Business name', validators=[DataRequired(), Length(min=5)])
    email = StringField('Business email', validators=[DataRequired(), Email()])
    owner_id = HiddenField("Owner's Id")
    location = StringField('Business location', validators=[DataRequired()])
    description = TextAreaField('About the business', validators=[DataRequired(), Length(min=100)])
    online_available = BooleanField('Online Business')
    offline_available = BooleanField('Offline Available.')
    submit = SubmitField('Add business')

