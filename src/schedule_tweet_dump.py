# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 18:30:58 2016

@author: Anitha
"""

import os
import sys
import logging
from datetime import datetime

import pandas as pd
import requests
from apscheduler.schedulers.background import BackgroundScheduler


def tweet_dump_func():

    print("Dumping tweets : %s " % datetime.now())
    
    from TwitterAPI import TwitterAPI
    
    SEARCH_TERM = ['game of thrones','gameofthrones','gameof thrones','game ofthrones']
    tweet_file = 'tweet_dumped.txt'
    tweet_df = pd.DataFrame()
    #Twitter API credentials
    consumer_key = "Yc7WqmyJ2mcoNoT6pHumO06oy"
    consumer_secret = "45a4VNcbXjl7O2y3YLT7jSzqcMpl9I6K3Z0ILXJZkNsjNQUJWg"
    access_key = "746236373418418176-nt41zwawfRNIBTqSQvxfxmSSx8QTgXn"
    access_secret = "lbIHt5dLYqIKeHQgQ9yzGsQt6javsDSIbIbUObXmtg5Zu"
    
    
    
    api = TwitterAPI(consumer_key,
                     consumer_secret,
                     access_key,
                     access_secret,
                     #proxy_url="http://bc-cls03.ccla.com.au:3128"
                     )
    
    
    
    # Write out the scraped tweets
    
    with open(tweet_file, 'a', encoding='utf8') as tweet_out:
    
        iterator = api.request( 'search/tweets', {'q':SEARCH_TERM, 'lang':'en', 'tweet_mode':'extended', 'count':100})

        for item in iterator:
            if 'full_text' in item:
                print (item['created_at'], item['user']['screen_name'], item['full_text'],file=tweet_out)
            elif 'message' in item:
                #something needs to be fixed before re-connecting
                raise (Exception(item['message']))

    

if __name__ == '__main__':
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(tweet_dump_func, 'interval', seconds=1200)
    # scheduler.start()
    # print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    #
    #
    # try:
    #     # This is here to simulate application activity (which keeps the main thread alive).
    #     while True:
    #         time.sleep(2)
    # except (KeyboardInterrupt, SystemExit):
    #     # Not strictly necessary if daemonic mode is enabled but should be done if possible
    #     scheduler.shutdown()

    tweet_dump_func()