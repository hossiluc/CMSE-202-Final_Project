library(rvest)
library(dplyr)
# data scraped from currentresults.com
web_address<-"https://www.currentresults.com/Weather/US/annual-average-humidity-by-state.php"
# Read the html code of the webpage in to the variable webpage_code
webpage_code<-read_html(web_address)

# Read the webpage using the CSS path identified
climate_data <- html_nodes(webpage_code,'td:nth-child(4)')

# Convert the new headlines to text
climate_data_text7 <- html_text(climate_data)

# Create a dataframe to append all other climate data to
state_climate <- data.frame(climate_data_text)

# Append a new column to the state_climate dataframe
state_climate$Aftnoon_Humid = climate_data_text7
state_climate
#export the finished dataframe as a .csv file
write.csv(state_climate, file = "State_ClimateData.csv")