"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request
from mbta_helper import find_stop_near, get_nearest_station, get_lat_long, get_json
from config import MAPQUEST_API_KEY, MBTA_API_KEY

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        place = request.form["location"]
        nearest = find_stop_near(str(place))

        return render_template("stop_result.html", stop = nearest[0], access = nearest[1])
    return render_template("stop_form.html")



if __name__ == '__main__':
    app.run(debug=True)
