import logging,smtplib,json,datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
    with open('email_config.json', 'r') as file:
        config = json.load(file)
        SMTP_SERVER = config["SMTP_SERVER"]
        SMTP_PORT = config["SMTP_PORT"]
        SENDER = config["SENDER_NAME"]
        SENDER_EMAIL = config["SENDER_EMAIL"]
        SENDER_PASSWORD = config["SENDER_PASSWORD"]
        RECIPIENT_EMAIL = config["RECIPIENT_EMAIL"]
        NEWS_FILE = config["NEWS_FILE"]
        LOG_FILE = config["LOGGING_FILE"]
        NUM_NEWS = config["NUM_NEWS"]
except Exception as e:
    logging.error(f"Error loading configuration: {e}")
    
logging.basicConfig(filename=LOG_FILE ,level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger().addHandler(logging.StreamHandler())

logging.info("Email bot started.")

def load_news():
    try:
        with open(NEWS_FILE, 'r') as file:
            news_data=json.load(file)
            logging.info("News data loaded successfully.")
            return news_data
    except Exception as e:
        logging.error(f"Error loading news data: {e}")
        return []

def compose_email(news_items):
    try:
        msg=MIMEMultipart()
        msg["from"]=f"{SENDER}<{SENDER_EMAIL}>"
        msg["to"]=RECIPIENT_EMAIL
        msg["subject"]=f"Daily Tech News Update-{datetime.date.today().strftime('%Y-%m-%d')}"
        
        news_content=f"<h3>Today's Top Tech News</h3><ul>"
        for news in news_items[:NUM_NEWS]:
            title=news.get("title","No Title")
            link=news.get("url","No url")
            source=news.get("source","No source")
            news_content+=f"<li><a href='{link}'>{title}</a> - <i>{source}</i></li><br>"
        news_content+="</ul>"
        msg.attach(MIMEText(news_content,'html'))
        logging.info("Email composed successfully.") 
        return msg
        
    except Exception as e:
        logging.error(f"Error composing email: {e}")
        return None
    
def send_email(msg):
    try:
        with smtplib.SMTP(SMTP_SERVER,SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL,SENDER_PASSWORD)
            server.send_message(msg)
            logging.info("Email sent successfully.")
            
    except Exception as e:
        logging.error(f"Error sending email: {e}")
        

if __name__ == "__main__":
    try:
        news_items=load_news()
        email_message=compose_email(news_items)
        if email_message:
            send_email(email_message)
        else:
            logging.error("Email message is None, not sending email.")
        logging.info("Email bot finished execution.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")