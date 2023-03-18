# Movie-Search-App
An application that can search the movies on IDMB and classifies the movies into various genres.


SEARCH ENGINE (WEB SCRAPING) 
MVP
PROBLEM STATEMENT: Develop an application that can search the movies on IDMB and classifies the movies into various genres.
 
PROBLEM SPECIFICATION: The application should show a pie chart of the genre classification.

TEAM: Paul Ogbonna {github: AcerNg548}
 
ANALYSIS
Requirements (to be installed): tkinter, os, openpyxl, pandas, numpy, json, PyMovieDb, matplotlib
 
Installation Specification: Windows
 
 
Input: Input the name of the movie to search for
 
Process: Using the function declaration named “search”, once the button is clicked a variable filepath is created in the operating system (os) called “searchdata.xlsx” if it doesn’t exist, then a heading and the genre of the movie is being append to the excel sheet called “searchdata.xlsx” from the search results gotten in the MovieDBb Api
 
Output: With the help of “openpyxl module” it saves the excel sheet so it can be open and also the statistics of each genre in the console and draw the pie chart
