import feedparser
import time

# আমরা BBC থেকে নিউজ টানবো (তুমি পরে অন্য সাইটও যোগ করতে পারবে)
RSS_URL = "http://feeds.bbci.co.uk/news/rss.xml"

def fetch_news():
    feed = feedparser.parse(RSS_URL)
    print("📰 Latest BBC Headlines:\n")
    for entry in feed.entries[:5]:
        print(f"• {entry.title}")
        print(f"  {entry.link}\n")

if __name__ == "__main__":
    while True:
        fetch_news()
        print("🔁 Next update in 5 minutes...\n")
        time.sleep(300)  # প্রতি ৫ মিনিট পর পর আপডেট
