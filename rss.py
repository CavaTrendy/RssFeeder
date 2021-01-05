import feedparser
import json
from url_check import urls
import re

links = urls

#######CLASS METHOD TRY##################
# class RSSFeed:
#     def __init__(self, urls):
#         self.urls = urls
#         print("Analyzing " + self.urls)
#
#     def feed(self):
#         rss_feed = feedparser.parse(self.urls)
#         feed_entries = rss_feed.entries
#
#         feeds = {"header": [], "link": [], "date": []}
#         for entry in feed_entries:
#             feeds["header"].append(entry.title)
#             feeds["link"].append(entry.link)
#             try:
#                 feeds["date"].append(entry.published)
#             except KeyError:
#                 print("no pubDate")
#         return feeds
#
#
# topics_dict = {
#     "source": [],
#     "title": [],
#     "date": [],
#     "url": []
# }
# for link in links:
#     rss_feed = feedparser.parse(link).channel.title
#     topics_dict["source"].append(rss_feed)
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
# def feed():
#     for urls in links:
#         print("Analyzing " + urls)
#         rss_feed = feedparser.parse(urls)
#         feed_entries = rss_feed.entries
#         feeds_articles = []
#         sourcerex = re.match("https?://([A-Za-z_0-9.-]+).", urls)
#         source = sourcerex[0]
#
#         for entry in feed_entries:
#             header = entry.title
#             link = entry.link
#             try:
#                 date = entry.published
#             except KeyError:
#                 print("no pubDate")
#
#             feeds = {"source": source, "header": header, "link": link, "date": date}
#             feeds_articles.append(feeds)
#     return feeds_articles
#
#
# a = feed()

# print(a)
feeds = {"source": [], "title": [], "link": [], "date": []}
for urls in links:
    print("Analyzing " + urls)
    rss_ = feedparser.parse(urls)
    feed_channel = rss_.channel
    # feed_title = feed_channel.title
    rss_feed = feedparser.parse(urls)
    feed_entries = rss_feed.entries
    i =0
    while i <= len(feed_entries):

        try:
            feeds["source"].append(feed_channel.title)

        except KeyError:
            feeds["source"].append(urls)
        except AttributeError:
            feeds["source"].append(urls)
            print("boh" + urls)
        i +=1


    for entry in feed_entries:
        feeds["title"].append(entry.title)
        feeds["link"].append(entry.link)
        try:
            feeds["date"].append(entry.published)
        except KeyError:
            print("no pubDate")

print(type(feeds))
# a= json.dumps(feeds,indent= 4, separators=(", ", ": "), sort_keys=True)
new_data = [{"source": s, "title": t,  "link": l, "date": d,} for s, t, l, d in
            zip(feeds["source"], feeds["title"], feeds["link"], feeds["date"])]
with open("static/feeds.json", "w") as write_file:
    json.dump(new_data, write_file, indent=4)
    # separators=(", ", ": "), sort_keys=True)

