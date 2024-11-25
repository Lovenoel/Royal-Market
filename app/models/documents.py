from . import db


class Document(db.Model):
    """A Documents class model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    last_updated = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        """Returns a string representation of documents object."""
        return f'<Documents {self.title}, {self.last_updated}>'