from . import db
from models.baseModel import BaseModel


class Business(BaseModel):
    """A business model class that inherites from BaseModel"""
    id = db.Column(
        db.Integer,
        primary_key = True
        )
    name = db.Column(
        db.String(255),
        nullable = False,
        unique = True
        )
    email = db.Column(
        db.String(255),
        nullable = False,
        unique = True
        )
    description = db.Column(
        db.Text(255),
        nullable = False
    )
    location = db.Column(
        db.String(255),
        nullable = False
    )
    owner_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable = False
    )
    online_available = db.Column(
        db.Boolean,
        default=True
        )
    offline_available = db.Column(
        db.Boolean,
        default=True
        )