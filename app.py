"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, request, render_template
from backup import find_stop_near



app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        place_name = request.form["name"]
        (location, accessible) = find_stop_near(place_name)
        return render_template("index.html", city = place_name, stop = location, wheelchair = accessible)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run()
    app.config['DEBUG'] = True
