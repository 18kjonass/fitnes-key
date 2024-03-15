
# Investigation

## Resources
- some of the resources i found online indacates that people are not getting a lot of running and being active outside more. this is because of the pandemic witch forced people inside and not be as well fit to run [covid effects][https://www.nytimes.com/2020/10/07/well/move/pandemic-exercise-habits-study.html].

## Research
- **Survey Results:**
    - Based on a survey I carried out i found out that a lot of my age group dont really run a lot.
    - I found out that over 70% dont do any active sport.
    - I found out that over 63% had a device that could count steps 
    - I found out when asked why over 86% said that it is not very motavating for them 

## What-If questions
- **for my what if qustion** 
    - What if the user wants to incress thier distance traveled?
    - What if the user wants to decress thier time traveled?
- these qustion will help me carry out my Basic requirements and Advanced requirements 

## Target Audience
- My device target audience is people of the older age group like 18 and over but it maybe use they the younger Audience. it is for thos who want to keep a recound on how far and fast they travel.

## Main Objectives
- i need to find a way to get peoples steps 
- i need to found out how far they travel 
- i need to find the time they toke to travel 
- i need to graph that data 
- i then need to give user feed back on that data 


# Plan and Design 
## How I will meet the requirements
### Basic Requirements
- cheak if the user is over 37 degress this is to cheak if there are sick 

- at the start the user has to put in there height this will go up in incroments of 10 cm when pressed A and 100 cm if B

- when done press A+B to conform the height which will give us the stride length of the user

- to start the run the user will have to press on the other micro bits logo to set the timer to the data base 

- the user then runs to get steps

- user presses the logo button on the micro bit witch sends data to the data base 

- i ask for age to norrow down the grouping 

- i read user data and give them a prodiction and incite on there physical wellbeing
### Advanced Requirements
- for my first what if qustion i gave "What if the user wants to incress thier distance traveled?"
    - i get the users stride, distance and time and then graph the information and then give futer incite on there wellbeing 
- for my secound what if qustion i gave "What if the user wants to decress thier time traveled?"
    - i get the users stride, distance and time and then graph the information and then give futer incite on there wellbeing 

## Technologies Used 
- 

## Detailed Flowchart

## Architecture Flowchart

# Create
## Dates

- **Week 1:**
    - i worked on investigation of the project 

- **Week 2:**
    - Worked on plan and design:
        - Listed technologies I will use based on survey results
        - Created architecture diagram and flowchart, will likely have small changes made later
    
    - Worked on the serial reader:
        - Made the program read data recieved from the serial port and write it to an SQLite database

    - Created basic draft of microbit step counter code:
        - The program simply counted steps using the accelerometer and sent them on button press

- **Week 3:**
    - Worked on investigation:
        - Added the source for my formula to calculate calories lost to my investigation
        - Added anything relating weight and calories lost to write-up
        - Wrote up draft of 'what-if' questions
    - Added to plan and design:
        - Added a system summary, which sumamrises what my project and each program involved does
    - Made some changes to serial reader code, such as automatic port finding and many bug fixes 

- **Week 4:**
    - Made changes to serial reader;
        - Changed format of database to not include a primary key as it is unnecesarry for this program
    - Made the layout of the HTML document
    - Created config for ChartJS, in preperation for graphing
    - Made small wording changes to flowchart

- **Week 5:**
    - I took a break in preperation for my mock exams next week

- **Week 6:**
    - I had my mock exams this week

- **Week 7:**
    - Added venv, which stores all required modules locally, this is removed later due to issues that took too long to solve
    - Fixed up HTML layout
    - Added to serial reader
        - Implemented data validation, the data won't upload if it's not a number or if it's 0
    - Fixed microbit step counter code
        - Fixed issue where microbit would count multiple steps in one movement

- **Week 8:**
    - Added some basic CSS styling to the page
    - Attempted to make venv work
    - Removed venv in favor of downloading the required modules through the batch script, this will work assuming the user has python installed and is running windows

- **Week 9:**
    - Fixed an error in my stride calculation
    - Made ChartJS update the graph dynamically when a value is inputted
    - Added a function to calculate calories lost using the user's height, weight and steps
    - Added a function to advise the user on their step count and how it compares to others their sex and age

- **Week 10:**
    - Added a user system, which takes a username from the batch file when ran and writes/reads to/from that user's table in the database
    - Modified HTML layout to fit all inputs on the top of the screen
    - Worked on CSS
        - Made the graph zoomed in and scrollable to account for the readability large datasets
        - Added color to make the graphs more readable for the user
        - Made the label of the graph appear even if the user isn't hovering over the bar itself
        - Made the empty graphs hidden until data is found in them 

- **Week 11:**
    - Finishing touches to the CSS, such as colors and margins
    - Added a function to uncheck the other checkbox when a checkbox is selected
    - Fixed up the formatting of some javascript functions
    - Added a background gradient
    - Changed some input placeholders to be more clear, aswell as some text
    - Reworked my age group function as I thought of a more efficient way to write it
    - Fixed a bug with calorie function that would return NaN
    - Reworded my 'what-if' questions to be more clear
    
- **Week 12:**
    - Recorded my video, I left this for last in case I made any changes and had to record it again
    - Finalised my write-up and my code

## One Encountered Problem


## Important piece of code
