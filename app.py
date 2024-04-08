from flask import Flask,render_template,request, redirect, url_for
from mbta_helper import get_nearest_station, find_stop_near, get_weather


app = Flask(__name__)


@app.route("/", methods = ["GET","POST"])
def mbta():
    try:
        if request.method == "POST":
            place_name = request.form.get("place_name")
            nearest_stop, wheelchair_accessible = find_stop_near(place_name)
            nearest_stop, wheelchair_accessible = find_stop_near(place_name)
            weather_info = get_weather(place_name)

            return render_template(
                "station_info.html",
                place_name=place_name,
                nearest_stop=nearest_stop,
                wheelchair_accessible=wheelchair_accessible,
                weather_info=weather_info,
            )

    except Exception as e:
        return render_template("error_page.html", error_message=str(e))

    return render_template("welcome_page.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error_page.html", error_message="Page not found."), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("error_page.html", error_message="Internal server error."), 500


if __name__ == "__main__":
    app.run(debug=True)