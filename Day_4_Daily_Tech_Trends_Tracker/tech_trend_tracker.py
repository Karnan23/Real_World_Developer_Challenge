import os
import json
import requests
import datetime
import logging
from datetime import timezone

# Load config 
try:
    with open(os.path.join(os.path.dirname(__file__), 'config.json')) as config_file:
        config = json.load(config_file)
        tech_api = config["tech_news_sources"]
        output_folder = config["output_folder"]
        log_file = config["log_file"]
        req_datas = config["news_datas"]

except Exception as e:
    logging.error(f"Error occurred while getting config file: {e}")
    raise

# Setup logging 
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.info("Script started successfully.")

# Create output folder 
os.makedirs(output_folder, exist_ok=True)

# Source-specific fetchers 
# techcrunch
def fetch_techcrunch(data, urls_seen):
    news_list = []
    for item in data:
        news = {
            "title": item.get("title", {}).get("rendered"),
            "url": item.get("link"),
            "author": item.get("author"),
            "published_at": item.get("date"),
            "source": "TechCrunch"
        }
        if news["url"] and news["url"] not in urls_seen:
            news_list.append(news)
            urls_seen.add(news["url"])
            logging.info(f"Fetched: {news['title']}")
    return news_list

# hackernews
def fetch_hackernews(data, urls_seen):
    news_list = []
    hits = data.get("hits", [])
    for item in hits:
        created_ts = item.get("created_utc")
        published_at = datetime.datetime.fromtimestamp(created_ts, tz=timezone.utc).isoformat() if created_ts else datetime.datetime.now(timezone.utc).isoformat()
        news = {
            "title": item.get("title"),
            "url": item.get("url"),
            "author": item.get("author"),
            "published_at": published_at,
            "source": "HackerNews"
        }
        if news["url"] and news["url"] not in urls_seen:
            news_list.append(news)
            urls_seen.add(news["url"])
            logging.info(f"Fetched: {news['title']}")
    return news_list

# reddit
def fetch_reddit(data, urls_seen):
    news_list = []
    posts = data.get("data", {}).get("children", [])
    for post in posts:
        post_data = post.get("data", {})
        created_ts = post_data.get("created_utc")
        published_at = datetime.datetime.fromtimestamp(created_ts, tz=timezone.utc).isoformat() if created_ts else datetime.datetime.now(timezone.utc).isoformat()
        news = {
            "title": post_data.get("title"),
            "url": post_data.get("url"),
            "author": post_data.get("author"),
            "published_at": published_at,
            "source": "Reddit"
        }
        if news["url"] and news["url"] not in urls_seen:
            news_list.append(news)
            urls_seen.add(news["url"])
            logging.info(f"Fetched: {news['title']}")
    return news_list

# Mapping sources 
source_handlers = {
    "techcrunch.com": fetch_techcrunch,
    "hn.algolia.com": fetch_hackernews,
    "reddit.com": fetch_reddit
}

# Tech Trend Tracker
class TechTrendTracker:
    def fetch(self):
        all_news = []
        urls_seen = set()  # Deduplication

        for source_url in tech_api:
            try:
                headers = {}
                if "reddit.com" in source_url:
                    headers["User-Agent"] = "Mozilla/5.0"

                response = requests.get(source_url, headers=headers)
                response.raise_for_status()
                data = response.json()

                handled = False
                for key, func in source_handlers.items():
                    if key in source_url:
                        all_news.extend(func(data, urls_seen))
                        handled = True
                        break

                if not handled:
                    logging.warning(f"No handler defined for {source_url}")

                logging.info(f"All news fetched successfully from {source_url}")

            except requests.exceptions.RequestException as e:
                logging.error(f"Error while fetching from {source_url}: {e}")

        return all_news

    def save(self, all_news):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = os.path.join(output_folder, f"tech_trends_{timestamp}.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(all_news, f, ensure_ascii=False, indent=4)

        logging.info(f"All fetched news saved to {output_file}")


# Run tracker 
if __name__ == "__main__":
    tracker = TechTrendTracker()
    tracker.save(tracker.fetch())
