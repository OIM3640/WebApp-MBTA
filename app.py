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



if __name__ == '__main__':
    app.run(debug=True)
