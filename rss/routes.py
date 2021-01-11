
from rss.creation_rss import rss_data
from flask import render_template, request
from rss.__int__ import app

from rss.__int__ import db


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/rss")
def rss():
    # SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    # json_url = os.path.join(SITE_ROOT, "static", "feeds.json")
    # data = json.load(open(json_url))
    # for data in creation_rss.rss_data:
    #     db.session.add()
    data = rss_data
    db.session.add_all(data)
    db.session.commit()
    page = request.args.get("page", 1, type=int)
    posts = data.paginate(page=page, per_page=5)

    return render_template("rss.html", data=posts)
