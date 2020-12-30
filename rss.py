import feedparser
import json
from added_urls import added_urls

links = added_urls


class RSSFeed:
    def __init__(self, urls):
        self.urls = urls
        print("Analyzing " + self.urls)

    def feed(self):
        rss_feed = feedparser.parse(self.urls)
        feed_entries = rss_feed.entries
        feeds = {"header": [], "link": [], "date": []}
        for entry in feed_entries:
            feeds["header"].append(entry.title)
            feeds["link"].append(entry.link)
            try:
                feeds["date"].append(entry.published)
            except:
                print("no pubDate")
        return feeds


topics_dict = {"title": [],
               # "summary": [],
               "date": [],
               "url": []
               }
for link in links:
    for values in RSSFeed(link).feed().values():
        # print(values)
        for keys in values:
            # print(keys)
            if "htt" in keys:
                topics_dict["url"].append(keys)
            elif len(keys) == 31:
                topics_dict["date"].append(keys)
            else:
                topics_dict["title"].append(keys)

new_data = [{"title": t, "date": u, "url": i} for t, u, i in
            zip(topics_dict["title"], topics_dict["date"], topics_dict["url"])]
# files = json.dump(new_data, indent=3)
# print(files)
