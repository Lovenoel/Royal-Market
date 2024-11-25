from . import db, login_Manager
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """A User class model."""

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False, unique=True)
    accepted_privacy_policy = db.Column(db.Boolean, default=False, nullable=False)
    accepted_terms_of_service = db.Column(db.Boolean, default=False, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        """A string representation of the user object"""
        return f"<User {self.username}, {self.email}>"


@login_Manager.user_loader
def load_user(user_id):
    """Helper function for loading users"""
    return User.query.get(int(user_id))