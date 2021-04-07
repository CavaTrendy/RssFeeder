from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///trouble.db"
db = SQLAlchemy(app)

from rss import routes,models
