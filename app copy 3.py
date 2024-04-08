from flask import Flask, render_template, request, redirect, url_for
from mbta_helper import get_nearest_station, find_stop_near, get_weather

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """
    Renders the welcome page for the MBTA application.
    """
    return render_template('welcome_page.html')

@app.route("/", methods=["POST"])
def mbta():
    """
    Handles the POST request for the MBTA application.
    """
    place_name = request.form.get("place_name")
    if place_name:
        try:
            stop_name, wheelchair_accessible = find_stop_near(place_name)
            weather_info = get_weather(place_name)
            return render_template('station_info.html', place_name=place_name, nearest_stop=stop_name, wheelchair_accessible=wheelchair_accessible, weather_info=weather_info)
        except Exception as e:
            return redirect(url_for('error', error_message=str(e)))
    else:
        return redirect(url_for('index'))

@app.route("/station/<stop_name>", methods=["GET"])
def stop_info(stop_name):
    """
    Renders the station information page.
    """
    return render_template("station_info.html", stop_name=stop_name)

@app.route("/error/", methods=["GET"])
def error():
    """
    Renders the error page.
    """
    error_message = request.args.get('error_message', 'An unknown error occurred.')
    return render_template("error_page.html", error_message=error_message)

@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 errors.
    """
    return render_template("error_page.html", error_message="Page not found."), 404
      
if __name__ == "__main__":
    app.run(debug=True)
