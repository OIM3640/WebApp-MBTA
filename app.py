"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
MAPQUEST = 't4D6lrgBv1A3GziGDewd3iG2CK0qQVNs'
MBTA_API = '6cbb9987c1e94035a98b7ec078de747b'
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
