from flask_mail import Message
from flask import url_for
from app.app import mail
from typing import TYPE_CHECKING
from models.users import User


def send_password_reset_email(user: User):
    """
    Sends a password reset email to the user.
    """
    token = user.password_reset_token()
    msg = Message('Password Reset Request', recipients = [user.email])
    msg.body = (f'''To reset your password, visit the following link:
{url_for('auth.reset_password', token=token, _external=True)}
If you did not make this request, simply ignore this email.
''')
    
    mail.send(msg)

def send_verification_email(user: User):
    token = user.email_verification_token()
    msg = Message('Verify Your Email', recipients=[user.email])
    msg.body = f'''Please verify your email by clicking on the following link:
{url_for('auth.verify_email', token=token, _external=True)}
'''
    mail.send(msg)