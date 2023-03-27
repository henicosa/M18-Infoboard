import os

# change the working directory to the directory that contains this
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

import schedule
import time

import applog
import feed


print("Started scheduling")
feed.fetch_crawlers()
    
schedule.every(2).hours.do(feed.fetch_crawlers)

while True:
    try:
        schedule.run_pending()
        time.sleep(60)
    except Exception as e:
        applog.error(e)
