On this Project we explored different concepts of data manipulation and visualization with regards to the climate of the US.

Before we begin, please note that the 'MasterNotebook_Model' file is the most current file for our model. Run that one.

The following will detail instructions for running our code:

  1. The first part contains the pip installs of some of the more uncommon modules that you'll need to make this work, the imports for all of our data, and the masks you'll need to make parts 2 and 3 work. Make sure you run all of the cells in part 1!

  2. Part 2 contains all of the cells used for the folium mapping and widget display. The first three cells deal with the coding for the fourth, so the fourth is optional. 

  Note that the fourth cell will display both a color map and clickable markers- when changing datasets using the widget, please be sure to run both the cell above the widget and the one below the widget. Otherwise, you will only get the new colormap displayed, without the markers.

  3. Part 3, while cool, is completely optional. It is a user interface aimed at determining what state(s) would be the best for the user to live in, according to their own personal preferences. 

  It will intake user input, so please be sure to follow the directions in the notebook for what input will send you where! Otherwise, you may find yourself trapped in a polite, but infinite, loop of questioning.

Please refer to the Jupyter Notebook in the repository for further details and code comments.



For the visualization of this project:

  - We used folium to get our data visualized in maps

  - pandas for data manipulation
  


We got data from the following websites:

  -currentresults.com

  -noaa.gov
  
  

The workload for this project was split as follows:

Deontae: Worked on the User-input "Choose your own adventure" functionality (part 3).
Lucas: Fixed all labeling issues with folium plot, and helped with web-scraping.
Maegan: Added in initial labels, cleaned up MasterNotebook, compiled the group code, and put together powerpoint.
Hunter: Web-scraped the data for our project using selector gadget, and begun a web server to visualize our plot.
Noah: Added in base code and ground work for the project, including implementation of the folium plot with the widget, and the color-maping.
