from flask import Flask
from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route('/', methods=['',''])
def show_station():
    return 'hello worldhhh!'


if __name__ == '__main__':
    app.run(debug=True)
