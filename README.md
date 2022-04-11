# WebApp-MBTA
 This is the base repo for MBTA project. Please read [instructions](instructions.md). 
**Project Overview** [~1 paragraph]
Our project takes a users input (location) and converts that text input into [lat, lng] coordinate via the mapquest API. We created an instance for the URL and then called it to return the coordinates after processing the locational input. We then asessed how the data was structured and extracted the coordinates. Following the extraction, all we needed to do was then create another instance for the MBTA API so we can call it. We tested the ouput on the website and understood how the data was formatted and then extracted the URL we should use to call the database from CURL. We then merely stored the lat,lng coordinates as variables that we could refference later when calling the MBTA API. We then created a dynamic url that could take in the stored variables are arguements. Following that, we sorted the MBTA stops by distance (yielding the closest locations first) and then extracted the first location provided to us. To determine if the stop was wheelchair accesible, we utilized a conditional statement to assess if the returned value was equal to 1 ( the value linked to accesibilty). If the value was present , the html form returned a "yes" and vice versa.








- **Project Reflection** [~2 paragraphs]
After you finish the project, Please write a short document for reflection [~2 paragraphs]

  1. From a process point of view, what went well? What could you improve? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for unit testing? What self-studying did you do? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?
    From a process standpoint I felt that we did well understanding the functionality requirements. We also understood how to interact with the API's. However, we became to ambitious with the HTMl styling, and complicated our process in general. Both of us had an understanding over HTMl but we spent too much time researching the styling elements and not the Flask interface. As a result, we struggled with many bugs pertaining to the extraction of user posts. Specifically, we did alot of flask tutorials on youtube. We also did alot of research with regards to font styling and spacing (HTML). Going forward, I think it will be interesting to see if I can apply these skills to produce simple (yet useful) web applications for future ideas I may have. However, before starting I wish I would have understood the interaction template between HTML and PYTHON. It was a bit difficult to understand how the two languages interact with one another (syntatically)


  2. Also discuss your team process in your reflection. How did you plan to divide the work (e.g. split by module/class, always pair program together, etc.) and how did it actually happen? Were there any issues that arose while working together, and how did you address them? What would you do differently next time?

    Me and Andrew divided the work quite evenly. Andrew had taken an HTMl class in highschool so he helped with the fundamentals. After understanding the base syntax, we both expanded our knowledge via GITHUB and Youtube.We both helped on the front end and the back-end. We didn't crystallize the work via module, we both apported what we could and participated in the areas we felt we knew best. For example, the font styling and form structure was mostly done by Andrew. I specalized more on the backend as I am better at logic oriented sequences and had less understanding over HTML. Overall, we both learned alot. We were lucky that we our personalities were compatible and allowed us to work past disagreements. Next time, I think a proper plan of action (outlining the functionality requirements and components) could have allowed us to be more efficient. 
