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
source code for this project. So setting up the SQL db is as simple as:

    CREATE DATABASE eplApi;
    
You should also create a user named `flaskuser` with full permissions to this database.

    mysql -u root -p GRANT ALL PRIVILEGES ON eplApi.* TO 'flaskuser'@'localhost' IDENTIFIED BY 'password';

Now, you can import the tables into the database.

    mysql -u flaskuser -p eplApi < db/schema.sql
    
__NOTE:__ The database configuration and username/password for the database are all read in from a .env file. So, it will be
necessary to create a .env file with the following format for the rest of the code in this project to work.

    epl_db_user="flaskuser"
    epl_db_password=<password>
    epl_db_name="eplApi"

### Install Chromedriver and Selenium

Next, it is necessary to install [Chromedriver](http://chromedriver.chromium.org/downloads). Once you have downloaded 
 and saved the binary in `/usr/local/bin/` (if on MacOS), you will pass it into 
`get_player_page()` located in the `get_player_links` module in order to retrieve the list of EPL players

    
### Retrieve a list of players in the EPL

Now you will need to get the list of players in the EPL and store this list in the *Players* table. 


### Retrieve and store the statistics for each player

    
    


