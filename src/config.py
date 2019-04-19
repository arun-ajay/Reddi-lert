import json


class Config():
    
    def __init__(self):
        print("Loading config..")
        with open('config.json') as config_file:
            self.config_data = json.load(config_file)
    
    def praw_id(self):
        return str(self.config_data["Reddit"]["praw_id"])
    
    def praw_secret(self):
        return str(self.config_data["Reddit"]["praw_secret"])
    
    def sender(self):
        return str(self.config_data["Emails"]["sender"])
    
    def sender_password(self):
        return str(self.config_data["Emails"]["sender_password"])
    
    def receiver(self):
        return self.config_data["Emails"]["receiver"]
        #return str(self.config_data["Emails"]["receiver"])


