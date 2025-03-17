import json
import crawler.pinnwand
import crawler.dummy

import datetime

def fetch_crawlers():
    # Now add here all the crawlers
    entries = []
    entries += crawler.pinnwand.get_feed_entries()
    # TODO
    # entries.append(crawler.instagram.get_feed_entries())

    # ...
    # sort entries according to their publication time
    entries.sort(key=lambda x: x["pubUnix"], reverse=True)

    # filter all entries that are older than 1 month
    entries = [entry for entry in entries if entry["pubUnix"] > datetime.datetime.now().timestamp() - 30*24*60*60]

    with open("feed.json", "w") as feed:
        json.dump(entries, feed, indent=4)

fetch_crawlers()