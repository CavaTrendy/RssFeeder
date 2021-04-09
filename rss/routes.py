
from flask import render_template
from rss.__int__ import app, db
from rss.models import Post
from rss.creation_rss import new_data






# @app.route("/")
# def home():
#     return render_template("home.html")


@app.route("/")
def rss():
    # flash('Your post has been updated!', 'success')
    # for d in new_data:
    #     post_dic = Post(source=d["source"], title=d["title"], description=d["description"], link=d["link"],
    #                     date=d["date"])
    #     db.session.add(post_dic)
    #     db.session.commit()
    posts = Post.query.order_by(Post.date.desc())
    return render_template("rss.html", data=posts)
