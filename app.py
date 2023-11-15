from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/mbta/', methods=['GET', 'POST'])
def mbta():
    if request.method == 'POST':
        place_name = request.form.get('place_name')
        nearest_station, accessible = find_stop_near(place_name)

        if nearest_station:
            return render_template("station_found.html", 
                place_name=place_name, 
                nearest_station=nearest_station, 
                accessible=accessible)
        else:
            return render_template("nostations.html")
    else:
        return render_template("index.html")

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errorpage.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errorpage.html'), 500

if __name__ == '__main__':
    app.run(debug=True)