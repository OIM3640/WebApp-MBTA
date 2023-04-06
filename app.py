from flask import Flask, render_template, request

from mbta_helper import find_stop_near, get_weather, get_lat_long, get_event

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    This code defines a Flask web application that takes a user input for a location and retrieves information on the nearest a MBTA station, current weather, and nearby events using different APIs.
    """
    # Check if  the request method is Post
    if request.method == "POST":

        # Get name from the form data (user input)
        place_name = request.form["place_name"]

        # Get latitude and longitude given the place name
        latitude, longtitude = get_lat_long(place_name)

        # Find the nearrest MBTA station to the specified coordinates
        station_name, is_accessible = find_stop_near(place_name)

        # Get temperature and weather description at the specified coordinates
        temperature, weather_description = get_weather(latitude, longtitude)

        # Get the first event happing nearby the specified coordinates
        event = get_event(latitude, longtitude)

        # If there is an event, get the name and start date
        if event:
            event_name = event[0]
            event_date = event[1]

        # or else it stores no event message for the variables
        else:
            event_name = "There are no event nearby."
            event_date = "None"

        # If all necessary data is avilable, render the result template with the data
        if station_name and temperature is not None and weather_description is not None:
            return render_template(
                "result.html",
                place_name=place_name,
                station_name=station_name,
                is_accessible=is_accessible,
                temperature=temperature,
                weather_description=weather_description,
                event_date=event_date,
                event_name=event_name,
            )
        # If there are missing data, then render error template
        else:
            return render_template("error.html")

        # If the request method is get, render the index template
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
