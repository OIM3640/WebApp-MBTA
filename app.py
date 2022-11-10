from flask import Flask, render_template, request, redirect
# We pulled the functions from the helper module
from MBTAhelper import get_json, get_lat_long, get_nearest_station
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def get_stop():
    """
    this is a function to retrive the nearest MBTA stop to a user inputted location 
    """
    if request.method == "POST":
        #
        place_name = request.form["Location"]
        yield place_name

        return render_template("form.html", location=place_name)

    return render_template("form.html")


if __name__ == "__main__":
    app.run(port=5001, debug=True)
