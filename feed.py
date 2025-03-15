import json
import crawler.pinnwand
import crawler.dummy

def fetch_crawlers():
    # Now add here all the crawlers
    entries = []
    entries += crawler.pinnwand.get_feed_entries()
    # TODO
    # entries.append(crawler.instagram.get_feed_entries())

    # ...
    # sort entries according to their publication time
    entries.sort(key=lambda x: x["pubUnix"], reverse=True)

    with open("feed.json", "w") as feed:
        json.dump(entries, feed, indent=4)

fetch_crawlers()