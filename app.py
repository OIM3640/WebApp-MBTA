from flask import Flask, render_template, request
from mbta_helper import find_stop_near, get_nearby_restaurants
import datetime


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/mbta/")
@app.get("/mbta/")
def mbta_get():
    return render_template("mbta_form.html")


@app.post("/mbta/")
def mbta_post():
    try:
        place_name = request.form["place"]
        print("place is here")
        stop_near = find_stop_near(place_name)[0]
        print(stop_near)
        if stop_near != None:
            if find_stop_near(place_name)[1] == True:
                handicap = "This station is handicap-accessible."
                print(handicap)
            elif find_stop_near(place_name)[1] == False:
                handicap = "This station is not handicap-accessible."
                print(handicap)
            elif find_stop_near(place_name)[1] == None:
                handicap = ""
                print(handicap)
        else:
            stop_near = "not available. Try another location."
            handicap = ""
        food=get_nearby_restaurants(place_name)
        print(food)

        return render_template(
            "result.html", place=place_name, station=stop_near, access=handicap, restaurants=food
        )
    except:
        return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)
