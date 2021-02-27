from rss.creation_rss import rss_decoded
from flask import render_template, flash
from rss.__int__ import app, db
from rss.models import Post
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
#
data = rss_decoded


class AddRecord(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    source = StringField("source")
    title = StringField("title")
    description = StringField("description")
    link = StringField("link")
    date = StringField("date")
    # updated - date - handled in the route function
    updated = HiddenField()
    submit = SubmitField('Add/Update Record')


# @app.route("/")
# def home():
#     return render_template("home.html")


@app.route("/", methods=['GET', 'POST'])
def rss():
    # SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    # json_url = os.path.join(SITE_ROOT, "static", "feeds.json")
    # data = json.load(open(json_url))
    for d in data:
        post_dic = Post(source=d["source"], title=d["title"], description=d["description"], link=d["link"] )

    db.session.add(post_dic)
    db.session.commit()
    # form1 = AddRecord()
    # for d in data:
    #      post_dic = Post(source=form1.source.data, title=form1.title.data, date=form1.date.data, description=form1.description.data, link=form1.link.data)
    #      db.session.add(post_dic)
    #      db.session.commit()

    flash('Your post has been updated!', 'success')
    # page = request.args.get("page", 1, type=int)
    # posts = data.paginate(page=page, per_page=5)

    return render_template("rss.html", data=data)
