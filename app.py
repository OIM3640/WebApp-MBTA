# This website will help people find a nearby MBTA station and other information by providing an address or point of interest.
from flask import Flask
from flask import request, render_template  # used to render html templates
from mbta_helper import (
    get_lat_long,
    find_stop_near,
)  # importing functions from mbta_helper

app = Flask(__name__)


# this was done with code inspiration from the weather example we did in class
@app.route("/mbta/", methods=["GET", "POST"])
def mbta_stop():  # includes function in mbta_helper.py, will be called when '/mbta/' is accesed in the web
    if (
        request.method == "POST"
    ):  # checking if the incoming request is a POST request, this method is used to send data to the server
        place_name = request.form["place_name"]  # getting the placec name using POST

        stop_name, wheelchair_accessible = find_stop_near(
            place_name
        )  # calling find_stop_near with place_name which returns the stop name and if its wheelchair accessible or not

        if stop_name:  # checks if stop name was found or not
            accessibility_status = (
                "wheelchair accessible"
                if wheelchair_accessible
                else "not wheelchair accessible"
            )
            return f"The nearest MBTA stop to {place_name} is {stop_name} and it is {accessibility_status}."
        else:
            return f"Could not find the nearest MBTA station for {place_name}"

    else:  # if no stop was found
        return render_template(
            "index.html"
        )  # sends back the content of the index.html file as a webpage in response to a GET request


#     else:
#         return f"Location not found: {place_name}" #for  invalid address or location not found

if __name__ == "__main__":
    app.run(debug=True)
