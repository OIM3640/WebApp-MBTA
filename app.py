"""
application that can find the nearest MBTA and shows whether it is wheelchair accessible using Flask
"""

from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def show_location():
    if request.method == "POST":
        location = request.form['location']
        station, wheelchair_accessible = find_stop_near(location)
        return render_template('index-result.html', location=station, wheelchair_accessible=wheelchair_accessible)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
