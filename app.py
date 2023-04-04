from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.get('/')
def nearest_mbta_get():
    return render_template("index.html")

@app.post("/nearest_mbta")
def nearest_mbta_post():
    place_name = request.form.get("place_name")
    station_name, wheelchair_accessible = find_stop_near(place_name)
    if wheelchair_accessible:
        wheelchair_accessible = "is" # mbta_station page will say "It is wheelchair accessible"
    else:
        wheelchair_accessible = "is not" # mbta_station page will say "It is not wheelchair accessible"
    return render_template("mbta_station.html", station=station_name, is_or_is_not_accessible=wheelchair_accessible)

if __name__ == '__main__':
    app.run(debug=True)
