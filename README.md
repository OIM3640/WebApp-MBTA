# Team: Andrew
# Project Writeup

## Project Overview
The project just completed was to build a flask webpage that would take a user's input for a Boston location and pull data from two APIs to display which MBTA station is closest and whether it was wheelchair accessible. The APIs used was Mapbox and the MBTA API. Mapbox was used to pull the longitude and latitude from a query and the MBTA API would take those coordinates and determine which MBTA station was the closest to it. First, the code to pull from the two APIs to get the data was built in the mbta_helper. After that, the functions used were imported to app.py where code to be used in the flask web page was developed. Finally, the new_index.html and error.html was used to pull the data to the flask webpage in the proper format. 

## Reflection

### Process Point of View
The process in completing this project was a little shaky. As for what went well, the general guideline to follow on how to complete the project was clear and easy to follow. What was difficult was how to connect each of the different parts of the project correctly that would make the final product fully capable of what it was meant to do. For the most part, the three main components (Pulling data from API, incorporating the functions to be used in the flask webpage, and the design of the final webpage) of the project werem't relatively hard to complete. It was a little tricky on how to properly have each part be connected to draw the correct end results. Debugging with the use of print statements was especially helpful in finding out what wasn't connecting correctly. In terms of what could be improved, the functionality of the flask webpage and the code is very limited and the use of more APIs to add in more features could make the webpage much better. 

### Team Work Division
I worked alone on this project. But if i were to do this project differently next time in terms on how to work on it, I would do a better job of turning this assignment in on time.

### Learning Perspective 
I learned a lot about how to use multiple APIs to reach a final result that was wanted. I was also able to learn on how to properly integrate code from multiple modules to then be implemented into a flask webpage. I also gained greater experience and practice in creating flask webpages based on data pulled from APIs in a different module. Throughout completing the project, I was able to better my intuition on how to debug code that was not displaying the results that was intended, mainly on where to put print statements to find the inconsistencies. I will definitely be using better debugging skills when coding in the future and to also split my code into multiple modules to help organize code better. ChatGPT has helped me immensely in creating functional code for this project. It made up for my lack in fundamental coding knowledge as long as I knew what to ask and knew how to implement it. I was not very familiar with flask and how to pull data into a flask webpage and ChatGPT helped bridge the gap in my understanding of the code. It also helped me understand how to properly format code for the use of specific APIs that I was not familiar with, like the MBTA API. 


