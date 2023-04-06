# WebApp-MBTA
**Group members: Matteo Sta Maria, Xue Zhen Ng**

## 1. Project Overview (~1 paragraph)

<!-- Write a short abstract describing your project. Include all the extensions to the basic requirements.  -->

## 2. Reflection (~3 paragraphs + screenshots)

### Process
<!-- Discuss the **process** point of view, including what went well and what could be improved. Provide reflections on topics such as project scoping, testing, and anything else that could have helped the team succeed. -->


For this project, we utilized bootstrap to add dynamic elements to our web app, including beautifying the landing page and form validation. We also decided to add more features to our webpage - current weather and mapbox map. 

What went well was that our webpage was able to give the outputs of the nearest MBTA, and the map was able display search results for the user's input. However, we were unable to pass data dynamically from the flask app itself directly into javascript, to pass the coordinates of the user's input from the flask function using handlebars. Thus, to work around this, we were able to access the data from the HTML section, and then use DOM manipulation to access the hidden element to obtain the innerHTML value - which is the coordinates that we want. 

||Screenshots from the webapp|
| ----------- | ----------- |
| landing page form | <img src="images/landing_page.png"> |
| form validation for no input | <img src="images/form_validation.png"> |
| successful output | <img src="images/results.png"> |
| no search results output | <img src="images/no_results.png"> |
| location does not exist output (raise Exception "Address entered does not exist")| <img src="images/non-existent.png"> |


### Team's Work Division
<!-- Discuss your **team's work division**, including how the work was planned to be divided and how it actually happened. Address any issues that arose while working together and how they were addressed. Finally, discuss what you would do differently next time. -->

### Things learnt
<!-- Discuss from a learning perspective, what you learned through this project and how you'll use what you learned going forward. Reflect on how ChatGPT helped you and what you wish you knew beforehand that could have helped you succeed. Consider including screenshots to demonstrate your project's progress and development. -->

We learnt how to utilize a flask app, and to redirect user to a html file. We also learnt about dynamically accessing and passing data through props using flask, and then accessing the data from the html file. 

We also learnt how to use python libraries such as urllib.parse to convert the user's string input into url form, which can then be passed into the URL to access the mapbox API. 