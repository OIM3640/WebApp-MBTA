from flask import Flask, redirect, render_template, request, url_for
from mbta_helper import find_stop_near, get_realtime


app = Flask(__name__, template_folder="templates")


@app.route("/")
def hello():
    return render_template("index.html")

@app.get("/nearest_mbta")
def temp_get():
    return render_template("index.html")

@app.post("/nearest_mbta")
def nearest_mbta():
    place_name = request.form["place_name"] 
    nearest_station = find_stop_near(place_name)[0]
    wheelchair = find_stop_near(place_name)[1]
    start = get_realtime(place_name)[2]
    end = get_realtime(place_name)[3]
    return render_template("render_station.html", place = place_name, station = nearest_station, wheelchairs = wheelchair, starttime = start, endtime = end)



if __name__ == "__main__":
    app.run(debug=True)
