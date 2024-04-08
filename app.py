from flask import Flask, request, render_template
<<<<<<< Updated upstream
from mbta_helper import (
    get_lat_lng,
    find_stop_near,
    get_real_time_nearest_station,
    get_city_weather,
    get_city_name,
    get_nearby_events,
    top_restaurants_near_station,
    MAPBOX_TOKEN,
    MBTA_API_KEY,
)

=======
from app2 import get_coordinates
from app2 import MAPBOX_TOKEN
from app2 import find_closest_mbta_stop
from app2 import MBTA_API_KEY
>>>>>>> Stashed changes

app = Flask(__name__)


# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/find", methods=["POST"])
# def find():
#     address = request.form["address"]
#     coordinates = get_lat_lng(address, MAPBOX_TOKEN)
#     lat = coordinates[0]
#     lng = coordinates[1]

#     stop_name, wheelchair = find_stop_near(address, MAPBOX_TOKEN, MBTA_API_KEY)

#     if wheelchair == [1]:
#         accessibility = "Yes"
#     else:
#         accessibility = "No"
#     return render_template("result.html", stop_name=stop_name, accessible=accessibility)


@app.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method == "POST":
            place_name = request.form.get("place_name")

            # Input Validation
            if (
                not place_name
                or len(place_name) < 3
                or not place_name.replace(" ", "").isalpha()
            ):
                error_message = "Please enter a valid location name."
                return render_template("error.html", error_message=error_message)

            nearest_stop, wheelchair_accessible = find_stop_near(place_name)
            weather_info = get_city_weather(place_name)
            nearby_events = get_nearby_events(place_name)
            top_restaurants = top_restaurants_near_station(place_name)
            real_time_info = get_real_time_nearest_station(place_name)

            return render_template(
                "results.html",
                place_name=place_name,
                nearest_stop=nearest_stop,
                wheelchair_accessible=wheelchair_accessible,
                real_time_info=real_time_info,
                weather_info=weather_info,
                nearby_events=nearby_events,
                top_restaurants=top_restaurants,
            )

    except Exception as e:
        return render_template("error.html", error_message=str(e))

    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", error_message="Page not found."), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("error.html", error_message="Internal server error."), 500


if __name__ == "__main__":
    app.run(debug=True)
