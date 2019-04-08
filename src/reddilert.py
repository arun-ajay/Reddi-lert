#! /usr/bin/env python3

import praw
import time
import os
import config
from datetime import datetime as dt

import smtplib
import email
from email.mime.text import MIMEText
from tools import *

brands = open(os.path.join(os.path.split(os.path.dirname(__file__))[0],'names.txt')).read().splitlines()
#TODO: USE config json...


reddit = praw.Reddit(client_id= config.praw_id,
                    client_secret=config.praw_secret,
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
            alert(new_deals_list)
        time.sleep(60) #scan every minute
        current_time = get_time()
        time_diff = time_subtract(start_time,current_time)
        print("Time elapsed:",time_diff)
        if( time_diff >= 1):
            break

