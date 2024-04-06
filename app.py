from flask import Flask, redirect, render_template, request, url_for
from mbta_helper import find_stop_near, get_realtime, get_temp, get_city, get_nearby_events


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
    temperaturef = get_temp(place_name)
    temperaturec = round(5 / 9 * (temperaturef - 32),2)
    citys = get_city(place_name)
    events = get_nearby_events(place_name)
    return render_template(
        "render_station.html",
        place=place_name,
        station=nearest_station,
        wheelchairs=wheelchair,
        temp=temperaturef,
        tempc=temperaturec,
        starttime=start,
        endtime=end,
        city = citys,
        event = events
    )


# This handles any 404 error for the website
@app.errorhandler(404)
def page_not_found(error):
    return (
        render_template(
            "error.html",
            error_message="Mmmm... my colleage Steve just chewed your page. Try again later perhaps?",
        ),
        404,
    )


if __name__ == "__main__":
    app.run(debug=True)
