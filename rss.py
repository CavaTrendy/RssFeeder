import feedparser
import pandas as pd

links = ["http://www.reddit.com/r/learnphyton+Python+learnprogramming+programming+swift.rss",
         "https://www.china-files.com/feed/", "https://agfundernews.com/feed", "https://www.coindesk.com/feed"]


class RSSFeed:
    def __init__(self, link):
        self.link = link
        print("Analyzing " + self.link)

    def feed(self):
        rss_feed = feedparser.parse(self.link)
        feed_entries = rss_feed.entries
        feeds = {"header": [], "link": []}
        for entry in feed_entries:
            feeds["header"].append(entry.title)
            feeds["link"].append(entry.link)
        return feeds


topics_dict = {"title": [],
               "url": []}
for link in links:
    # print(RSSFeed(link).feed())
    for values in RSSFeed(link).feed().values():
        for keys in values:
            if "htt" in keys:
                topics_dict["url"].append(keys)
            else:
                topics_dict["title"].append(keys)

topics = pd.DataFrame(topics_dict)
print(topics)
topics.to_csv('Reddit.csv', index=False)
# file = [
#     {
#         "source": "reddit",
#         "feeds": [
#             {
#                 "title": "avffa",
#                 "url": "www.ciao.it"},
#             {
#                 "title": "gfafa",
#                 "url": "www.fafa.it"},
#         ]
#     },
#     {
#         "source": "twitter",
#         "feeds": [
#             {
#                 "title": "avffa",
#                 "url": "www.ciao.it"},
#             {
#                 "title": "gfafa",
#                 "url": "www.fafa.it"},
#         ]
#     }
# ]
