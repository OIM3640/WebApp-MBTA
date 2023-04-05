from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.get('/')
def nearest_mbta_get():
    return render_template("index.html")

@app.post("/nearest_mbta")
def nearest_mbta_post():
    place_name = request.form["place_name"]
    if "There is no stop nearby" in find_stop_near(place_name):
        return render_template("error.html", location=place_name)
    else:
        station_name, wheelchair_accessible, vehicle_type, time_until_arrival = find_stop_near(place_name)
        return render_template("mbta_station.html", 
                               station=station_name, accessible=wheelchair_accessible, 
                               vehicle=vehicle_type, mins=time_until_arrival)


if __name__ == '__main__':
    app.run(debug=True)
