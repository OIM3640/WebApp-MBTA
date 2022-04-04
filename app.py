"""
Web App to find nearest MTBA station to your location!
"""

from tkinter import Place
from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def nearest_mbta_station():
    if request.method == "POST":
        location_name = request.form["Location"]
        result = find_stop_near(f"{location_name}")
        return render_template(
            "result.html",
            location=location_name,
            station=result[0],
            wheelchair_status=result[1],
        )
    return render_template("index.html")


# https://flask.palletsprojects.com/en/2.0.x/errorhandling/
@app.errorhandler(Exception)
def handle_bad_request(e):
    return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)
