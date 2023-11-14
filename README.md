# WebApp-MBTA
 This is the base repository for Web App Developement project. Please read [instructions](instructions.md). 

Niusha Nikpour 

## 1. Project Overview (~1 paragraph)

In my project, I developed a web page with an interactive form. Users can enter a location within the vicinity of a MBTA station, and the page responds with the nearest MBTA station to the entered location and it tells the user whether the station is wheelchair accessible or not. I integrated the Openweather API so users can see the description of the weather at that specific location of the station. I also added the exact temperature in Kelvins. This way, users can not only see the temperature outside, but if it is raining, snowing, cloudy, sunny, etc. Having the combination of which station to take and the weather information lets the user make better informed decisions prior to leaving wherever they are.

## 2. Reflection (~3 paragraphs + screenshots)

   **process**
   I think that the beginning of the process went well. When I was doing the MBTA part, I was able to do it in a reasonable amount of time. Setting up the HTML aspect was fairly easy for me since I have taken Web Tech before so I just had to refresh myself on some aspects. The hardest part was implementing other APIs on top of what I had done. I definitely think I could have improved on that. I spent many more hours trying to get the Eventbrite API to work and it never ended up working. I did prioritize functionality of my web page over it having extra APIs. I could not get my web page to even load anything when trying to implement the Eventbrite API, but I got the Openweather API to be functional. 
   
   I was surprised that the hardest part wasn't setting up the original code but making it have more functions. I think I could improve on knowing how to add functionality but alse knowing when something just is not going to work even if I spend time on it. I tested my code after every single change just so I could see what would have an effect on my code at all. I think it helped me a lot to test a lot just so I would be able to verify what part of my code and what part was not functioning.

   **team's work division**
   I did my work individually so there was no division that needed to be done.

   **learning**
   I learned how to implement APIs on Flask and how useful they can be when doing a project like this. I think the biggest thing I learned was the interactiveness of APIs and the different use cases. They offer so much information and you can choose what parts of the information you would like the user to see.  
   
   
   Chat GPT helped me with a certain function.

![Chat GPT](<Screenshot (90).png>)
![Chat GPT pt.  2](<Screenshot (91).png>)

   I got stuck and was unsure on how to continue, so it was helpful and saved time having it figure it out for me. However, I had a lot of issues and errors with my code that even with Chat GPT trying to help, I could not get to work. SO this showed me that Chat GPT cannot solve any problem and there are times where I need to be able to catch the problem myself. Especially with multiple files having my project, it is more difficult for Chat GPT to catch small or even large mistakes. I still find it helpful but this project was the least helpful I have found Chat GPT to be.


   These are a few photos of progress from my code.

![Code Progress](<Screenshot (89).png>) 
- This screenshot shows my code when I was trying to implement all my APIs. I did not end up using this exact function for my index.

![Eventbrite Issue](<Screenshot (86).png>)
- This picture shows the functions for the Eventbrite code that I could not get to work. I ended up commenting it out so I could still refer to it if I wanted to try and make it work. In the future I would like to go back to it and try to figure it out. 

I wish I had more insight on APIs in terms of which ones exist and how to implement them in a more efficient way. I am dissapointed that I could not get the Eventbrite API to work but I am still happy that my Flask and web page were able to work with the MBTA and Openweather APIs.