from flask import Flask, render_template
import os
import json
import rss


app = Flask(__name__)


@app.route("/")
# def index():
#     return '<h1>Hello world!</h1>'
# def home():
#     # feed_dict = rss.new_data
#     return render_template("home.html", feeds= feed_dict)
# def renderblog():
#     filename = os.path.join(app.static_folder, 'feeds.json')
#     with open(filename) as blog_file:
#         data = json.load(blog_file)

def showjson():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "feeds.json")
    data = json.load(open(json_url))
    return render_template("home.html" , data=data)

if __name__ == '__main__':
    app.run(debug=True)

