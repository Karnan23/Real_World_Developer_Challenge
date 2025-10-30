# 🧾 Day 7 – Automated Log Reporter (Python)

This project automatically reads a log file, generates a daily summary report as a PDF, and sends it to a configured email address using secure credentials from a `.env` file.

---

## ⚙️ Features

- Reads and processes application log data.

- enerates a PDF summary report using ReportLab.

- Sends the report automatically via email.

- Uses logging for error handling and tracking.

- Uses dotenv for secure environment variable management.

---

## 🧠 Tech Stack

**Language:** Python

**Libraries Used:**

- os, datetime, logging, smtplib, pathlib

- dotenv for environment variable loading

- reportlab for PDF generation

- email.mime for email attachment handling

---

## 📂 Project Structure
```bash
Day_7_Automated_Log_Reporter/
│
├── main.py                # Main script (log read + PDF + email)
├── .env                   # Environment variables (email credentials)
├── venv/                  # Virtual environment folder
├── report.log             # log file (to be analyzed)
├── summary.log            # logging file (auto generated)
└── generated_report.pdf   # Auto-generated daily PDF
```
---

## 🧰 Setup Instructions

### 1️⃣ Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # For Windows
# or
source venv/bin/activate   # For macOS/Linux
```
### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Configure environment variables in .env (sample)
```bash
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=receiver_email@gmail.com
....
....
```
### 4️⃣ Run the script
```bash
python main.py
```
---

## 📬 Output

- A PDF report summarizing log data.

- An automated email sent with the PDF attached.

- Error logs written to error.log file if any issue occurs.

--- 

## 💡 Author

Karnan