import feedparser
import json
from datetime import datetime

# একাধিক নিউজ সাইটের RSS লিংক
RSS_FEEDS = {
    "BBC": "http://feeds.bbci.co.uk/news/rss.xml",
    "CNN": "http://rss.cnn.com/rss/edition.rss",
    "AlJazeera": "https://www.aljazeera.com/xml/rss/all.xml",
    "ProthomAlo": "https://www.prothomalo.com/feed",
    "BDNews24": "https://bangla.bdnews24.com/?widgetName=rssfeed&widgetId=1150&getXmlFeed=true"
}

def fetch_all_news():
    all_news = {}
    for source, url in RSS_FEEDS.items():
        print(f"Fetching from {source}...")
        feed = feedparser.parse(url)
        all_news[source] = [
            {"title": entry.title, "link": entry.link}
            for entry in feed.entries[:5]
        ]
    return all_news

if __name__ == "__main__":
    news_data = fetch_all_news()
    news_data["last_updated"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    with open("latest_news.json", "w", encoding="utf-8") as f:
        json.dump(news_data, f, indent=2, ensure_ascii=False)

    print("✅ নিউজ ফাইল আপডেট সম্পন্ন!")
