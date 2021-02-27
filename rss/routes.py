from rss.creation_rss import rss_decoded
from flask import render_template, flash
from rss.__int__ import app, db
from rss.models import Post
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField

data = rss_decoded
# @app.route("/")
# def home():
#     return render_template("home.html")


@app.route("/", methods=['GET', 'POST'])
def rss():
    for d in data:
        post_dic = Post(source=d["source"], title=d["title"], description=d["description"], link=d["link"] )
    db.session.add(post_dic)
    db.session.commit()
    flash('Your post has been updated!', 'success')
    # page = request.args.get("page", 1, type=int)
    # posts = data.paginate(page=page, per_page=5)

    return render_template("rss.html", data=data)
