import uuid
from . import db, bcrypt
from models.baseModel import BaseModel
from flask_login import LoginManager
from itsdangerous import URLSafeTimedSerializer
from flask import current_app

login_manager = LoginManager()



class User(BaseModel):
    """User class for managing user accounts"""
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    _password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email_verified = db.Column(db.Boolean, default=False)

    def __init__(self, username, email, password, first_name=None, last_name=None):
        """Initialize a User instance"""
        self.username = username
        self.email = email
        self.password = password  # This will call the setter for password hashing
        self.first_name = first_name
        self.last_name = last_name

    @property
    def password(self):
        """Getter for password"""
        return self._password

    @password.setter
    def password(self, pwd: str):
        """Setter for password (hashes the password)"""
        if pwd is None or type(pwd) is not str:
            self._password = None
        else:
            self._password = bcrypt.generate_password_hash(pwd).decode('utf-8')

    def is_valid_password(self, pwd: str) -> bool:
        """Validate a password by comparing the hash"""
        if pwd is None and type(pwd) is not str:
            return False
        elif self.password is None:
            return False
        return bcrypt.check_password_hash(self.password, pwd)
    
    def display_name(self) -> str:
        """ Display User name based on email/first_name/last_name/username """
        if self.username:
            return self.username  # Return username if available
        elif self.first_name and self.last_name:
            return "{} {}".format(self.first_name, self.last_name)  # First name and last name if no username
        elif self.first_name:
            return self.first_name  # If only first name available
        elif self.last_name:
            return self.last_name  # If only last name available
        elif self.email:
            return self.email  # Fallback to email if no other fields are available
        return ""

    @classmethod
    def username_exists(cls, username: str):
        """Check if a username already exists in the database"""
        return cls.query.filter_by(username=username).first() is not None

    @classmethod
    def email_exists(cls, email: str):
        """Check if an email already exists in the database"""
        return cls.query.filter_by(email=email).first() is not None

    def save(self):
        """Save current object to the database with validation"""
        if User.username_exists(self.username):
            raise ValueError("Username already taken.")
        if User.email_exists(self.email):
            raise ValueError("Email already in use.")
        db.session.add(self)
        db.session.commit()


    # ------------ Password Reset Methods----------- #
    def password_reset_token(self, expires_sec = 1800):
        """
        Genearte a secure password reset token
        """
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return serializer.dumps(
            {'user_id': self.id},
            salt='reset-password'
            )
    
    @staticmethod
    def verify_password_reset_token(token, expires_sec = 1800):
        """
        Verify password reset token and return user
        """
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            user_id = serializer.loads(
                token,
                salt='reset-password',
                max_age = expires_sec
            ) ['user_id']
        except Exception:
            return None
        return User.get_by_id(user_id)
    

    # -------------Email Verification Methods ---------------#
    def email_verification_token(self, expires_sec = 1800):
        """
        Generate email verification token.
        """
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return serializer.dumps(
            {'user_id': self.id},
            salt = 'verify-email'
            )
    
    def verify_email_token(token, expires_sec = 1800):
        """
        Verify email verification token and return user.
        """
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            user_id = serializer.loads(
                token,
                salt = 'verify-email',
                max_age = expires_sec
            ) ['user_id']
        except Exception:
            return None
        return User.get_by_id(user_id)

# Function to load user by ID (required for Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)