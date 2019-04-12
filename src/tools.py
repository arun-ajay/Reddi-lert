
from datetime import datetime as dt
import smtplib
import email
from email.mime.text import MIMEText


def get_time():
    time_format = '%Y-%m-%d %H:%M:%S'
    return dt.now().strftime(time_format)

def time_subtract(start,now):
    time_format = '%Y-%m-%d %H:%M:%S'
    return (dt.strptime(now,time_format) - dt.strptime(start,time_format)).days

def key_word_check(key_list,title,title_storage):
    for key in key_list:
        if (key.lower() in title.lower()) and title not in title_storage:
            return True
    return False

def alert(item_list,config_data):
    smtp_server = "smtp.gmail.com:587"

    body = ""
    for title,url in item_list:
        body += title + "\n" + url +  "\n\n"

    
    title = 'My title'
    msg_content = '<h2>{title} > <font color="green">OK</font></h2>\n'.format(title=title)
    message = MIMEText(msg_content, 'html')
    message['From'] = config_data.sender()
    message['To'] = config_data.receiver()
    message['Subject'] = "New Deals" + str(get_time())

    msg_full = body

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(config_data.sender(), config_data.sender_password())
    server.sendmail(config_data.sender(),
                    [config_data.receiver(), config_data.receiver()],
                    msg_full)
    server.quit()


