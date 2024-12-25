from . import db
from models.baseModel import BaseModel


class Product(BaseModel):
    """ A product model class that inherites from BaseModel"""
    __tablename__ = 'products'
    name = db.Column(
        db.String(100),
        nullable = False
        )
    business_id = db.Column(
        db.Integer,
        db.ForeignKey('business.id'),
        nullable = False
    )
    description = db.Column(
        db.Text(255),
        nullable = False
        )
    price = db.Column(
        db.Float,
        nullable = False
        )
    quantit = db.Column(
        db.Integer,
        nullable = False
    )
    stock = db.column(
        db.Integer,
        default = 0
    )