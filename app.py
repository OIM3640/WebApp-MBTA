
from flask import Flask, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route('/stopfinder/', methods=["GET", "POST"]) 
def get_station():
    if request.method == "POST":
        city_name = request.form["city"]
        try:
            nearest_stop = find_stop_near(city_name)
            return render_template("station_result.html", city=city_name, stops=nearest_stop)
        except:
            return render_template("station_error.html") , 'Location Not Found'
    return render_template("station.html")
    



if __name__ == '__main__':
    app.run(debug=True)
