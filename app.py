from flask import Flask
import pprint

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello WOrld"


if __name__ == '__main__':
    app.run(debug=True)
