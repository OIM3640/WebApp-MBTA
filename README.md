# WebApp-MBTA
 This is the base repository for Web App Development project. Please read [instructions](instructions.md). 

## Project Writeup
 A summary of the project and our team's reflections.

### Project Overview
 The project, titled "WebApp-MBTA," is a web application designed to enhance user accessibility to public transportation in the Greater Boston area. Leveraging Flask, Python, Mapbox API, MBTA API, JSON, and urllib, the application offers a seamless search experience where users can input diverse queries, ranging from specific locations to other identifiable information (i.e., 'MCPHS'), and receive information on the nearest MBTA station along with its accessibility status. The integration of Mapbox API ensures accurate geolocation services, while the MBTA API provides real-time data on mbta stations and their accessibility. 
 
 Going beyond basic requirements, the project incorporates an intuitive user interface developed with HTML, CSS, and JavaScript, fostering a user-friendly experience. The frontend allows users to interact effortlessly with the application, making the process of finding the nearest station a visually engaging and efficient task. Furthermore, the project emphasizes data integrity and responsiveness by utilizing JSON for efficient data exchange between the frontend and backend. Overall, "WebApp-MBTA" not only facilitates convenient access to public transportation information but also demonstrates a harmonious blend of diverse technologies for a robust and user-centric application.

### Reflection
 The project was broken down into three segments: 1 - Python functionality, 2 - Front-end development, and integration, 3 - Bug fixes, touch-ups, etc.

 In general, from the process point of view, the team worked smoothly and efficiently. To give some specific examples, at stage 1, one thing that went well was creating small functions that could then be called in a large function to perform the entire project functionality in one call. Ensuring all of our functions would pass through parameters that were returned by the prior function was a rewarding exercise and analytically engaging. On the flip side, one thing that was difficult was organizing the data we were gathering from each API. Selecting the correct data structure for the data we were using within our functionality was challenging, but after consulting different online sources, we believe we chose the right structures. It now makes sense why we store data in different structures, and we have become a lot more familiar with accessing data differently across these structures. We utilized and navigated within dictionaries, lists, and tuples for this project.

 Example 1 - Storing data using tuples, accessing data in dictionaries:
 ![image](https://github.com/OIM3640/WebApp-MBTA/assets/97844882/df4a2626-a4ab-45d5-a79f-76b001c4adb1)

 Example 2 - Storing data using lists, using dictionary methods:
 ![image](https://github.com/OIM3640/WebApp-MBTA/assets/97844882/dbd8250d-0d8d-4f7c-8209-ec29de9b33b3)

 Additionally, the team worked quite collaboratively in this project, ensuring we were utilizing each others' skills to the best of our ability. In general, the work was broken down across the team as:
 Stephen - python initial functioning and setting up web app landing
 Rohan - flask integration, error handling, web app results page
 We chose to not initially break up the work, and instead wanted to see which section we both enjoyed doing the most. Stephen found satisfaction with the python functionality and interacting with the APIs, whereas Rohan found more satisfaction with the front-end and flask integration aspects of the project. One thing that the team could do in the future to be more efficient is to define the scope of the project and try to itemize the different tasks/requirements for the project, and have each team member choose which tasks they would like to complete--kind of like a scrum. 


 ![image](https://github.com/OIM3640/WebApp-MBTA/assets/97844882/e99aabf8-5f94-41b3-97f5-476411bcaede)

 A massive concept that the team got better at was utilizing flask and understanding how to write code with the intention that it would be easily accessible for the front-end to executive it. Ensuring variable names were simple, our program's architecture made sense, and double checking all different end-user inputs for our program allowed the team to grow and see more of the nuances of programming. Additionally, learning how to test different inputs and handle errors using try and except was insightful, and it was interesting to see how simple this error handling can be, and how hard one can make it on themselves. ChatGPT was very helpful for understanding error messages (i.e., list indices cannot be strings ^_^), and how to avoid these errors with proper code. Additionally, ChatGPT was very helpful for implementing flask and jinja for our app. We queried ChatGPT to assist with pulling data from the front-end to the backend, and vice-versa. 

 Example 3 - Flask code + passing arguments:
 ![image](https://github.com/OIM3640/WebApp-MBTA/assets/97844882/338be4c1-a274-45d7-8910-4ad156f5f083)

 Example 4 - Error handling:
 ![image](https://github.com/OIM3640/WebApp-MBTA/assets/97844882/f79d9960-a339-4ec9-b307-171f211e7b02)

 #### We hope you learned more about the project, and feel free to test out the code!
