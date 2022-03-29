"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
MAPQUEST = 't4D6lrgBv1A3GziGDewd3iG2CK0qQVNs'


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
