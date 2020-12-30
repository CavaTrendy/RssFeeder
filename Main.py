from flask import Flask, render_template
import rss

feed_dict = rss.files

app = Flask(__name__)


@app.route("/")
# def index():
#     return '<h1>Hello world!</h1>'
def hello():
    return render_template('home.html', feed_dict=feed_dict)

if __name__ == '__main__':
    app.run(debug=True)