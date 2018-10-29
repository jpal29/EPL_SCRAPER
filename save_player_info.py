import pprint
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import mysql.connector
import re
import requests
from dotenv import load_dotenv
from pathlib import Path
import time

#Loading environment variables
load_dotenv()
load_dotenv(dotenv_path='../.env')



class PlayerCrawler():
    def __init__(self):
        self.active_db = mysql.connector.connect(
            host="localhost",
            user=os.getenv('epl_db_user'),
            passwd=os.getenv('epl_db_password'),
            database=os.getenv('epl_db_name')
        )

        self.db_cursor = self.active_db.cursor(buffered=True)

    def crawl_player_links(self):
        print('Beginning to crawl links')
        print('Retrieving records from player table')
        print('--------------------------------------')
        print('--------------------------------------')
        self.db_cursor.execute("SELECT * from Players")
        print('Retrieved values, now crawling')
        players = self.db_cursor.fetchall()
        for row in players:
            print(row)
            print('retrieving player {}'.format(row[0]))
            time.sleep(5)
            player_page = self.get_player_page(row[3])
            self.save_player_stats(player_page, row[0])
        print('Finished retrieving all players and saving their stats, going to bed now')
        return



    def get_player_page(self, link):
        """
        Loads the player stats page and prepares it to be parsed for
        the stats pertinent to that player's position.

        :param link: link to the individual player stats page
        :type link: str
        :return: html page that has been loaded into Beautful Soup class
        :rtype: bs4.BeautifulSoup
        """
        r = requests.get(link)
        player_page = BeautifulSoup(r.text, features="lxml")
        return player_page

    def save_player_stats(self, player_page, player_id):
        """
        Parses the player stats page for the pertinent stats based on their position and then saves
        those stats to the corresponding table in database

        :param player_page: html page that has been loaded into Beautiful Soup class
        :type player_page: bs4.BeautifulSoup
        :param player_id: id of the player from player's table in db
        :type player_id: int
        :return: the position of that player
        :rtype: str
        """
        positions = {"Goalkeeper", "Midfielder", "Forward", "Defender"}
        global player_position
        global filtered_stats
        global write_query
        for position in positions:
            results = player_page.find_all(string=re.compile('.*{0}.*'.format(position)), recursive=True)
            try:
                player_position = results[0]
            except:
                pass
        print('Found player position {} {}, retrieving their relevant stats'.format(player_position, player_id))
        if player_position == "Forward":

            player_stats = player_page.find_all("span", {"class": "stat"})
            relevant_stats = [
                "Appearances",
                "Goals",
                "Goals per match",
                "Shots",
                "Shots on target",
                "Assists",
                "Passes",
                "Passes per match",
                "Crosses"
            ]

            #Will use this to make writing to the db easier
            filtered_stats = {}
            player_name = player_page.find("div", {"class": "name"})
            filtered_stats["Name"] = player_name.text
            filtered_stats["Position"] = "Forward"
            filtered_stats["player_id_for"] = player_id
            for stat_sec in player_stats:
                stat = str(stat_sec.contents[0]).strip()
                print(stat)
                if stat in relevant_stats:
                    print(stat)
                    child = stat_sec.findChildren("span")
                    if len(child) == 1:
                        filtered_stats[stat] = child[0].text.strip()
            #Want to make sure that all relevant stats have been mapped over to filtered stats
            for stat in relevant_stats:
                if stat not in filtered_stats.keys():
                    filtered_stats[stat] = None

            self.db_cursor.execute("INSERT INTO Forwards (name, appearances, goals, goals_per_match, " \
                          "shots, shots_on_target, assists, passes, passes_per_match, crosses, " \
                          "player_id_for, position) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                filtered_stats["Name"],
                filtered_stats["Appearances"],
                filtered_stats["Goals"],
                filtered_stats["Goals per match"],
                filtered_stats["Shots"],
                filtered_stats["Shots on target"],
                filtered_stats["Assists"],
                filtered_stats["Passes"],
                filtered_stats["Passes per match"],
                filtered_stats["Crosses"],
                filtered_stats["player_id_for"],
                filtered_stats["Position"]
            ))
            self.active_db.commit()


        elif player_position == "Midfielder":

            player_stats = player_page.find_all("span", {"class": "stat"})
            relevant_stats = [
                "Goals",
                "Shots",
                "Shots on target",
                "Assists",
                "Shooting accuracy %",
                "Passes",
                "Passes per match",
                "Crosses",
                "Big chances created",
                "Cross accuracy %",
                "Through balls",
                "Accurate long balls",
                "Tackles",
                "Tackle success %",
                "Blocked shots",
                "Interceptions",
                "Clearances",
                "Recoveries",
                "Duels won",
                "Duels lost",
                "Successful 50/50s",
                "Aerial battles won"
            ]

            #Will use this to make writing to the db easier
            filtered_stats = {}
            player_name = player_page.find("div", {"class": "name"})
            filtered_stats["Name"] = player_name.text
            filtered_stats["Position"] = "Midfielder"
            filtered_stats["player_id_mid"] = player_id
            print(player_name.text)
            for stat_sec in player_stats:
                stat = str(stat_sec.contents[0]).strip()
                if stat in relevant_stats:
                    child = stat_sec.findChildren("span")
                    if len(child) == 1:
                        if stat == "Shooting accuracy %":
                            stripped_data = child[0].text.strip()
                            filtered_stats[stat] = float(stripped_data.strip('%'))/100
                        elif stat == "Cross accuracy %":
                            stripped_data = child[0].text.strip()
                            filtered_stats[stat] = float(stripped_data.strip('%'))/100
                        elif stat == "Tackle success %":
                            stripped_data = child[0].text.strip()
                            filtered_stats[stat] = float(stripped_data.strip('%')) / 100
                        else:
                            filtered_stats[stat] = child[0].text.strip()
                    else:
                        print('This stat has nothing: {}'.format(stat))
            # Want to make sure that all relevant stats have been mapped over to filtered stats
            for stat in relevant_stats:
                if stat not in filtered_stats.keys():
                    filtered_stats[stat] = None

            self.db_cursor.execute("INSERT INTO Midfielders (name, goals, shots, shots_on_target, player_id_mid, shooting_accuracy, " \
                          "assists, passes, passes_per_match, big_chances_created, " \
                          "crosses, cross_accuracy, through_balls, accurate_long_balls, " \
                          "tackles, tackle_success, blocked_shots, interceptions, clearances, " \
                          "recoveries, duels_won, duels_lost, successful_50_50, aerial_battles_won" \
                          ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                filtered_stats["Name"],
                filtered_stats["Goals"],
                filtered_stats["Shots"],
                filtered_stats["Shots on target"],
                filtered_stats["player_id_mid"],
                filtered_stats["Shooting accuracy %"],
                filtered_stats["Assists"],
                filtered_stats["Passes"],
                filtered_stats["Passes per match"],
                filtered_stats["Big chances created"],
                filtered_stats["Crosses"],
                filtered_stats["Cross accuracy %"],
                filtered_stats["Through balls"],
                filtered_stats["Accurate long balls"],
                filtered_stats["Tackles"],
                filtered_stats["Tackle success %"],
                filtered_stats["Blocked shots"],
                filtered_stats["Interceptions"],
                filtered_stats["Clearances"],
                filtered_stats["Recoveries"],
                filtered_stats["Duels won"],
                filtered_stats["Duels lost"],
                filtered_stats["Successful 50/50s"],
                filtered_stats["Aerial battles won"],
            ))
            self.active_db.commit()


        elif player_position == "Defender":
            player_stats = player_page.find_all("span", {"class": "stat"})
            relevant_stats = [
                "Clean sheets",
                "Goals conceded",
                "Tackles",
                "Tackle success %",
                "Goals conceded",
                "Last man tackles",
                "Blocked shots",
                "Interceptions",
                "Clearances",
                "Recoveries",
                "Duels won",
                "Duels lost",
                "Successful 50/50s",
                "Own goals",
                "Errors leading to goal",
                "Assists",
                "Passes",
                "Passes per match",
                "Big chances created",
                "Crosses",
                "Cross accuracy %",
                "Through balls",
                "Accurate long balls",
                "Goals"
            ]

            # Will use this to make writing to the db easier
            filtered_stats = {}
            player_name = player_page.find("div", {"class": "name"})
            filtered_stats["Name"] = player_name.text
            filtered_stats["Position"] = "Defender"
            filtered_stats["player_id_def"] = player_id

            for stat_sec in player_stats:
                stat = str(stat_sec.contents[0]).strip()
                print(stat)
                if stat in relevant_stats:
                    print(stat)
                    child = stat_sec.findChildren("span")
                    if len(child) == 1:
                        if stat == "Tackle success %":
                            stripped_data = child[0].text.strip()
                            filtered_stats[stat] = float(stripped_data.strip('%'))/100
                        elif stat == "Cross accuracy %":
                            stripped_data = child[0].text.strip()
                            filtered_stats[stat] = float(stripped_data.strip('%'))/100
                        else:
                            filtered_stats[stat] = child[0].text.strip()

            for stat in relevant_stats:
                if stat not in filtered_stats.keys():
                    filtered_stats[stat] = None

            self.db_cursor.execute("INSERT INTO Defenders (name, clean_sheets, goals_conceded, " \
                                  "tackles, tackle_success, player_id_def, " \
                                  "last_man_tackles, blocked_shots, interceptions, " \
                                  "clearances, recoveries, duels_won, duels_lost, " \
                                  "successful_50_50, own_goals, err_leading_to_goal, " \
                                  "assists, passes, passes_per_match, " \
                                  "big_chances_created, crosses, cross_accuracy, " \
                                  "through_balls, accurate_long_balls, goals" \
                                  ") VALUES (%s, %s, %s, %s, %s, " \
                                  "%s, %s, %s, %s, %s, " \
                                  "%s, %s, %s, %s, %s, " \
                                  "%s, %s, %s, %s, %s, " \
                                  "%s, %s, %s, %s, %s)", (
                        filtered_stats["Name"],
                        filtered_stats["Clean sheets"],
                        filtered_stats["Goals conceded"],
                        filtered_stats["Tackles"],
                        filtered_stats["Tackle success %"],
                        filtered_stats["player_id_def"],
                        filtered_stats["Last man tackles"],
                        filtered_stats["Blocked shots"],
                        filtered_stats["Interceptions"],
                        filtered_stats["Clearances"],
                        filtered_stats["Recoveries"],
                        filtered_stats["Duels won"],
                        filtered_stats["Duels lost"],
                        filtered_stats["Successful 50/50s"],
                        filtered_stats["Own goals"],
                        filtered_stats["Errors leading to goal"],
                        filtered_stats["Assists"],
                        filtered_stats["Passes"],
                        filtered_stats["Passes per match"],
                        filtered_stats["Big chances created"],
                        filtered_stats["Crosses"],
                        filtered_stats["Cross accuracy %"],
                        filtered_stats["Through balls"],
                        filtered_stats["Accurate long balls"],
                        filtered_stats["Goals"]
                    ))
            self.active_db.commit()


        elif player_position == "Goalkeeper":
            player_stats = player_page.find_all("span", {"class": "stat"})
            relevant_stats = [
                "Saves",
                "Penalties saved",
                "Punches",
                "High Claims",
                "Catches",
                "Sweeper clearances",
                "Throw outs",
                "Goal Kicks",
                "Clean sheets",
                "Goals conceded",
                "Errors leading to goal",
                "Own goals",
                "Assists",
                "Passes",
                "Passes per match",
                "Accurate long balls"
            ]

            #This will make writing to the db easier
            filtered_stats = {}
            player_name = player_page.find("div", {"class": "name"})
            filtered_stats["Name"] = player_name.text
            filtered_stats["Position"] = "Goalkeeper"
            filtered_stats["player_id_goal"] = player_id

            for stat_sec in player_stats:
                stat = str(stat_sec.contents[0]).strip()
                print(stat)
                if stat in relevant_stats:
                    print(stat)
                    child = stat_sec.findChildren("span")
                    if len(child) == 1:
                        filtered_stats[stat] = child[0].text.strip()

            for stat in relevant_stats:
                if stat not in filtered_stats.keys():
                    filtered_stats[stat] = None

            self.db_cursor.execute("INSERT INTO Goalkeepers (name, saves, player_id_goal, " \
                                  "penalties_saved, punches, high_claims, " \
                                  "catches, sweeper_clearances, throw_outs, " \
                                  "goal_kicks, clean_sheets, goals_conceded, err_leading_to_goal, " \
                                  "own_goals, assists, passes, passes_per_match, " \
                                  "accurate_long_balls" \
                                  ") VALUES (%s, %s, %s, %s, %s, " \
                                  "%s, %s, %s, %s, %s, " \
                                  "%s, %s, %s, %s, %s, " \
                                  "%s, %s, %s)", (
                        filtered_stats["Name"],
                        filtered_stats["Saves"],
                        filtered_stats["player_id_goal"],
                        filtered_stats["Penalties saved"],
                        filtered_stats["Punches"],
                        filtered_stats["High Claims"],
                        filtered_stats["Catches"],
                        filtered_stats["Sweeper clearances"],
                        filtered_stats["Throw outs"],
                        filtered_stats["Goal Kicks"],
                        filtered_stats["Clean sheets"],
                        filtered_stats["Goals conceded"],
                        filtered_stats["Errors leading to goal"],
                        filtered_stats["Own goals"],
                        filtered_stats["Assists"],
                        filtered_stats["Passes"],
                        filtered_stats["Passes per match"],
                        filtered_stats["Accurate long balls"]
                    ))
            self.active_db.commit()


if __name__ == "__main__":
    #get_player_position(driver)
    crawler = PlayerCrawler()
    crawler.crawl_player_links()
    #soup = BeautifulSoup(open("/Users/Josh/development/EPL_API/pl_html_files/sample_goal_page.htm"), "html.parser")
    #player_crawler = PlayerCrawler()
    #player_crawler.get_player_position(soup, 3)



	        
        


        	
   
	


    




