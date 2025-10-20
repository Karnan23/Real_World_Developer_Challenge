# 🔍 GitHub Repo Tracker (Day 3 – Real World Developer Challenge)

## 📘 Overview
This Python project automatically fetches and saves public repository details of any given GitHub user.  
It uses the **GitHub REST API**, allowing developers to monitor open-source projects, audit profiles, or gather data for dashboards.

---

## ⚙️ Features
✅ Fetches repository info (name, stars, forks, language, created date)  
✅ Handles multiple users dynamically  
✅ Logs all activities and errors to a log file  
✅ Automatically creates output folder if missing  
✅ Saves each user's data in a clean JSON format  

---

## 🧩 Tech Stack
- Python 3.x  
- Requests (for GitHub API)  
- JSON (for config and output)  
- Logging (for activity tracking)  
- OS module (for file handling)

---

## ⚙️ Configuration (config.json)

Example configuration file:
```json
{
    "github_users": ["torvalds", "TheAlgorithms"],
    "output_directory": "github_output",
    "log_file": "github_logs.log",
    "req_github_details": ["name", "html_url", "stargazers_count", "forks_count", "language", "created_at"]
}
```
## How to Run

1. Clone this repo or copy the Day_3_GitHub_Repo_Tracker folder.

2. Install dependencies:

```bash
pip install requests
```

3. Run the script:

```bash
python repo_fetcher.py
```

4. Check the output folder — JSON files will be generated for each GitHub user listed.

## Logs

All events, errors, and file actions are recorded in github_logs.log for easy debugging.

## 🧠 Learning Outcome

You’ll understand:

- How to consume REST APIs in Python

- Handling API responses and errors gracefully

- File automation for real-world developer tasks

## 🧑‍💻 Author

Karnan