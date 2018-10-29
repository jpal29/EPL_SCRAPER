## Web Scraper

This is a webscraper I created to crawl the website of the
[English Premier League](https://www.premierleague.com) (EPL) 
to retrieve and save player statistics for future analysis.

Several steps are required to implement this. From a high level, it is 
necessary to

* [Create the Database](#create-the-database)
* [Use Chromedriver and Selenium to retrieve list of players](#use-chromedriver-and-selenium-to-retrieve-list-of-players)
* [Save player list to local database](#save-player-list-to-local-database)
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

### Use Chromedriver and Selenium to retrieve list of players

Next, it is necessary to install [Chromedriver](http://chromedriver.chromium.org/downloads). Once you have downloaded 
 and saved the binary in `/usr/local/bin/` (if on MacOS), you will pass it into 
`get_player_page()` located in the `get_player_links` module in order to retrieve the list of EPL players.

    def get_player_page():
    
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/local/bin/chromedriver'
        options.add_argument('window-size=800x841')
        options.add_argument('headless')
    
        driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        driver.get('https://www.premierleague.com/players/')
        driver.maximize_window()
    
        driver.get('https://www.premierleague.com/players/')
    
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        # Need to allow the browser adequate time to load the page
        time.sleep(120)
        html = driver.page_source
    
        return html

    
### Save player list to local database

Now that you have the means by which to get the list of players in the EPL, 
it is now necessary to store this list in the *Players* table that you created
when you imported the schema.sql file. This can be accomplished by taking the html
returned from `get_player_page()` and passing it into `save_player_links()`

    def save_player_links(html):
        soup = BeautifulSoup(html, "html.parser", parse_only=SoupStrainer('a'))
        active_db = mysql.connector.connect(
            host="localhost",
            user=os.getenv('epl_db_user'),
            passwd=os.getenv('epl_db_password'),
            database=os.getenv('epl_db_name')
        )
    
        mycursor = active_db.cursor()
        active_db.commit()
        p = re.compile('https://www.premierleague.com/players/[0-9]*')
        for link in soup:
            if link.has_attr('href'):
                if p.match(link['href']):
                    sql = "INSERT INTO Players (player_link) VALUES (%s)"
                    temp_link = link['href']
                    if temp_link.endswith("overview"):
                        temp_link = temp_link[:-8]
                        stats_link = temp_link + 'stats'
                        mycursor.execute(sql, (stats_link,))
                        active_db.commit()


### Retrieve and store the statistics for each player

With all of the EPL players and the links to their individual statistics page, retrieving
and saving the statistics for each player is made easy through the use of the PlayerCrawler
defined in the `save_player_info` module.

    from save_player_info import PlayerCrawler
    
    crawler = PlayerCrawler()
    crawler.crawl_player_links()
    


    
    


