from datetime import datetime
from app.app import db


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, index=True, unique=True, nullable=False)
    auther = db.Column(db.String)
    description = db.Column(db.Text)
    isbn_code_10 = db.Column(db.String)
    isbn_code_13 = db.Column(db.String)
    thumbnail_small = db.Column(db.String)
    thumbnail = db.Column(db.String)
    total = db.Column(db.Integer, nullable=False, default=1)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now
    )
