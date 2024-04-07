from flask import Flask, redirect, render_template, request, url_for
from mbta_helper import find_stop_near

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        place_name = request.form.get('place_name', '')
        if place_name:  
            station_name, is_accessible = find_stop_near(place_name)
            if station_name:
                return render_template('mbta_station.html', station_name=station_name, is_accessible=is_accessible)
            else:
                return render_template('index.html', error_message="No nearest station found in the location you")
        else:
            return render_template('index.html', error_message="Please enter a valid place name.")
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error_message='There seems to be an connection issue. Try agin later, or check your internet')

if __name__ == "__main__":
    app.run(debug=True)

