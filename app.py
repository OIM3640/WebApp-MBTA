from flask import Flask,render_template,request
from mbta_helper import get_nearest_station


app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.route("/")
def hello():
    """
    Welcomes the user to a hello page
    """
    return render_template("hello.html")

def mbta():
    """
    uses the get_nearest_station in mbta_helper code and directs users to the corresponding html page
    """
    try:
        place_name = request.form.get("place_name")
        stop_name, wheelchair_accessible = get_nearest_station(place_name)
        return render_template("index.html", stop_name=stop_name, wheelchair_accessible=wheelchair_accessible)
    except Exception as e:
        #assigns the exception instance to variable e
        return render_template("errorpage.html", error_message=str(e))
        #passed as the error_message to the error.html template
        
def errorpage():
    """
    If anything went wrong, directs the user to an error page
    """
    return render_template("errorpage.html", error_message="HTTP 404. Your page has not been found.")
      

if __name__ == "__main__":
    app.run(debug=True)
