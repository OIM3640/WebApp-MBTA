"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from config import MBTA_API

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
