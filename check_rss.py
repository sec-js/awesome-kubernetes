import requests
import feedparser

urls_to_test = [
    "https://www.anthropic.com/feed.xml",
    "https://www.anthropic.com/rss.xml",
    "https://www.anthropic.com/index.xml",
    "https://openai.com/news/rss.xml",
    "https://openai.com/blog/rss.xml",
    "https://developers.googleblog.com/feeds/posts/default?alt=rss",
    "https://developers.googleblog.com/rss",
    "https://cursor.com/blog/rss",
    "https://cursor.com/rss",
    "https://www.uber.com/en-US/blog/engineering/rss/",
    "https://eng.uber.com/feed/",
    "https://blog.developer.atlassian.com/feed/",
    "https://engineering.atlassian.com/feed/",
    "https://netflixtechblog.com/feed",
    "https://cloud.google.com/blog/rss"
]

for url in urls_to_test:
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
        if r.status_code == 200:
            d = feedparser.parse(r.content)
            if len(d.entries) > 0:
                print(f"VALID: {url} ({len(d.entries)} entries)")
            else:
                print(f"EMPTY/INVALID: {url}")
        else:
            print(f"FAIL ({r.status_code}): {url}")
    except Exception as e:
        print(f"ERROR: {url} -> {e}")
