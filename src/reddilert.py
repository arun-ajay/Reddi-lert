#! /usr/bin/env python3

import praw
import time
import os
import config
from datetime import datetime as dt

import smtplib
import email
from email.mime.text import MIMEText

brands = open(os.path.join(os.path.split(os.path.dirname(__file__))[0],'names.txt')).read().splitlines()
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

def alert(item_list):


    fromaddr = config.sender
    toaddr = config.receiver
    smtp_user = config.sender
    smtp_password = config.emailpassword
    smtp_server = "smtp.gmail.com:587"

    body = ""

    for title,url in item_list:
        body = body + title + "\n" + url +  "\n\n"

    title = 'My title'
    msg_content = '<h2>{title} > <font color="green">OK</font></h2>\n'.format(title=title)
    message = MIMEText(msg_content, 'html')

    message['From'] = fromaddr
    message['To'] = toaddr
    message['Subject'] = 'New Deals' + get_time()

    msg_full = body

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(fromaddr,
                    [toaddr, toaddr],
                    msg_full)
    server.quit()
    



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
        time.sleep(5) #scan every minute
        current_time = get_time()
        time_diff = time_subtract(start_time,current_time)
        print("Time elapsed:",time_diff)
        if( time_diff > 30):
            break

