from flask import Flask, redirect, render_template, request
from mbta_helper import find_stop_near

# print(mbta_helper.find_stop_near("Boston Common"))
# Output: Beacon St opp Walnut St


app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/place/')
def place_get():
    return render_template("place.html")

@app.route('/place/')
def place():
    place_name = request.form.get("place")
    res1 = find_stop_near(place_name)
    return f"{res1}"


if __name__ == '__main__':
    app.run(debug=True)
