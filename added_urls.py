added_urls = ["https://www.cryptohackers.party/feed/rss/", "https://www.cointelegraph.com/rss-feeds",
              "https://www.coindesk.com/feed/rss", "https://www.ccn.com/feed/",
              "https://www.nakamotoinstitute.org/mempool/feed/",
              "https://www.china-files.com/feed/rss", "https://agfundernews.com/feed/rss"]

# # http://www.reddit.com/r/``{SUBREDDIT_NAME}``/new/.rss?sort=new
# for scanned_rules in added_urls:
#     if scanned_rules.startswith('http://www.reddit.com/'):
#         user = input("[N]ew or [H]ot: ")
#         if user == 'n':
#             new = scanned_rules + '/new/.rss?sort=new'
#             # print(new)
#             user_urls.append(new)
#         elif user == 'h':
#             hot = scanned_rules + '/hot/.rss?sort=hot'
#             # print(hot)
#             user_urls.append(hot)
#     else:
#         user_urls.append(scanned_rules)

# print(user_urls)
