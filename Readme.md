How to Use EPL Scraper

This is a webscraper I created to crawl the website of the
[English Premier League](https://www.premierleague.com) (EPL) 
to retrieve player statistics for future analysis.

Several steps are required to implement this. From a high level, it is 
necessary to

* [Create the Database](#create-the-database)
* [Install Chromedriver and Selenium](#install-chromedriver-and-selenium)
* [Retrieve a list of players in the EPL](#retrieve-a-list-of-players-in-the-epl)
* [Retrieve and store the statistics for each player](#retrieve-and-store-the-statistics-for-each-player)


### Create the Database

For the purpose of storing the data that I scraped from the EPL 
site I decided to use a MySQL database. To save time, I've included the schema.sql file in the
source code for this project. This [SO post](https://stackoverflow.com/questions/10769344/create-mysql-database-with-sql-file) 
should provide guidance on how to create the database using the .sql file. The rest of this project
code is written under the assumption that the database is named `eplApi` so you should either
name your database the same, or update the source code to reflect your preferred database name. In this project that 
should be done in the get_player_links module and the save_player_info

### Install Chromedriver and Selenium

There are a few pre-requisites needed in order to scrape the EPL website for player
statistics. The first being that you will need to have [Chromedriver](http://chromedriver.chromium.org/downloads) 
installed. Once you have downloaded it, you will need to eventually pass it into the 
```save_player_page``` function in the ```get_player_links``` module

    
### Retrieve a list of players in the EPL

Now you will need to get the list of players in the EPL and store this list in the *Players* table. 


### Retrieve and store the statistics for each player

    
    


