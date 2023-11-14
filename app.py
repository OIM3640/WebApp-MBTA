from flask import Flask, render_template, request
from mbta_helper import find_stop_near, get_temp, get_lat_long

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/station/", methods=["GET", "POST"])
def find_mbta():
    if request.method == "POST":
        place_name = request.form["place_name"]

        # station information
        station = find_stop_near(place_name)

        # weather information
        latitude, longitude = get_lat_long(place_name)
        temperature = get_temp(latitude, longitude)

        return f"{station}\n The current temperature of is {temperature[0]}°F, with the low for the day being {temperature[1]}°F and the high for the day being {temperature[2]}°F."
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
