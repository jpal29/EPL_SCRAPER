from bs4 import BeautifulSoup, SoupStrainer
import re
import mysql.connector
import os
from dotenv import load_dotenv
import time
from selenium import webdriver


#Loading environment variables
load_dotenv()
load_dotenv(dotenv_path='../.env')

def get_player_page():
    """
    Will retrieve the list of players from from 'https://www.premierleague.com/players/
    :return:
    """
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


def save_player_links(html):
    """
    Will parse the player_links html page saved by get_players_page and write out the player links to
    the players table in the eplApi db.
    :return:
    """

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
                    print(stats_link)
                    mycursor.execute(sql, (stats_link,))
                    active_db.commit()
                    print(stats_link)


if __name__ == "__main__":
    links_page = get_player_page()
    #save_player_links(links_page)
    print(links_page)