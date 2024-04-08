# from flask import Flask,render_template,request
# from mbta_helper import get_nearest_station, find_stop_near, get_weather


# app = Flask(__name__)


# @app.route("/", method = ["GET","POST"])
# def mbta():
#     """
#     uses the get_nearest_station in mbta_helper code and directs users to the corresponding html page
#     """
#     if request.method == "POST":
#         place_name = request.form.get("place_name")
#         if place_name:
#             try:
#                 stop_name, wheelchair_accessible = get_nearest_station(place_name)
#                 weather_info = get_weather(place_name)
#                 return render_template("index.html", stop_name=stop_name, wheelchair_accessible=wheelchair_accessible)
#             except Exception as e:
#                 #assigns the exception instance to variable e
#                 return render_template("errorpage.html", error_message=str(e))
#                 #passed as the error_message to the error.html template
        
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template("errorpage.html", error_message = "Page not found."), 404
      

# if __name__ == "__main__":
#     app.run(debug=True)
