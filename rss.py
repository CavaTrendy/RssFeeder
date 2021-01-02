import feedparser
import json
from added_urls import added_urls
import re

links = added_urls

#######CLASS METHOD TRY##################
# class RSSFeed:
#     def __init__(self, urls):
#         self.urls = urls
#         print("Analyzing " + self.urls)
#
#     def feed(self):
#         rss_feed = feedparser.parse(self.urls)
#         feed_entries = rss_feed.entries
#         feeds = {"header": [], "link": [], "date": []}
#         for entry in feed_entries:
#             feeds["header"].append(entry.title)
#             feeds["link"].append(entry.link)
#             try:
#                 feeds["date"].append(entry.published)
#             except KeyError:
#                 print("no pubDate")
#         return feeds
# topics_dict = {"title": [],
#                # "summary": [],
#                "date": [],
#                "url": []
#                }
# for link in links:
#     for values in RSSFeed(link).feed().values():
#         # print(values)
#         for keys in values:
#             # print(keys)
#             if "htt" in keys:
#                 topics_dict["url"].append(keys)
#             elif len(keys) == 31 and 21:
#                 topics_dict["date"].append(keys)
#             else:
#                 topics_dict["title"].append(keys)

#########DEF METHOD ##########
def feed():
    for urls in links:
        print("Analyzing " + urls)
        rss_feed = feedparser.parse(urls)
        feed_entries = rss_feed.entries
        fedds_articles = []
        sourcerex = re.match("https?://([A-Za-z_0-9.-]+).", urls)
        source  = sourcerex[0]

        for entry in feed_entries:
            header = entry.title
            link = entry.link
            try:
                date= entry.published
            except KeyError:
                print("no pubDate")

            feeds = {"source" : source, "header": header,  "link": link, "date": date}
            fedds_articles.append(feeds)
    return fedds_articles

a = feed()

# print(a)
# new_data = [{"title": t, "date": u, "url": i} for t, u, i in
#             zip(topics_dict["title"], topics_dict["date"], topics_dict["url"])]
with open("feeds.json", "w") as write_file:
    json.dump(a, write_file, indent=3, separators=(", ", ": "), sort_keys=True)

