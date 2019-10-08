# reddilert.py

I wrote this script as a means of immediately notifying me when content of a particular subreddit appears.

I've found my most convenient usage in deal subreddits such as r/frugalmalefashion. 

## Setup

- Clone(or download this repo)
- Optional: Create your own virtual environment in the Reddi-lert folder
  - Run `python3 -m venv env`
  - Activate your env by running: `source env/bin/activate`
- While in the Reddi-lert folder install the necessary packages by running: `pip install -r requirements.txt` 
- Go into the `Reddi-lert/src` folder
- Open your `config_template.json` file and fill in the following parameters:
  - praw_id
  - praw_secret
  - sender
  - sender_password
  - receiver
- Create a `names.txt` file within `Reddi-lert/src` and put whatever keywords you wanted detected. For example:
  - Nike
  - Banana
  - Macy
- Run `reddilert.py`

I've personally run this script on my Raspberry Pi 3 on a 24/7 basis and it's been a huge help in ensuring I don't miss out on the brands I care about the most

## Future Plans

Here's what I have in mind
  - Simple Gui to manage keywords
  - Allow for multiple subreddit scanning
  
As always, I'm open to more ideas! :)
