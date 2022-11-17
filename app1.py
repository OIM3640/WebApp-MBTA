"""
Simple "Hello, World" application using Flask
"""
import sqlite3
from flask import Flask, render_template,request, g, abort
from mbta_helper import find_stop_near

app = Flask(__name__)

# 1. 
# Hello page + input form
@app.route('/')
def home():
    return render_template("hello.html")

# 2. 
# @app post/nearest post request

@app.route('/hello', methods=["GET", "POST"])
def get_MBTA():
    if request.method == "POST":
        place = request.form.get("fname")
        MBTA = find_stop_near(place)
        if MBTA != None:
            return render_template("error.html")
        else:
            return render_template("mbta_station.html", place_name = place , stations = MBTA[0], wheelchair = MBTA[1])
        
# 3.  
# Render a page present result from part 1
# 4. 
# Or error page say the search did not work

if __name__ == '__main__':
    app.run(debug=True)
