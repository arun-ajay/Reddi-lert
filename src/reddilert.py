#! /usr/bin/env python3

#Public Libraries
import praw
import time
import os
import json


#Custom Files
from tools import *
from config import Config

brands = open('names.txt').read().splitlines()

information = Config()



praw_id = information.praw_id()
praw_secret = information.praw_secret()


reddit = praw.Reddit(client_id= praw_id,
                    client_secret=praw_secret,
                    user_agent='my user agent')



while True:
    old_deals_list = [] #Collection of titles that were already notifed
    start_time = get_time() #Baseline for time reset
    while True:
        new_deals_list = [] #Temporary list of new deals posted in past 30 secs
        for submission in reddit.subreddit('frugalmalefashion').new(limit=10):
            subtitle = submission.title
            suburl = submission.url
            if(key_word_check(brands,subtitle,old_deals_list)):
                    new_deals_list.append((subtitle,suburl))
                    old_deals_list.append(subtitle)
        if new_deals_list:
            print("Emailing New Deals!")
            alert(new_deals_list,information)
        time.sleep(60) #scan every minute
        current_time = get_time()
        time_diff = time_subtract(start_time,current_time)
        print("Time elapsed:",time_diff)
        if( time_diff >= 1):
            break

