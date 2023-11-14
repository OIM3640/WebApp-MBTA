from flask import Flask, render_template, request, redirect, url_for
from mbta_helper import (
    get_nearest_station,
    get_lat_long,
    get_weather_info,
    get_ticketmaster_events,
    get_nearby_hotels,
)
from config import (
    MAPBOX_TOKEN,
    MBTA_API_KEY,
    OPENWEATHERMAP_API_KEY,
    TICKETMASTER_API_KEY,
    BOOKING_API_KEY,
)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        place_name = request.form.get("place_name")
        latitude, longitude = get_lat_long(place_name)
        if latitude is not None and longitude is not None:
            result = get_nearest_station(latitude, longitude)
            if result:
                weather_info = get_weather_info(latitude, longitude)
                ticketmaster_events = get_ticketmaster_events(
                    latitude, longitude, TICKETMASTER_API_KEY
                )
                hotels = get_nearby_hotels(
                    latitude, longitude, BOOKING_API_KEY
                )  
                return render_template(
                    "mbta_station.html",
                    stop_name=result[0],
                    accessible=result[1],
                    weather_info=weather_info,
                    ticketmaster_events=ticketmaster_events,
                    hotels=hotels,
                )
            else:
                return render_template("error.html")
    return render_template("index.html", greeting="Hello World!")


if __name__ == "__main__":
    app.run(debug=True)
