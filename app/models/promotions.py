from . import db


class Promotion(db.Model):
    """A Promotion class model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    discount = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        """Returns a string representation of promotion string."""
        return f'<Promotion {self.name}, {self.discount}>'