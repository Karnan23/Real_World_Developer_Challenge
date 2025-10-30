import os,logging,datetime,smtplib
from dotenv import load_dotenv
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

try:
    load_dotenv()
    sender_mail=os.getenv("SENDER_EMAIL")
    sender_password=os.getenv("SENDER_PASSWORD")
    receiver_mail=os.getenv("RECEIVER_MAIL")
    log_path=os.getenv("LOG_PATH")
    report_path=os.getenv("REPORT_PATH")
    report_name=os.getenv("REPORT_NAME")
    smtp_server=os.getenv("SMTP_SERVER")
    smtp_port=os.getenv("SMTP_PORT")
    email_subject=os.getenv("EMAIL_SUBJECT")

except Exception as e:
    logging.error(f"Error loading config: {e}")

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s', handlers=[logging.FileHandler("summary.log"),logging.StreamHandler()])
logging.info("Summary bot started...")

def log_analyze(log_path):
    try:
        total_entries=0
        error_entries=0
        info_entries=0
        Warning_entries=0
        errors=[]
        infos=[]
        warnings=[]
        with open(log_path,'r') as log_file:
            content=log_file.readlines()
            for i in content:
                total_entries+=1
                if "ERROR" in i:
                    error_entries+=1
                    errors.append(i)
                if "INFO" in i:
                    info_entries+=1
                    infos.append(i)
                if "WARNING" in i:
                    Warning_entries+=1
                    warnings.append(i)
        logging.info(f"Total log entries: {total_entries}")
        logging.info(f"Total ERROR entries: {error_entries}")
        logging.info(f"Total INFO entries: {info_entries}")
        logging.info(f"Total WARNING entries: {Warning_entries}")

        return {
            "total_entries": total_entries,
            "error_entries": error_entries,
            "info_entries": info_entries,
            "warning_entries": Warning_entries,
            "errors": errors,
            "infos": infos,
            "warnings": warnings
        }
                
    except Exception as e:
        logging.error(f"Error on log analyze : {e}")

def make_pdf(log_details, log_report_name=report_name):
    try:
        pdf = SimpleDocTemplate(log_report_name, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        story.append(Paragraph("<b>===== SYSTEM LOG REPORT =====</b>", styles["Title"]))
        story.append(Spacer(1, 20))
        story.append(Paragraph(f"Date: {datetime.datetime.now():%Y-%m-%d}", styles["Normal"]))
        story.append(Spacer(1, 20))

        summary = f"""
        <b>Summary of Log Analysis:</b><br/>
        Total Log Entries: {log_details['total_entries']}<br/>
        Info Logs: {log_details['info_entries']}<br/>
        Errors: {log_details['error_entries']}<br/>
        Warnings: {log_details['warning_entries']}
        """
        story.append(Paragraph(summary, styles["Normal"]))
        story.append(Spacer(1, 20))

        story.append(Paragraph("<b>Infos:</b>", styles["Heading3"]))
        for line in log_details["infos"]:
            story.append(Paragraph(line.strip(), styles["Normal"]))

        story.append(Spacer(1, 15))
        story.append(Paragraph("<b>Errors:</b>", styles["Heading3"]))
        for line in log_details["errors"]:
            story.append(Paragraph(line.strip(), styles["Normal"]))

        story.append(Spacer(1, 15))
        story.append(Paragraph("<b>Warnings:</b>", styles["Heading3"]))
        for line in log_details["warnings"]:
            story.append(Paragraph(line.strip(), styles["Normal"]))

        pdf.build(story)
        logging.info("PDF generated successfully")

    except Exception as e:
        logging.error(f"PDF Generation Error: {e}")


def send_mail(report_path):
    try:
        msg=MIMEMultipart()
        msg["From"]=f"{email_subject}<{sender_mail}>"
        msg["To"]=receiver_mail
        msg["Subject"]=f"{email_subject} - {datetime.datetime.now(): %Y %m %d}"

        with open(report_path,'rb') as f:
            part=MIMEBase("application","octet-stream")
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % report_name)
            msg.attach(part)
            logging.info("Msg created successfully")

        with smtplib.SMTP(smtp_server,smtp_port) as server:
            server.starttls()
            server.login(sender_mail,sender_password)
            server.send_message(msg)
            logging.info("Msg send successfully")
    except Exception as e:
        logging.error(f"Email Error : {e}")


if __name__=="__main__":
    try:
        log_details=log_analyze(log_path)
        make_pdf(log_details)
        send_mail(report_path)
        logging.info("Summary work completed Successfully...")
    except Exception as e:
        logging.error(f"Summary work ended Unsuccessfully... {e}")