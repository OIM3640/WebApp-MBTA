from flask import Flask, redirect, render_template, request
from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.get("/nearest_mbta/")
def findstop_get():
    return render_template("index.html")


@app.post("/nearest_mbta/")
def findstop():
    place_name = request.form.get("place")
    if place_name.lower() == "nightcity" or place_name.lower() == "night city":
            return redirect("https://www.youtube.com/watch?v=sJbexcm4Trk") 
    stop_info = find_stop_near(place_name)

    return render_template(
        "display.html", stop_name=stop_info[0], wheelchair_accessible=stop_info[1]
    )


@app.errorhandler(IndexError)
def index_error(e):
    return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)
