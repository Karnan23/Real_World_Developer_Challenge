# Daily Tech Trends Tracker – Day 4

A Python script that fetches the latest tech news from **TechCrunch**, **Hacker News**, and **Reddit Technology** and saves it as a JSON file. It supports logging and deduplication of news articles.

---

## Features

- Fetches latest tech news from multiple sources.
- Supports **TechCrunch**, **Hacker News**, and **Reddit**.
- Handles missing data and sets default timestamps when needed.
- Deduplicates news based on URLs.
- Saves all news to a timestamped JSON file.
- Logs all fetch and error activities.

---

## Requirements

- Python 3.11+
- Packages:
  - `requests`
  - `logging`
  - `json`

Install dependencies with:

```bash
pip install requests
```
## Setup

1. Clone the repository or download the project folder.

2. Add a config.json in the project folder:

```bash
{
  "tech_news_sources": [
    "https://techcrunch.com/wp-json/wp/v2/posts?per_page=5",
    "https://hn.algolia.com/api/v1/search_by_date?tags=story&hitsPerPage=5",
    "https://www.reddit.com/r/technology/new.json?limit=5"
  ],
  "output_folder": "Fetched_Tech_Trends",
  "log_file": "tech_trend_tracker.log",
  "news_datas": ["title", "source", "url", "published_at", "author"]
}
```

3. Ensure the output folder exists (the script will create it automatically if missing).

## Usage

1. Run the script:
```bash
python tech_trend_tracker.py
```

The script will:

- Fetch news from all configured sources.

- Deduplicate news based on URLs.

- Save results in output_folder as a JSON file.

- Log all fetched news and errors in log_file.

## Example Output
```bash
[
    {
        "title": "Spiro raises $100M, the largest-ever investment in Africa’s e-mobility",
        "url": "https://techcrunch.com/article-link",
        "author": "Author Name",
        "published_at": "2025-10-21T16:00:47+00:00",
        "source": "TechCrunch"
    },
    {
        "title": "Show HN: Xcache.io – fast, instant, permissionless Redis cache",
        "url": "https://news.ycombinator.com/item?id=123456",
        "author": "HNUser",
        "published_at": "2025-10-21T16:00:48+00:00",
        "source": "HackerNews"
    }
]
```
## Logging

Logs saved in log_file as defined in config.json.

Includes:

- Script start message

- Each fetched news title

- Fetch errors

- Successful save of all news

## Notes

1. Reddit requires a User-Agent header.

2. HackerNews timestamps (created_utc) are converted to ISO format with UTC timezone.

3. TechCrunch date fields are used as-is.

4. Posts without URLs are skipped.

## Author

Karnan G