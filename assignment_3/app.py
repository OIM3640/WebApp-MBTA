# from crypt import methods
from flask import Flask, render_template, request
from config import MAPQUEST, MBTA_API
from mbta_helper import find_stop_near

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/mbta/', methods=["GET", "POST"])
def get_mbta():
    if request.method == "POST":
        location_name = request.form["location"]
        find_stop = find_stop_near(location_name)
        return render_template("mbta_result.html", location=location_name, mbta_stop=find_stop) #replace temp with something

    return render_template("mbta_form.html")


if __name__ == '__main__':
    app.run(debug=True)



