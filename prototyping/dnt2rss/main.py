import requests
from bs4 import BeautifulSoup
import datetime
import pytz

link = "https://www.nationaltheater-weimar.de/de/spielplan.php?MONTH=replaceMonth&YEAR=replaceYear"


def retrieve_events_from_link(link):
    # get html
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")

    # get all events
    events = soup.find_all("div", {"class": "event-box"})

    # create dict for each event
    event_infos = []
    for event in events:
        info = {"date": "", "title": "", "time": "", "location": "", "link": "", "image": "", "description_short": ""}
        day = event.find("span", {"class": "day"}).text.strip()
        info["date"] = datetime.date(year, month, int(day))
        info["title"] = event.find("span", {"class": "headline"}).text.strip()
        info["description_short"] = event.find("span", {"class": "subline"}).text.strip()
        info["image"] = "https://www.nationaltheater-weimar.de" + event.find("img")["src"]

        # filter links by text inside, only get the one with "Infos"
        links = event.find_all("a")
        for link in links:
            if "Infos" in link.text.strip():
                info["link"] = "https://www.nationaltheater-weimar.de" + link["href"]

        # get duration and further information from infolink
        info["full_description"] = ""
        if info["link"]:
            r = requests.get(info["link"])
            msoup = BeautifulSoup(r.text, "html.parser")
            info["full_description"] = msoup.find("div", {"class": "text-col"}).text.strip()

        # get time and location
        multi_info = event.find("span", {"class": "info"})
        if multi_info:
            multi_info = multi_info.text.strip().split("\xa0//")
            info["time"] = multi_info[0].strip()
            info["location"] = multi_info[1].split(" // ")[0].strip()

        # parse time
        if info["time"]:
            dt_time = datetime.datetime.strptime(info["time"].replace(" Uhr", ""), "%H.%M")
            # user berlin timezon
            info["start"] = datetime.datetime.combine(info["date"], dt_time.time())
            info["start"] = pytz.timezone("Europe/Berlin").localize(info["start"])
            info["end"] = info["start"] + datetime.timedelta(hours=2)
        event_infos.append(info)

    return event_infos


# get current month and year
now = datetime.datetime.now()
month = now.month
year = now.year

request_link = link.replace("replaceMonth", str(month))
request_link = request_link.replace("replaceYear", str(year))

event_infos = retrieve_events_from_link(request_link)

if len(event_infos) < 5:
    month = month + 1
    if month > 12:
        month = 1
        year = year + 1
    
    request_link = link.replace("replaceMonth", str(month))
    request_link = request_link.replace("replaceYear", str(year))

    event_infos += retrieve_events_from_link(request_link)

# generate rss feed
from feedgen.feed import FeedGenerator

fg = FeedGenerator()
fg.id("https://www.nationaltheater-weimar.de/de/spielplan.php")
fg.title("Spielplan Nationaltheater Weimar")
fg.author({"name": "Nationaltheater Weimar", "email": ""})
fg.link(href="https://www.nationaltheater-weimar.de/de/spielplan.php", rel="alternate")
fg.logo("https://www.nationaltheater-weimar.de/images/dnt-logo.png")
fg.subtitle("Spielplan Nationaltheater Weimar")

for event in event_infos:
    fe = fg.add_entry()
    fe.id(event["link"])
    fe.title(event["title"])
    fe.link(href=event["link"])
    fe.description(event["full_description"])
    fe.published(event["start"])
    fe.updated(event["end"])
    fe.enclosure(event["image"], 0, "image/jpeg")

fg.rss_file("rss.xml")



