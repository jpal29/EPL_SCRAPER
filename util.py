import pprint
import os
from selenium import webdriver
from bs4 import BeautifulSoup
import mysql.connector
from dotenv import load_dotenv
import time
import requests

#Loading environment variables
load_dotenv()
load_dotenv(dotenv_path='./.env')


url = "https://www.premierleague.com/players/"

def how_to_scroll():

    options = webdriver.ChromeOptions()
    options.binary_location = '/Users/Josh/Downloads/chromedriver'
    options.add_argument('window-size=800x841')
    options.add_argument('headless')

    driver = webdriver.Chrome('/Users/Josh/Downloads/chromedriver')
    driver.get('https://www.premierleague.com/players/')
    driver.maximize_window()


    driver.get('https://www.premierleague.com/players/')

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #Need to allow the browser adequate time to load the page
    time.sleep(120)
    html = driver.page_source

    player_file = open('player_page.html', 'w')
    player_file.write(html)
    player_file.close()

    soup = BeautifulSoup(html, features="lxml")

    for tag in soup.find_all('tr'):
        print(tag.text)


def get_player_name():
    player_page = BeautifulSoup(open("/Users/Josh/development/EPL_API/pl_html_files/sample_forward_page.html"), features="lxml")
    player_name = player_page.find("div", {"class": "name"})
    print(player_name.text)

def get_player_id():
    print(os.getenv('epl_db_user'))
    active_db = mysql.connector.connect(
        host="localhost",
        user=os.getenv('epl_db_user'),
        passwd=os.getenv('epl_db_password'),
        database=os.getenv('epl_db_name')
    )

    db_cursor = active_db.cursor()

    db_cursor.execute("SELECT * from Players")
    for row in db_cursor:
        pprint.pprint(row)


def get_player_info():
    url = "https://www.premierleague.com/players/"
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')
    player_table = soup.find('tbody')

    players = []

    for table_row in player_table.find_all('tr'):
        player = {}
        for index, cells in enumerate(table_row.find_all('td')):
            if cells.find('a'):
                player_link_tag = cells.find('a')
                player['Link'] = player_link_tag.get('href')
                player['Name'] = player_link_tag.text.strip()

            if index == 1:
                player['Position'] = cells.text.strip()
        players.append(player)
    print(len(players))
    keys = players[0].keys()
    with open('player_list.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(players)

#get_player_id()
how_to_scroll()

