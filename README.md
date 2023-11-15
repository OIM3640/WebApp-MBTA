# WebApp-MBTA
 This is the base repository for Web App Developement project. Please read [instructions](instructions.md). 

# Project Overview
My Project is designed to asist users in locating the nearest MBTA station, check its wheelchair accesssibility status, and obtain the current temperature based on a provided place name. Buil using Flask framework, this web application allows users to submit a place name on the website through a `form subimisssion`. the route would then renders a `GET requests` and process form submissions(user's input) for `POST requests`. In case of an incorrect place name or an unexpected error, the application will render an error page along with a link redirect users back to the home page. To achieve these functionalities I developed 2 external modules including `mbta_helper.py` for finding the nearest MBTA station and `weather.py` for retrieving and displaying the current temperature. Additionally, I created three HTML templates to enhance the user interface: `index.html` for the homepage, `nearest_station.html` for displaying results, and `error.html` for presenting error page.

# Reflection
## Process point of view
My project successfully tackeled the challenge of creating a capitvating "Wow Factor" by displaying real-time weather status of a given location. The initial steps invlved obtaining API keys from the the `OpenWeather` website and researching the approprate `URL` for fetching live temperature data. The identified `URL` (https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIKEY}) necessitates `latitude` and `longitude` information, which gives me a hint of utilizing the `get_lat_long()` from the `mbta_helper.py` module. this function extracts the corrdinates  of the given place using `Mapbox Geocoding API`, providing the necessary data for temperature retrieval.  

My project also benefitde from exploing and documenting various problem-solving approaches, enhancng my coding proficiency.

While the project has seen success, there are key areas that warrant improvement. Firstly, addressing the display of temperature units is essential. Currently set to Kelvin, considering options like Celsius or Fahrenheit would enhance user-friendliness. Secondly, attention to HTML template design and styling is crucial. There's room for refinement to elevate the visual appeal and user experience of the pages. Additionally, contemplating the inclusion of more features or enhancements can contribute to the continued development and enrichment of the web application.

## Team's work Division
I worked on this project Independently. However, I actively sought input from classmates during discussions centered around the `Wow factor` and decided that temperature feature is the most feasible and impactful enhancement for the project. I am eager to collaborate with a friend on future project, beacause I felt like discussions with classmates underscored the importance of diverse viewpoints in shaping and refining project ideas.

## Learning perspective
ChatGPT helped me on this project with the HTML templates styling. 
For example:https://chat.openai.com/share/c8ae501c-c882-475a-955f-0908ce7365ff 
I have provided my codes to ChatGPT and asked How to make a particular code bold.
![Alt text](image.png)
![Alt text](image-1.png)

Moreover, I felt like there's still so much to learn in HTML tamplates, which ChatGPT is a good tool to be used to answer our questions.
For example:https://chat.openai.com/share/4d642ae4-d91e-4704-839f-84fb55be2b89
I have asked ChatGPT about what does `<div>` meanss in HTML tamplate
![Alt text](image-2.png)

