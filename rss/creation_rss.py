from rss.models import Post
from rss.__int__ import db
import feedparser
import json
from rss.url_check import urls
import re
from dateutil import parser, tz

links = urls

feeds ={"source": [] , "title" : [], "description": [], "link": [], "date" : [] }

for urls in links:
    print("Analyzing " + urls)
    rss_ = feedparser.parse(urls)
    feed_channel = rss_.channel
    # feed_title = feed_channel.title
    rss_feed = feedparser.parse(urls)
    feed_entries = rss_feed.entries
    i = 0
    while i <= len(feed_entries):
        try:
            feeds["source"].append(feed_channel.title)
        except KeyError:
            feeds["source"].append(urls)
        except AttributeError:
            feeds["source"].append(urls)
            # print("boh" + urls)
        i += 1

    for entry in feed_entries:
        feeds["title"].append(entry.title)
        feeds["link"].append(entry.link)
        try:
            pub = entry.published
            dt = parser.parse(pub)
            print()
            feeds["date"].append(dt.astimezone(tz.tzutc()))
        except KeyError:
            print("no pubDate")
        try:
            description = entry.description
            if entry.description_detail.type != 'text/html':
                feeds["description"].append(description)
            else:
                sanitized_description = re.sub("<.*?>", "", description)
                feeds["description"].append(sanitized_description)
        except:
            feeds["description"].append("no Descirption")



print (feeds)


new_data = [{"source": s, "title": t, "description": e, "link": l, "date": d} for s, t, e, l, d in zip(feeds["source"], feeds["title"], feeds["description"], feeds["link"], feeds["date"])]
print(new_data)

for d in new_data:
    post_dic = Post(source=d["source"], title=d["title"], description=d["description"], link=d["link"], date=d["date"])
db.session.add(post_dic)
db.session.commit()
rss_posts = Post.query.all()
print(rss_posts)
# rss_data = json.dumps(new_data, indent=5)
# rss_decoded = json.loads(rss_data)
# print(rss_decoded)


