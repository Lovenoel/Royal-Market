from . import db


class Business(db.Model):
    """A business class model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    online_available = db.Column(db.Boolean, default=True)
    offline_available = db.Column(db.Boolean, default=True)
    location = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text(255), nullable=False)

    def __repr__(self):
        """A string representation of a business object"""
        return f'<Business {self.name}, {self.location}>'