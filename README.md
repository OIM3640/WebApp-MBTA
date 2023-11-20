# WebApp-MBTA
Project Members: **Carina Hu & Max Sun**


## Project Overview 
In our project, we developed a user-friendly web application that allows users to efficiently locate closest Massachusetts Bay Transportation Authority (MBTA) stations. The website is built using Flask and it's easy to use. The user can input an address/place name, and the website displays results such as the closest MBTA station to that spot, whether if it's wheelchair-accessible, arrival_time, and status. 
The application was based on two main APIs: Mapbox API & MBTA API. The application leveraged Mapbox API to translate the address into geographical coordinates, which are then used as key information to search for nearest station using MBTA API. The predictions feature in MBTA API allows us to provide real-time transit information about the station such as arrival time and status, adding to the functionality of the application. 


## Reflection

### **What went Well & Areas of Improvment**

Successes: By using multiple blocks of functions within MBTA-helper, we were able to test the functions step by step and make changes easily. For example, after finishing the basic structure, we wanted to add additional feature by incorporating real-time data to our results. The well-establsihed structure allowed us to make that changes effortlessly by just building another function and change the call function in the "main" section. 

Areas of Improvement: One significant area of improvement was the lack of  error handling at the intial stage, especially around API interactions. This led to issues during testing when encountering unexpected responses or failures in API calls. We could've saved a lot of time in figuring out where the issues come from if we implemented error handling code at the beginning. In addition, we could've read through the MBTA API documents more carefully to understand how to use some of the API features such as sorting. 


### **team's work division**
Our initial plan was to work together on the document to keep track of progress. However, we realized this plan required us to frequently commit our responses because we cannot see each other's progress simultaneously. So we decided to distribute the work as such: 

Max worked on building the initial structure of the web application and focused mainly on the MBTA-helper functions. Carina worked on optimizing the MBTA-helper code and the Flask application part. 

This plan worked really well in terms of improving efficiency. However, we identified some areas of improvement throughout the process for future considerations. For example, we should still commit out responses regularly and maintain frequent communication even though we are working separately on different parts as both sections are interrelated. Building the flask requires understanding of the MBTA helper while improving flask may need modifications from the MBTA helper. The team was able to resolve the issue by helping each other udnerstand the codes they wrote and worked together to modify both parts together. 

### **Project Learnings**

From this project, both team members were able to gain more practice knowledge on API integrtion and Flask by applying classroom knowledge to solve a real issue. It was especially useful to learn how to fetch real-time data and display the results through Flask. One additional knoweldge we learned was the importance of error handling, which is an effective approach to signal any issues within the application. Going forward, we will make sure to include error handling as part of our process to improve the feasibility and efficiency of our code. Another piece of knowledge that may seem minor is to read documents fully if we plan to incorporate external sources such as API. It could've saved us a lot time if we learned about the sort function in MBTA function ahead of time.

ChatGPT was a very useful tool that helped us optimzie code efficiency and identy/solve occuring issues. For example, after we finished the basic structure of the project, we encountered issue with retriving results from our flask application. So we send ChatGPT our code and asked it to detect any issues and provde areas of improvement. It provided a very detailed and useful answer, as shown in this image: 

![Alt text](image.png)

while we were stuck with integrating real-time to our application, ChatGPT provided a good outline that allowed us to understand what information are needed to build such function (adding the stop_id filter)
![Alt text](image-2.png)

We wish we had more knoweldge/awareness towards error handling so we also asked chatgpt to provide us examples on error handling methods related to this project, which further enhanced the learning process. 

![Alt text](image-1.png)