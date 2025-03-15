import feedparser
from pprint import pprint
import time

rss_feed_url = "https://www.uni-weimar.de/de/universitaet/aktuell/pinnwaende/rss/bereich/stuko/"

def get_feed_entries():
    print("Fetching RSS Feed from " + rss_feed_url)

    rss_feed = feedparser.parse(rss_feed_url)
    entries = []

    # Auf 10 Einträge beschränken
    if len(rss_feed.entries) > 10:
        rss_feed.entries = rss_feed.entries[:10]

    for rss_entry in rss_feed.entries:
        title = "".join(rss_entry["title"].split(": ")[1:])
        author = rss_entry["title"].split(": ")[0]
        entry = {
            # This is the type of the feed, e.g pinnwannd, instagram etc.
            "type": "StuKo Pinnwand",
            # This is the publication date and time
            "pubDate" : rss_entry["published"],
            # This is the publication date and time in unix time (was a bit lazy in this example)
            "pubUnix" : time.mktime(rss_entry["published_parsed"]),
            # This is the title of the feed element
            "title": title,
            "author": author,
            # This is the link to the original resource
            "link": rss_entry["link"],
            # This is a short summary of the content
            "summary": rss_entry["summary"],
            # This is the content
            "content" : rss_entry["content"][0]["value"],
            # Encoding of the content
            "content_encoding" : "html",
            # Tags (could be parsed out of hashtags or something else)
            "tags" : [tag["term"] for tag in rss_entry["tags"]],
            # link to a web image that should be displayed
            "image" : None
        }

        for link in rss_entry["links"]:
            if "image" in link["type"]:
                entry["image"] = link["href"]
                break
       
        entries.append(entry)

    return entries
