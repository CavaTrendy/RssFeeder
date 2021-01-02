from flask import Flask, render_template
import rss

feed_dict = rss.topics_dict

app = Flask(__name__)


@app.route("/")
# def index():
#     return '<h1>Hello world!</h1>'
def home():
    # feed_dict = rss.new_data
    return render_template("home.html", feeds= feed_dict)

if __name__ == '__main__':
    app.run(debug=True)

