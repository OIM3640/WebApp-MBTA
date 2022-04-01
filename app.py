from flask import Flask, render_template, request
from temp_helper import get_temp

app = Flask(__name__)


@app.route('/weather/', methods=["GET", "POST"])
def get_weather():
    if request.method == "POST":
        city_name = request.form["city"]
        temperature = get_temp(city_name)
        return render_template("weather-result.html", city=city_name, temp=temperature)

    return render_template("weather-form.html")


@app.route(
    '/'
)  # if website domain is www.abc.com, http://www.abc.com/ will triger the function below, hello()
@app.route(
    '/hello/<name>'
)  # if the route contains /hello/name, it will triger the function below, hello(name)
def hello(name=None):
    if name:
        # return f'<h1>Hello, {name}!</h1><p>I am excited to learn flask.</p>'
        return render_template('hello.html', username=name)
    return '<h1>Hello, world!</h1>'


# Create another route like '/square/<number>', so the webapp will display the square of the number
@app.route('/square/')  # square()
@app.route('/square/<number>')  # square(number)
def square(number=None):
    if number:
        return str(float(number) ** 2)
    else:
        return "You need to provide a number"


if __name__ == "__main__":
    app.run(debug=True)