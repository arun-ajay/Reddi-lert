#! /usr/bin/env python3

#Public Libraries
import praw
import time
import os
import json


#Custom FIles
from tools import *


brands = open('names.txt').read().splitlines()


with open('config.json') as config_file:
    config_data = json.load(config_file)

praw_id = str(config_data["Reddit"]["praw_id"])
praw_secret = str(config_data["Reddit"]["praw_secret"])




reddit = praw.Reddit(client_id= praw_id,
                    client_secret=praw_secret,
                    user_agent='my user agent')



while True:
    old_deals_list = []
    start_time = get_time()
    while True:
        new_deals_list = []
        for submission in reddit.subreddit('frugalmalefashion').new(limit=10):
            subtitle = submission.title
            suburl = submission.url
            if(key_word_check(brands,subtitle,old_deals_list)):
                    new_deals_list.append((subtitle,suburl))
                    old_deals_list.append(subtitle)
        if new_deals_list:
            print("Emailing New Deals!")
            alert(new_deals_list,config_data)
        time.sleep(60) #scan every minute
        current_time = get_time()
        time_diff = time_subtract(start_time,current_time)
        print("Time elapsed:",time_diff)
        if( time_diff >= 1):
            break

