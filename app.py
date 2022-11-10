from flask import Flask, render_template, request
from mbta_helper import find_stop_near
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


@app.route("/", methods= ["GET", "POST"]) 
def nearest():
    """
    Returns nearest MBTA stop and wheelchair accessibility 
    """
    if request.method == "POST":
        place = request.form["place"]
        stop, wheelchair_boarding = find_stop_near(place)
        return render_template("results.html", stop=stop, wheelchair_boarding=wheelchair_boarding
        )
    else:
        return render_template ("index.html", error=True)


if __name__ == '__main__':
    app.run(debug=True)
