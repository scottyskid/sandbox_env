import os
import sys
import time
import json

import pandas as pd
import requests
from bs4 import BeautifulSoup
from pprint import pprint


if __name__ == "__main__":
    #### 2007 T20 Cricket World Cup ####

    ### HTML Scrape ###

    url_wc_final = "http://www.espncricinfo.com/india/content/player/28081.html"

    session = requests.Session()

    # Proxies are required inside the Clemenger Network
    proxies = {
        'http': "http://bc-cls03.ccla.com.au:3128",
        'https': "http://bc-cls03.ccla.com.au:3128",
    }
    session.proxies = proxies

    # the the url stated above
    # html_response = session.get(url_wc_final)
    # html_string = html_response.text
    html_string = session.get(url_wc_final).text
    ### Using Beautiful Soup ###

    soup = BeautifulSoup(html_string, 'lxml')

    # Find all tables
    stats = soup.find_all('table', {'class': 'engineTable'})


    # convert the tables to a data frame (table)
    stats_df = pd.read_html(str(stats))

    # print them to a csv
    stats_df[0].to_csv('batting_stats.csv')
    stats_df[1].to_csv('bowling_stats.csv')

    ### API/JSON Scraping ###

    # http://www.espncricinfo.com/series/8604/scorecard/287879/india-vs-pakistan-final-icc-world-twenty20-2007-08
    url_wc_final_json = "http://site.web.api.espn.com/apis/site/v2/sports/cricket/8604/summary?contentorigin=espn&event=287879&lang=en&region=au&section=cricinfo"

    scorecard_response = session.get(url_wc_final_json)
    scorecard_json = scorecard_response.text

    scorecard_dict = json.loads(scorecard_json)

    # find the info that we need
    matchcards = scorecard_dict['matchcards']


    card_list = []
    for card in matchcards:
        card_list += card['playerDetails']

    matchcard_df = pd.DataFrame(card_list)

    matchcard_df.to_csv('matchcard.csv')
