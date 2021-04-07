
from flask import render_template, flash, request
from rss.__int__ import app, db


from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField





# @app.route("/")
# def home():
#     return render_template("home.html")


# @app.route("/")
# def rss():
#     # flash('Your post has been updated!', 'success')
#     # posts = Post.query.all()
#     return render_template("rss.html", data=data)
