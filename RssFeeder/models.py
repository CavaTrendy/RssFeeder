from main import db
from datetime import datetime

class Post (db.Model):
    id = db.Column(db.Integer,primary_key = True)
    source = db.Column(db.Text, nullable = False)
    title = db.Column(db.Text, nullable = False)
    date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    link = db.Column(db.String , nullable = False)
    
    def __repr__(self):
        return print("Post('{self.title}', '{self.date_posted}')")
