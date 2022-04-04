from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route('/nearest/', methods=["GET", "POST"])
def get_station():
    '''take user to the nearest page which allows them to input a location and returns a new page 
    with the nearest MBTA station and wheelchair availability'''
    if request.method == "POST":
        location = request.form["location"]
        nearest_station = find_stop_near(location)['station']
        wheelchair1 = find_stop_near(location)['wheelchair']
        return render_template("index2.html", station0=nearest_station, wheelchair0=wheelchair1)
    else:
        return render_template("index-form.html")


if __name__ == "__main__":
    app.run(debug=True)