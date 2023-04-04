from flask import Flask, render_template, request
from weather_helper import get_temp

app = Flask(__name__)

@app.route("/") # if website domain is www.abc.com, https://www.abc.com/ will trigger this function
@app.route("/hello/")
@app.route("/hello/<name>") # if the route contains /hello/<name>, it will trigger the function below
def hello(name=None):
    if name:
        #return f"<h1>Hello, {name}!</h1><p style='color:red'>I am excited to learn Flask.<p>"
        return render_template("index.html", username=name)
    return "Hello, world!"


# Create another route like "/square/<number>", so the web app will display the square of the integer
@app.route("/square/") # causes the message "You need to provide a number" to appear
@app.route("/square/<number>")
# @app.route("/square/<int:number>")
def square(number=None):
    if number:
        return str(float(number) ** 2)
    return "You need to provide a number"


@app.get("/temp") # show page with the data
def temp_get():
    return render_template("Weather-form.html")

@app.post("/temp") # sends data to API
def temp_post():
    city_name = request.form.get("city") # get user's imput from the page
    temperature = get_temp(city_name.replace(" ", "%20"))
    return render_template("weather-result.html", city=city_name, temp=temperature)

if __name__ == "__main__":
    app.run(debug=True) # allows one to make changes without having to restart
