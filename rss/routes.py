
from flask import render_template
from rss.__int__ import app
from rss.models import Post






# @app.route("/")
# def home():
#     return render_template("home.html")


@app.route("/")
def rss():
    # flash('Your post has been updated!', 'success')
    posts = Post.query.all()
    return render_template("rss.html", data=posts)
