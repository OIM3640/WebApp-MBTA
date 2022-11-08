"""
Simple "Hello, World" application using Flask
"""

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/square/<number>')  # square(number)
# @app.route('/square/<float:number>') # no need to convert
def square(number=None):
    if number:
        return str(float(number) ** 2)
    else:
        return "You need to provide a number"


if __name__ == '__main__':
    app.run(debug=True)
