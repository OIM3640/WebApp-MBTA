from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.get('/')
def nearest_mbta_get():
    return render_template("index.html")

@app.post("/nearest_mbta")
def nearest_mbta_post():
    place_name = request.form["place_name"]
    station_name, wheelchair_accessible = find_stop_near(place_name)
    if "there is no stop nearby" in station_name:
        return render_template("error.html", location=place_name)
    return render_template("mbta_station.html", station=station_name)
    # station_name, wheelchair_accessible, vehile_type, time_until_arrival = find_stop_near(place_name)

if __name__ == '__main__':
    app.run(debug=True)
