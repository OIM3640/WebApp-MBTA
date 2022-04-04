"""
Simple application allowing user to interface with logic from mbta_helper.py using Flask.
"""

from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def get_station():
    if request.method == "POST":
        place_name = request.form["place"]
        place_name = place_name.capitalize()
        station_name, w_accessibility = find_stop_near(place_name)

        return render_template("result.html", place=place_name, station=station_name, wheelchair=w_accessibility)
        
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)