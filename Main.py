from flask import Flask, render_template
import rss

feed_dict = rss.files

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('home.html', feed_dict=feed_dict)