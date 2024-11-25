from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


login_Manager = LoginManager()
db = SQLAlchemy()

__all__ = [
    'db',
    'login_Manager',
    ]