
# from crypt import methods
from operator import methodcaller
from flask import Flask, render_template, request
from config import MAPQUEST, MBTA_API
import mbta_helper

app = Flask(__name__)


@app.route('/mbta/', methods=["GET", "POST"])
def get_mbta():
    if request.method == "POST":
        location_name = request.form["location"]
        find_stop = mbta_helper.find_stop_near()
        return render_template("mbta-result.html", location=location_name, mbta_stop=find_stop) #replace temp with something

    return render_template("mbta-form.html")


if __name__ == '__main__':
    app.run(debug=True)



