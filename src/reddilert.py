#! /usr/bin/env python3

import praw
import time
import os
import config
from datetime import datetime as dt

#brands = open("names.txt").read().splitlines()

'''
current_dir = os.path.dirname(__file__)
parent_dir = os.path.split(current_dir)[0]
file_path = os.path.join(parent_dir,'TestLists/','names.txt')
brands = open(file_path)
'''

brands = open(os.path.join(os.path.split(os.path.dirname(__file__))[0],'TestLists/','names.txt')).read().splitlines()
#TODO: USE config json...


reddit = praw.Reddit(client_id= config.praw_id,
                    client_secret=config.praw_secret,
                    user_agent='my user agent')




def get_time():
    time_format = '%Y-%m-%d %H:%M:%S'
    return dt.now().strftime(time_format)
    
def time_subtract(start,now):
    time_format = '%Y-%m-%d %H:%M:%S'
    return (dt.strptime(now,time_format) - dt.strptime(start,time_format)).seconds

def key_word_check(key_list,title,title_storage):
    for key in key_list:
        if (key.lower() in title.lower()) and title not in title_storage:
            return True
    return False


while True:
    daily_list = []
    start_time = get_time()
    print(start_time)
    while True:
        for submission in reddit.subreddit('frugalmalefashion').new(limit=10):
            subtitle = submission.title
            suburl = submission.url
            if(key_word_check(brands,subtitle,daily_list)):
                    print(subtitle,"\n",suburl,"\n")
                    daily_list.append(subtitle)
        time.sleep(5) #scan every minute
        current_time = get_time()
        time_diff = time_subtract(start_time,current_time)
        if( time_diff > 30):
            print("RESETTING LIST")
            break
        print(time_diff," seconds have passed")

