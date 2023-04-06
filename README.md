# WebApp-MBTA by Matthew Syrigos & Lily Ichise

[Markdown format](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

## 1. Project Overview (~1 paragraph)

This project is a web application that finds the nearest MBTA station based on a user's location input, and provides additional information such as wheelchair accessibility, a map with the location of the nearest MBTA station, and the current temperature of the location the user inputted. 

The project uses the MBTA API to retrieve MBTA stop information and the OpenWeatherMap API to retreive weather information. Extensions to the basic requirements incude the flask web application used to create a user friendly interface, the map display showing the location of the station, the weather information that is provided with the help of OpenWeather API, the error handling securing the program from wrong entries and the wheelchair accessibility and location information, generated with the help of mbta helper and geolocation APIs. All the extensions used improve the user experiance and provide additional information, making the application more useful and engaging for users.

The Flask web framework is also used to handle HTTP requests and render HTML templates.

## 2. Reflection (~3 paragraphs + screenshots)

**1. The process**  
well and what could be improved. Provide reflections on topics such as project scoping, testing, and anything else that could have helped the team succeed.

**2. Team's work division**  
including how the work was planned to be divided and how it actually happened. Address any issues that arose while working together and how they were addressed. Finally, discuss what you would do differently next time.

**3. Learnings**  
Throughout this project, we were able to learn a lot about the basics of web development and the Flask framework. This project helped us gain a better understanding and comfortability with taking user inputs and integrating multiple APIs, as well as displaying information in a user-friendly format. ChatGPT was a huge help in contributing to our learnings, as it was particularly useful in helping us understand how to use certain Python libraries and improve our code with suggestions when we got stuck with stubborn errors. Going forward, we will use our knowledge of APIs and the Flask framework on our final project of matching students with shared interests to study groups via a web application. If we wished we knew anything beforehand that could've helped us succeed, it would've been that if you want to include a map on the same result page as the nearest station, you have to include it in the same function under app.py.

![](images/apppy_progress.png)
