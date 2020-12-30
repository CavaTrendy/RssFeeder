from flask import Flask, render_template
import rss



app = Flask(__name__)


@app.route("/home")
# def index():
#     return '<h1>Hello world!</h1>'
def hello():
    feed_dict = rss.new_data
    return render_template('home.html', feed=feed_dict)

if __name__ == '__main__':
    app.run(debug=True)