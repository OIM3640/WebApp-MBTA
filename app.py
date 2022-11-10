"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, request, render_template
from mbta_helper import find_stop_near



app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        place_name = request.form["name"]
        nearest_station = find_stop_near(place_name)
        return render_template("index.html", city = place_name, stop = nearest_station)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
