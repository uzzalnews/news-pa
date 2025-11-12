import feedparser
import json
from datetime import datetime

RSS_FEEDS = {
    "BBC": "http://feeds.bbci.co.uk/news/rss.xml",
    "AlJazeera": "https://www.aljazeera.com/xml/rss/all.xml",
    "Reuters": "https://www.reutersagency.com/feed/?best-topics=top-news",  # alt: https://feeds.reuters.com/reuters/topNews
    "CNN": "http://rss.cnn.com/rss/edition.rss",
    "Dawn": "https://www.dawn.com/feed",
    "APNews": "https://apnews.com/apf-topnews?format=xml",
    "NYTimes": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "MiddleEastEye": "https://www.middleeasteye.net/rss",
    "GeoTV": "https://www.geo.tv/rss/1/0",
    "NDTV": "https://feeds.feedburner.com/ndtvnews-top-stories",
    "TheGuardian": "https://www.theguardian.com/world/rss"
    
}

BREAKING_KEYWORDS = [
    "BREAKING", "Breaking", "Urgent", "LIVE",
    "জরুরি", "দুর্ঘটনা", "বিস্ফোরণ", "হামলা",
    "মৃত", "নিহত", "গুরুতর"
]

def is_breaking(title):
    return any(word in title for word in BREAKING_KEYWORDS)

def fetch_all_news():
    all_news = {}
    breaking_news = []

    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        items = []

        for entry in feed.entries[:5]:
            data = {"title": entry.title, "link": entry.link}
            items.append(data)

            # ✅ Breaking detection
            if is_breaking(entry.title):
                breaking_news.append({"source": source, **data})

        all_news[source] = items

    return all_news, breaking_news


if __name__ == "__main__":
    all_news, breaking = fetch_all_news()

    final = {
        "breaking": breaking,
        "news": all_news,
        "last_updated": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    }

    with open("latest_news.json", "w", encoding="utf-8") as f:
        json.dump(final, f, indent=2, ensure_ascii=False)

    print("✅ Breaking news detected:", len(breaking))
