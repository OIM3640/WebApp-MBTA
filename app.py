"""
Simple "Hello, World" application using Flask
"""
 
from flask import Flask, render_template, request 
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def MBTA():
    if request.method == "POST":
        place_name = str(request.form["Location"])
        closest_station = find_stop_near(place_name)
        return render_template("MBTA_Result.html", location = place_name, MBTA_Station = closest_station)
    return render_template("MBTA_Helper_Form.html")

if __name__ == '__main__':

    app.run(debug=True)