from . import db
from models.baseModel import BaseModel

class Service(BaseModel):
    """ A service model that inherites from BaseModel"""
    __tablename__ = 'services'
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
        db.Text,
        nullable = False
        )
    hourly_cost = db.Column(
        db.Float,
        nullable = False
        )
    duration = db.Column(
        db.Integer,
        nullable = False
    )

    # Relationship to access related business easily
    business = db.relationship('Business', backref='services')

    def __repr__(self):
         return f"<Service {self.name}, Hourly Cost: {self.hourly_cost}>"