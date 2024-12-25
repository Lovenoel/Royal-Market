from . import db
from datetime import datetime, timezone
from models.baseModel import BaseModel

class Shipping(BaseModel):
    __tablename__ = 'shipping'
    
    order_id = db.Column(db.String(36), db.ForeignKey('orders.id'), nullable=False)
    shipping_address = db.Column(db.String(255), nullable=False)
    shipping_method = db.Column(db.String(50), nullable=False)  # e.g., Standard, Express
    shipping_status = db.Column(db.String(50), nullable=False, default='pending')  # e.g., pending, shipped, delivered
    shipped_date = db.Column(db.DateTime, nullable=True)
    delivery_date = db.Column(db.DateTime, nullable=True)
    
    order = db.relationship('Order', back_populates='shipping')

    def __repr__(self):
        return f"<Shipping {self.id} - Order: {self.order_id}, Status: {self.shipping_status}>"
