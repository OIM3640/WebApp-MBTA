from flask import Flask, render_template, request
from mbta_helper import find_stop_near
from getweather import get_temp, get_cityid
from config import OPENWEATHERMAP_APIKEY
import sqlite3


app = Flask(__name__)

@app.route('/')
def show_station():
    return render_template("index.html")

@app.route("/nearest_mbta", methods=["POST", "GET"])
def station_post():
    if request.method == "POST":
        try:
            place_name = request.form.get("place")
            (station, wheelchair) = find_stop_near(place_name)
            temperature = get_temp(place_name)
            db = sqlite3.connect("data/stations.db")
            c = db.cursor()
            # c.execute('create table stations (place, station, wheelchair)')
            # db.commit()
            c.execute('insert into stations values (?,?,?)', (place_name, station, wheelchair))
            db.commit()
            return render_template("station-result.html", place = place_name, station = station, wheelchair = wheelchair, temperature = temperature)
        except:
            return render_template("error.html")


@app.post("/weather")
def weather():
    try:
        city = request.form.get("city")
        city_id = get_cityid(city)
        api = OPENWEATHERMAP_APIKEY
        return render_template("weather.html", cityid = city_id, api = api, city = city)
    except:
        return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)
