from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)

# @app.route("/")
@app.route('/')
def get_mbta_station():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
