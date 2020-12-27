import feedparser
import json

added_urls = ["http://www.reddit.com/r/learnphyton+Python+learnprogramming+programming+swift",
              "https://www.china-files.com/feed/", "https://agfundernews.com/feed", "https://www.coindesk.com/feed"]
links = []
# http://www.reddit.com/r/``{SUBREDDIT_NAME}``/new/.rss?sort=new
for urls in added_urls:
    if urls.startswith('http://www.reddit.com/'):
        user = input("[N]ew or [H]ot: ")
        if user == 'n':
            new = urls + '/new/.rss?sort=new'
            print(new)
            links.append(new)
        elif user == 'h':
            hot = urls + '/hot/.rss?sort=hot'
            print(hot)
            links.append(hot)
    else:
        links.append(urls)

print(links)


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

new_data = [{"title": i, "url": b} for i, b in zip(topics_dict["title"], topics_dict["url"])]
files = json.dumps(new_data, indent=3)
print(files)
