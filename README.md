Eva Lee

**1. Project Overview** (~1 paragraph)

In this project, I created a web application to get the user input of their current location to produce the output of the closet MBTA public transportation near them. The steps of the process included:
1. MBTA_help.py had functions in it that first turned a place into coordinates through using the MapBox API. Then with the coordinates, I used MBTA's API/data to find the closest public transportation near the coordinates of the current location, and to return the station, the handicap-accesibility. 
   1. I also created a function using the Yelp API to get the restaurants nearby with the highest rankings. This was also put onto the web app using HTML, and displayed in a dynamic list.
2. app.py had functions in it to route and get the functions in MBTA_help.py in order to put it into a site using Flask. 
3. The various HTML templates make up the various pages seen in the flask site.
4. I used CSS to format the site to make it much more visually pleasing and sophisticated-looking.

I chose to use the MapBox API rather than the Google API because MapBox had better customization/themming functionalities, to which I originally wanted to insert a map into the website. (https://www.softkraft.co/mapbox-vs-google-maps/). In addition I had used the MBTA API in order to get information for public transportation.

**2. Reflection** (~3 paragraphs + screenshots)

 The part of creating the functions for MBTA_helper.py went well as I had had previous expereince working with APIs and functions to get certain information. In addition, I was able to create a Flask application pretty well, and to use HTML and CSS to make the website more visually appealing. I was able to find information online on how to make a nicer heading, and messing around with the formatting, sizes, and texts of everything.

 However, what did not go well was how to put that data into visualizations and make it more appealing and easy to use for the user. I tried to put the current location and station location into a map for better visualization. While I was able to get the coordinates of both locations, I ran into trouble putting it onto and displaying it in the map for the front end, and had to scrap it in the end. In addition, it was also difficult using the MapBox API and figuring out the different ways I can use it. 

 In the end, I opted to use the Yelp API instead to get restaurants closeby to the location inputted by the user. My thinking was that some people might get hungry waiting for public transportation.

 In terms of the website side of things, one challenge that I faced and use unable to mitigate was inserting a logo for the website. The logo just would not load on the website, despite me decompressing it, resizing it, and changing it. In the end, I opted to insert a heading instead. Yet, I was able to learn how to create dynamic lists and loop using HTML, which was a success.

 In terms of project scoping, I was able to complete the core of the project in adequate time. But when I was searching for ideas to do the WOW factor, I tended to lean toward the ideas that were a bit out of scope. For example, I tried to see if I could get the color of the MBTA train that corresponds with the location displayed, only to discover that there isn't enough information on the color of the lines in the data provided by the MBTA. Then, I tried to see if I could put a map on the website to demonstrate the distance between the current location and station location. But I could not find a way to link the coordinates of the location to the map on the front end. If I had more time I would try to do a deeper search online for MBTA data and also experiment more with mapping, either with MapBox or with Google Maps to see if I can come up with a way to display a map.  

 Through this project, I was able to learn a lot about building a web application and utilizing different APIs. I have used a variety of tools to help me throughout this project. Firstly, this website: https://jsonformatter.curiousconcept.com/ . This website helped me a lot when I was looking at the JSON files when I was doing this project.

 ChatGPT in particular has helped me with learning about new things and debugging. For this project, however, I have found it very unhelpful. I tried to use it a lot to implement the WOW factor, but in the end, it still was not able to work. The screenshots below shows specifically the trouble I ran into with inserting a map, and the issue ChatGPT was unable to help me resolve.

 ![image](Screen%20Shot%202023-04-05%20at%205.43.56%20PM.png)
 ![image](Screen%20Shot%202023-04-05%20at%205.42.19%20PM.png)

I worked alone for this project, and to split up the work I had separated parts of the project into smaller parts to be completed over the course of the days before it was due. In turn, I was able to get a consistent work process, where I had time to troubleshoot any problems and add to my code before the deadline if I had new thoughts.

Going forward, I see myself using Flask, HTML, CSS, the JSON formatter website, and ChatGPT more to help me to create visually appealing websites and web applications, and to help me discover new ways to code, while understanding and viewing JSON files. In addition, I will be more conscious about project scope going forward and also the limitations of ChatGPT.
