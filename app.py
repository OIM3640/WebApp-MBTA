from flask import Flask, render_template, request
import mbta_helper

app = Flask(__name__)


@app.get("/")
def mbta_get():
    return render_template("index.html")

@app.post("/")
def mbta_post():
    location = request.form['location']
    nearest_station,wheelchair_accessible = mbta_helper.find_stop_near(location)
    if wheelchair_accessible:
        return f"A station near {location} is {nearest_station}, and it is wheelchair accessible"
    return f"A station near {location} is {nearest_station}, and it is not wheelchair accessible"

if __name__ == '__main__':
    app.run(debug=True)
