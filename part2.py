from flask import Flask, render_template, request
from mbta_helper import find_stop_near
from weather import get_temp


app = Flask(__name__)



@app.get("/")
def place_name_get():
    return render_template("form.html")

@app.post("/")
def place_name_post():
    try:
        place_name = request.form.get("place_name")
        (station, wheelchair) = find_stop_near(place_name)
        weather = get_temp(place_name)
        return render_template("mbta_station.html", place_name = place_name, station = station, wheelchair = wheelchair, weather = weather)
    except:
        return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)



