from rss.__int__ import db
from datetime import datetime


class Post(db.Model):
    __tablename__= "rss_feeds_posts"
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.String)

    def __init__(self, source, title, description, link, date, updated):
        self.source = source
        self.title = title
        self.description = description
        self.link = link
        self.date = date
        self.updated = updated



    # def __repr__(self):
    #     return print("Post('{self.title}', '{self.date_posted}')")

