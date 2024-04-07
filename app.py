from flask import Flask, redirect, render_template, request, url_for
from mbta_helper import find_stop_near, get_lat_lng, get_events

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        place_name = request.form.get('place_name', '')
        if place_name:  
            # Get latitude and longitude for the place name
            latitude, longitude = get_lat_lng(place_name)
            if latitude and longitude:
                station_name, is_accessible = find_stop_near(place_name)
                events = get_events(latitude, longitude)
                if station_name is None:
                    return render_template('error.html', error_message="Your address is valid but no nearby MBTA station found. Try again?")
                else:
                    return render_template('mbta_station.html', station_name=station_name, is_accessible=is_accessible, events=events)
            else:
                return render_template('error.html', error_message="Your address is invalid. Try again?")
        else:
            return render_template('index.html', error_message="Please enter a valid place name.")
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error_message='There seems to be an connection issue. Try agin later, or check your internet')

if __name__ == "__main__":
    app.run(debug=True)

