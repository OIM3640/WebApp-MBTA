from flask import Flask, render_template, request, redirect, url_for

from code_MBTA import find_stop_near, get_lat, get_long

app = Flask(__name__)



"""Define a route of the webside to the default route"""
@app.route("/home", methods=["POST","GET"])
def home():
    if request.method == "POST":
        street = request.form["street"] 
        city = request.form["city"]
        state = request.form["ma"]
        return redirect(url_for("closest",name=street+','+city+','+state))
    else:
        return render_template("index.html")


@app.route("/<name>")
def closest(name):
    return f"nearest station:{find_stop_near(name)}! "

if __name__ == "__main__":
    app.run(debug=True)