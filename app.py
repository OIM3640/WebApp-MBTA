"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template,request
from mbta_helper1 import find_stop_near

app = Flask(__name__)

# 1. 
# Hello page + input form

# 2. 
# @app post/nearest post request

@app.route('/MBTA/', methods=["GET", "POST"])
def get_MBTA():
    if request.method == "POST":
        Place = request.form["place"]
        MBTA = find_stop_near(Place)
        return render_template("Result.html", place_name = Place , stations = station , Wheelchair = wheelchair)

    return render_template("weather-form.html")
# 3.  
# Render a page present result from part 1
# 4. 
# Or error page say the search did not work + button(link) redirect to the first page
import sqlite3
from flask import Flask, render_template, request, abort, g
from mbta import find_stop_near

app = Flask(__name__)

DATABASE = 'app.db'

@app.route('/')
def hello():
    return render_template('index.html')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)