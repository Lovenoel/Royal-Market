from . import db


class Article(db.Model):
    """An Articles class model."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        """Returns a string representation of the article object"""
        return f'<Article {self.title}, {self.created_at}>'
