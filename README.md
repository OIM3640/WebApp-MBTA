# WebApp-MBTA
**Group members: Matteo Sta Maria, Xue Zhen Ng**

## 1. Project Overview (~1 paragraph)

<!-- Write a short abstract describing your project. Include all the extensions to the basic requirements.  -->
Our project is an MBTA helper. The point of this project is to be able to find the closest MBTA station for any given location. This required the use of web APIs such as Mapbox, an API which we used to receive a location's latitude and longtitude, along with the MBTA-realtime API in order to find the closest MBTA station to the given latitude and longtitude. We also built a Web App that allows users to interact through an interface. In order to do this, we utilized Flask, a web framework.

In addition to the basic requirements, we went above and beyond in several ways. Firstly, we utilized bootstrap to add dynamic elements to our web app, including beautifying the landing page and form validation. This led to a clean user interface that goes along with the MBTA Theme and even has a logo. Another extention we included was adding the weather in Celsius of the given location. Lastly, we used Mapbox in order to embed an actual map with the location pinned. This was done so that users get a better clarity of the surroundings, especially visually showing the nearest T stations.


## 2. Reflection (~3 paragraphs + screenshots)

### Process
<!-- Discuss the **process** point of view, including what went well and what could be improved. Provide reflections on topics such as project scoping, testing, and anything else that could have helped the team succeed. -->

What went well was that our webpage was able to give the outputs of the nearest MBTA, and the map was able display search results for the user's input. We were also able to work well as a team and delegate tasks effectively. Throughout the project, we communicated frequently to ensure we got microtasks done on-time. Our communication allowed us to ask each other for help or feedback when we were confused about something.

There were some parts that we initially struggled with but were able to figure out. For example, we were unable to pass data dynamically from the flask app itself directly into javascript, to pass the coordinates of the user's input from the flask function using handlebars. Thus, to work around this, we were able to access the data from the HTML section, and then use DOM manipulation to access the hidden element to obtain the innerHTML value - which is the coordinates that we want.

One thing we could improve on is efficiency. We found it kind of difficult to code at the same time, since pulling and pushing code may cause overlaps and some additional developments of the code to be removed. Thus, we had to let the other person know when we are working on code, when we are pushing the code, and when to pull code.

||Screenshots from the webapp|
| ----------- | ----------- |
| Landing page form | <img src="images/landing_page.png"> |
| Form validation for no input | <img src="images/form_validation.png"> |
| Successful output | <img src="images/results.png"> |
| No search results output | <img src="images/no_results.png"> |
| Location does not exist output (raise Exception "Address entered does not exist")| <img src="images/non-existent.png"> |


### Team's Work Division
<!-- Discuss your **team's work division**, including how the work was planned to be divided and how it actually happened. Address any issues that arose while working together and how they were addressed. Finally, discuss what you would do differently next time. -->

The teamwork division was not very structured. We essentially followed the chronological order of the assignment: Part 1: Geocoding and Web APIs --> Part 2: Web App --> Part 3: Wow! Factors (15%). Individual tasks were not specifically delegated. Instead, whenever someone was working on the project, they would message the other person saying they are doing a certain task. That way, 2 people aren't doing the same task. It was very important to text when we finished coding, so the other person can pull origin and get the most up-to-date code. The process was simple and text message communication was key. We also met several times in person in order to organize our thoughts, ensure we are on the same page, and delegate future tasks.

Next time, we want to meet up at the start of the project to clarify what work needs to be completed and what steps to take. For this assignment, we did not meet at the start to clarify tasks. Doing so would provide extra clarity and efficiency to the project.

### Things learnt
<!-- Discuss from a learning perspective, what you learned through this project and how you'll use what you learned going forward. Reflect on how ChatGPT helped you and what you wish you knew beforehand that could have helped you succeed. Consider including screenshots to demonstrate your project's progress and development. -->

We learnt how to utilize a flask app, and to redirect user to a html file. We also learnt about dynamically accessing and passing data through props using flask, and then accessing the data from the html file. 

We also learnt how to use python libraries such as urllib.parse to convert the user's string input into url form, which can then be passed into the URL to access the mapbox API. 
