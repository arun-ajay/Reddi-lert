#! /usr/bin/env python3

import praw
import time
import config
from datetime import datetime

brands = open("names.txt").read().splitlines()


reddit = praw.Reddit(client_id= config.praw_id,
                    client_secret=config.praw_secret,
                    user_agent='my user agent')

time_format = '%Y-%m-%d %H:%M:%S'

#def time_subtract(time1,time2):


while True:
    daily_list = []
    start_time = datetime.now().strftime(time_format)
    print(start_time)
    while True:
        for submission in reddit.subreddit('frugalmalefashion').new(limit=10):
            title = (submission.title)
            url = submission.url
            for name in brands:
                if (name.lower() in title.lower()) and title not in daily_list:
                    print(title,"\n",url,"\n")
                    daily_list.append(title)
        time.sleep(5) #scan every minute
        currenttime = datetime.now().strftime(time_format)
        delta = datetime.strptime(currenttime,time_format) - datetime.strptime(start_time,time_format)
        print(delta)
        print("not found!")

