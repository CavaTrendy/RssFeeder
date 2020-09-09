import feedparser
import webbrowser


def yahoo():
    feed = feedparser.parse("https://finance.yahoo.com/rss/")
    # feed_title = feed['feed']['title']  # NOT VALID
    feed_entries = feed.entries
    for entry in feed.entries:
        article_title = entry.title
        article_link = entry.link
        article_published_at = entry.published  # Unicode string
        article_published_at_parsed = entry.published_parsed  # Time object
        # article_author = entry.author  DOES NOT EXIST
        # content = entry.summary
        # article_tags = entry.tags  DOES NOT EXIST

        print("{}[{}]".format(article_title, article_link))
        print("Published at {}".format(article_published_at))
        # print ("Published by {}".format(article_author))
        # print("Content {}".format(content))
        # print("catagory{}".format(article_tags))


def reddit():
    feed = feedparser.parse("http://www.reddit.com/r/learnphyton+Python+learnprogramming+programming+swift.rss ")
    # feed_title = feed['feed']['title']  # NOT VALID
    feed_entries = feed.entries
    for entry in feed.entries:
        article_title = entry.title
        article_link = entry.link
        # article_published_at = entry.published  # Unicode string
        # article_published_at_parsed = entry.published_parsed  # Time object
        # article_author = entry.author  DOES NOT EXIST
        # content = entry.summary
        # article_tags = entry.tags  DOES NOT EXIST

        print("{}[{}]".format(article_title, article_link))
        # print("Published at {}".format(article_published_at))
        # print ("Published by {}".format(article_author))
        # print("Content {}".format(content))
        # print("catagory{}".format(article_tags))

def main():
    yahoo()
    reddit()

if __name__ == '__main__':
    main()
