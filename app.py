from importlib import import_module
from flask import Flask, render_template, request
from mbta_helper import find_stop_near, map_maker

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def mbta_close():
    if request.method== "POST":
        location=request.form["location"]
        try:
            stop,wheelchair, lat, long= find_stop_near(location)
            map_url = map_maker(lat,long,600,450,14)
        except TypeError:
            stop,wheelchair, map_url = "too far", "jus walk", ""
        return render_template("mbta-result.html", stop=stop, wheelchair=wheelchair,map_url=map_url)
    return render_template("mbta-form.html")




if __name__ == "__main__":
    app.run(debug=True)