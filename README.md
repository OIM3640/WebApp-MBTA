# Web App MBTA - Ashley Battiata

## 1. Project Overview

This project involves the creation of a web-based application that utilizes the Mapbox and MBTA APIs to help users find the nearest MBTA station to a given location and determine if it is wheelchair accessible. Built with Python and Flask, the application enhances user interaction through a simple web interface where users input a location name. Upon submission, the application processes this input to display real-time information about the closest MBTA station, including accessibility features. The application handles errors gracefully, providing feedback and redirection options to the user. The project meets basic requirements by displaying the nearest MBTA stop and its accessibility status but also goes slightly beyond by implementing robust error handling and MBTA arrival time.

## 2. Reflection

I worked on this project individually. I would have preferred to work with a partner, if I did, I could have implemented more features to my web application. Working on this project individually means there was both a time and skill constraint on my end. I was not able to divide up the work between two people or leverage the coding skills of a partner. With that said, I still think my project came out well for my capabilities. For the scope of the project, I made sure to include the basic requirements (MBTA stop, latitude and longitude, and wheelchair accessibility). I made sure each function worked before creating the next one. Additionally, I made sure my web app had the basic requirements before adding any additional requirements. The most I was able to do is add the mode of travel, and upcoming arrival times for the MBTA station.

I was not in a group therefore I worked on both the backend and frontend myself.

I wish I had dedicated more time to the front end. As we do not have much experience with HTML, writing the index.html template and mbta_station.html template proved to be difficult. ChatGPT was of great assistance, however, I am not comfortable coding in this language whatsoever and did not understand most of it. ChatGPT continuously helps me in error handling and debugging. A lot of the time I create a function then run it and wonder why there is no output. I would copy my code into ChatGPT and ask if it can modify my code to include error handling and debugging. This helped tremendously because when I would run it in the terminal, I was able to see what exactly didn’t work. Did it not get the longitude latitude correctly, did it not retrieve the station ID. The specificity was helpful and helped me move forward.

The most I learned from this assignment is how to combine the backend and front-end development. Though this was the most difficult part, there is much more clarity in terms of how the backend and front-end work together to create the user interface. With chatgpt's help I was able to format my upcoming arrival times. The arrival times were previously being displayed in ISO 8601 format. To make them more user-friendly, I converted them to the "HH:MM AM/PM" format. I used Python's dateutil parser to parse the ISO 8601 string and then format it as so. I was also learned how to use HTML's <style> tag to incorporate colored text into my web application. I added color by using the <style>  tag within the <head> section of the HTML document and by using inline styling with the style attribute directly on the text I wanted to modify.

## Front end Development
![Alt text](/images.py/Mbta_station.png)
![Alt text](/images.py/index.png)
![Alt text](/images.py/error.png)




