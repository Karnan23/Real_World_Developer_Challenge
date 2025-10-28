# 🧠 Daily Tech Report Automation

- This project automatically generates a **Daily Tech News Excel Report** from a JSON dataset and emails it as an attachment using Python.  
- It’s designed with proper logging, modular functions, environment variable handling, and secure email delivery.

---

## 🚀 Features
✅ Reads tech news data from a JSON file  
✅ Creates a well-formatted Excel report (auto column width, styled headers)  
✅ Sends the report automatically via email (with attachment)  
✅ Secure configuration via `.env` file (no credentials in code)  
✅ Detailed logging (both console and file)  
✅ Structured and modular design with proper error handling  

---

## 🧩 Tech Stack
- **Python 3.10+**
- **openpyxl** – for Excel report creation  
- **smtplib**, **email.mime** – for email sending  
- **dotenv** – for environment variable management  
- **logging** – for runtime tracking  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/daily-tech-report.git
cd daily-tech-report
```
### 2️⃣ Setup Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 4️⃣ Install Required Dependencies
```bash
pip install -r requirements.txt
```
### 5️⃣ Configure Environment Variables

Create a .env file in the project root with the following keys:
```bash
SENDER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password
RECEIVER_EMAIL=receiver_email@gmail.com
REPORT_NAME=Daily_Tech_Report.xlsx
EMAIL_SUBJECT=Daily Tech Report
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
NEWS_PATH=news_data.json
```
---

## 🧠 Project Structure
```bash
daily-tech-report/
│
├── venv/                    # Virtual environment (ignored in Git)
├── main.py                  # Main script file
├── .env                     # Environment configuration (ignored in Git)
├── requirements.txt         # Dependencies list
├── report.log               # Log file
├── reports.xlsx             # Generated Excel report file
├── news_data.json           # Sample JSON dataset
└── README.md                # Documentation
```
---

## 🧪 Running the Project
```bash
python main.py
```
Once executed, the script will:

- Load configuration and data
- Create a formatted Excel report
- Email the report to the specified recipient
- Log all actions to report.log

## 📜 Example Log Output
```bash
2025-10-26 14:31:05,401 - INFO - Configuration loaded successfully.
2025-10-26 14:31:05,403 - INFO - Script Started...
2025-10-26 14:31:06,122 - INFO - Excel report file created successfully: Daily_Tech_Report.xlsx
2025-10-26 14:31:06,900 - INFO - Email sent successfully!
```
---

## 🧑‍💻 Author

Karnan