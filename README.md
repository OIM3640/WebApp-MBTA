# WebApp-MBTA
 Team members: Linhao Jiang, Jasmine Zhang

# Project Overview

Our project aimed to assist users in locating the nearest MBTA station to their input address and checking its wheelchair accessibility status as well as other information like nearby restaurants and events. We use MAPBOX API to convert user-input addresses into coordinates, and then MBTA API with these coordinates to find the nearest subway station and assess its wheelchair accessibility status. Other APIs like OpenWeather for weather forecasts, Ticketmaster for local events, and Google Maps for restaurant recommendations. 

The core functionality of our application stays in the mbta_helper.py page, which interacts with those external APIs. The Flask framework is powered by app.py, it sets up the website and routing. When the user lands on the first page, will see a simple form where the user inputs their address via index.html, and receives detailed information on results.html, with error handling implemented in error.html. Our porject function beyond merely finding the nearest MBTA station, we also aim to include valuable local context and real-time updates. 


# Reflection (~3 paragraphs + screenshots)

One thing we changed very late in the process is that we decided to use the Google Map API to get the weather information and the city name because we found if we use MBTA API, for these places without a station nearby, we cannot output weather data, which is not logical. For the nearby restaurants for stations, we planned to use Yelp API but we found it very hard to apply and not intuitive to use, so we pivoted to Google Map API.

For mbta_helper.py, our initial version was stores in help_attempt.py, later we decided to use the template that Professor has provided because it more consistent with using urllib.request, in contrast, we initially mixed 'urllib.request' and 'request'. We believe that having consistency in using libaires can make code more uniform and easier to read.

For team collaboration, we initally planned frequent in-person meetings but due to scheduling conflicts, the approach was adjusted. Jasmine took the lead on inital development, laying down the groundwork for application, Linhao served as the debugger and perfectionist, fixed Jasmine's bugs, and enhanced functionality with applying additional APIs. Despite the shift from our initial plans, our team dynamic is very goos, we had active communication through online disscussions, we also used live-share, to effectively adoviding overlap in prograss. 

Ai helped us on project with HTML templates styling.
and
and


Overall, AI serves as an assistant, who can offer guidance and support in area where we lacked expertise and knowledge. 

After you finish the project, Please write a short document for reflection.

Discuss the process point of view, including what went well and what could be improved. Provide reflections on topics such as project scoping, testing, and anything else that could have helped the team succeed.

Discuss your team's work division, including how the work was planned to be divided and how it happened. Address any issues that arose while working together and how they were addressed. Finally, discuss what you would do differently next time.

Discuss from a learning perspective, what you learned through this project and how you'll use what you learned going forward. Reflect on how ChatGPT helped you and what you wish you had known beforehand that could have helped you succeed. Consider including screenshots to demonstrate your project's progress and development.