## Project Overview:

This is a project that takes the location from a user and pin points their location in latitude and longitude. Using this information, we run it through a MBTA API where we cross reference the coordinates to find the closest MBTA stop. Once we have the figured out, we get access to a bunch of other data from the station. With this, we can verify whether or not the station is wheelchair accessible.

## Project Reflection:

What went well: We indentified the main aspects of the program well (the scaffolding helped here too). Logic-wise, we feel as though the code is sound however the only issue is reading the data that is being accessed via our API. First, with Map Quest the key was not working and then with MBTA we were able to open the JSON file but upon further investigation, it was a nested loop of dictionaries and lists. Although the code shows that we tried to navigate that, we were not able to.

Going forward, figuring out how to utilize the API is the main priority as this is what would actually allow our entire program to run. Beyond this, we would also have spent more time on the HTML to provide a better UX for users navigating our platform. Process wise, we could have added a few more APIs since there is a lot that can be done with a transportation app. If given more time, we could have used the MBTA app to pick out routes to allow users to choose routes if they want a specific train service.

Working together was strong. We were able to share research and compile ideas about the logic regarding how to approach this project and divided up tasks and research accordingly. Next time, we will push to github more frequently instead of sending each other code of messages, etc. as this gets confusing.