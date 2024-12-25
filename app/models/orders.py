from . import db
from models.baseModel import BaseModel

class Order(BaseModel):
    """ An Order model class"""
    name = db.Column(
        db.String(255),
        nullable = False
        )