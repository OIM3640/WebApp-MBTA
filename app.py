"""
Simple "Hello, World" application using Flask
"""
 
from flask import Flask, render_template, request 
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/mbta/', methods = ["GET", "POST"])
def mbta_station_name():
    if request.method == "POST":
        place_name = request.form["Location"]
        closest_station = find_stop_near(place_name)
        return render_template("MBTA-Result.html", location = place_name, MBTA_Station = closest_station)
    return render_template("MBTA_Result.html")

if __name__ == '__main__':
    app.run(debug=True)