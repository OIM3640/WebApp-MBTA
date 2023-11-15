# WebApp-MBTA Reflection

#### Team Members: Joey Hudicka and Ronald Liu Jr

## Project Overview (~1 Paragraph)
#### Our project utilizes multiple APIs (Mapbox, MBTA, and OpenWeather) to help analyze a user's location, telling them the nearest MBTA station to a specified location as well as letting the user know whether or not the station is wheelchair accessible and what the current temperature is at that station. From there, we used Flask to help create a website where a user is able to input a location in the Greater Boston Area, and then obtain the information mentioned above.

## Reflection (~2-3 Paragraphs)

#### From a process point of view, everything went quite smoothly, from the scope of what we wanted to do and the testing process. A big factor that contributed to this was the fact that we were able to work in a team. Having a team member meant that we were able to  easily bounce ideas off of each other. Whenever one member hit an obstacle, the other would be able to pitch in ideas and from there, we would be able to figure it out the problem together. The only issue we ran into had to do with pair programming. With our method of working, we would have one member work on the code as the other either observed or try to do it themselves on their own computer, but this proved to a bit difficult when trying to combine our works, as it got a bit confusing which lines of code were needed and which ones were redundant.

#### As mentioned previously, the planned to divide the work evenly, however, that did provide to be a bit difficult given that the way we were pair programming involved only having one person write the code, push it to GitHub, and then the other member pulling the code to then add in their updates. However, we were able to work through this by having in person meetings, where the team member who was not coding would be able to give their input at any moment, and the team was able to solve the issues more efficiently. Next time, we will try to utilize the Live Share extension as it would allow us to collaborate on the same code without the need to sync code through pushing/pulling on GitHub Desktop.

#### Answer: We ran into a few issues when trying to recall functions in another function and when trying to incorporate the mbta_helper.py into the app.py file, where the functions weren't being transferred over properly. However, by asking ChatGPT to see what was going wrong and where the errors were occurring, we were able to understand why our code was failing and how to fix it. Here is the link to the chat dialogue we had with ChatGPT while troubleshooting errors with our code: https://chat.openai.com/share/7679e8ac-8468-4ee5-8c04-70abbc1db96c. Notably, we were able to troubleshoot why our get_nearest_station() function was not outputting a URL with a valid json that we could parse through. ![Screenshot of ChatGPT responding showing the difference between two URLs](/images/url.png) We found that the reason why the URL that the function was generating was outputting an unexpected result was due to our input. We set the input to "Babson College" which did not have an MBTA station close to it, so the output was blank. ![Screenshot of Blank response from URL](/images/blank.png) This was the expected result: ![Screenshot of expected response from URL](/images/expected.png) With ChatGPT we realized that nothing was wrong with the structure of the URL, so it had to be the coordinates inputted. After we changed the coordinates, the issue was resolved.




