# WebApp-MBTA
 This is the base repository for Web App Developement project. Please read [instructions](instructions.md). 

## Project Overview

This project uses the Flask library to construct a website with a Cyberpunk theme that provides users with the nearest station in MA, utilizing the MBTA API. Please be mindful that this is a local website where the user has to manually create a config file and note down their API keys:

```from config import MAPBOX_TOKEN, MBTA_API_KEY```  

The project then uses the API to obtain the latitude and longitude from the place entered. Be mindful that the stop search is strictly within a half-mile range; any location without a station within this range will result in an IndexError.

There is also a small Easter egg if you understand the background art. ^^

## Reflection

The mbta_helper.py is relatively straightforward. The only problem I encountered was that I didn't understand the difference between a station and a stop. Therefore, I chose to use the parent station of a given result as the station query result.

The form creation was relatively challenging. However, I followed the exact same format as the weather web app created by you, so it went smoothly. The most challenging part was when I set the homepage as the direct query page, which confused me about where I should place @app.route.

The formatting part of the web app is where I used ChatGPT to assist me. I learned a lot about style formatting, including margin, color, importing fonts, and how to set a video as a background. The most memorable lesson was when I tried to point the path of the video to the folder 'image/xxx.jpg'; Flask failed to find it because all assets need to be in a static folder. Two things that unfortunately I couldn't accomplish are:
- I wish I could display that Easter egg directly on the website, but I failed to do so.
- I wish I didn't need to hard-code the return button so that it would automatically display at the top left corner of the result page.

I did all the works, no work division.