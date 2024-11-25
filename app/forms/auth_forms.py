from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from wtforms.fields import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from models.user import User


class RegistrationForm(FlaskForm):
    """Registration form for users"""
    full_name = StringField('Full Name', validators=[DataRequired(), Length(min=5)])
    username = StringField('Username', validators=[DataRequired(), Length(min=5)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=10)])
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=8, max=16)])
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo(
            'password',
            'Confirm password should be equal to the password.')])
    accept_privacy_policy = BooleanField('I accept the Privacy Policy', validators=[DataRequired()])
    accept_terms_of_service = BooleanField('I accept the Terms of Service', validators=[DataRequired()])
    is_admin = BooleanField('Is_Admin')
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """ checks the availability of the username """
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose another')
        
    def validate_email(self, email):
        """ checks the availability of the username """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose another')


class LoginForm(FlaskForm):
    """Login form for users."""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=16)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')