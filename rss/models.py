from rss.__int__ import db
from datetime import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, source, title, link, date):
        self.source = source
        self.title = title
        self.link = link
        self.date = date



    def __repr__(self):
        return print("Post('{self.title}', '{self.date_posted}')")
