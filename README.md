# WebApp-MBTA
**By Hardik Pandey**

## Overview

I built a web program using the MBTA API and MapBox API that allows a user to enter a location and see if there is an MBTA transport option nearby, if it is wheelchair accesible, and what the weather is like in the area! 

## Reflection

I began the project with reading all the documentation provided and compiling whatever information I could in the form of links on the .py file. This was useful as there were multiple resources and I was constantly going back and forth between them attempting to piece the code together. My initial scope for the project was to just meet the requirements and then work to add features if time permitted. I ended up adding the weather feature and adding some CSS for the website. 

During the process, I tested the code quite often, keeping the wesite open on one side and checking for what errors showed up. Debugging was the most time consuming part of the process. It started with a KeyError due to naming issues. This is where I think I could've done better. Instead of scrambling to look for a solution, I should've read the traceback call on the website properly, as it showed which line had the error! Ultimately I did fix it after reviewing the MBTA documentation. I also had an issue with showing an error message if there was no station near the locaiton entered. I initially had text in the function that solved the problem, but during class (with professor) I made it into a try, except statement. The before and after are attached below.

The three primary skills I practiced in this assignment were API usage, debugging, and flask. Building the website was fun. I used the code we discussed in class mostly and then utilized [ChatGPT](https://chat.openai.com/share/f217efc8-fd84-4734-be50-55eca13553ce) to design my landing page. After that I took the same design elements to try my hand at CSS for the nearest.html page. I found the website to be easier to do, primarily because the scope for debugging is much more limited there, atleast it has been until now. This has given me an understanding of how I might approach my final project as well- in terms of scoping and managing the timeline. I have also learned simple ways of debugging, especially when working with Flask. I am looking forward to utilizing my learnings and getting started on my final project!

Before
![Alt text](image.png)

After 
![Alt text](image-1.png)