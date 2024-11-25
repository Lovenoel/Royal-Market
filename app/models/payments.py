from . import db


class Payment(db.Model):
    """A payment class model."""
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    order = db.relationship('Order', backref='payment', lazy=True)