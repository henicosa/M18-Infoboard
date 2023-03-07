import json
import crawler.dummy

def fetch_crawlers():
    # Now add here all the crawlers
    entries = crawler.dummy.get_feed_entries()
    # TODO
    # entries.append(crawler.instagram.get_feed_entries())
    # entries.append(crawler.pinnwand.get_feed_entries())
    # ...
    # sort entries according to their publication time

    with open("feed.json", "w") as feed:
        json.dump(entries, feed)

fetch_crawlers()