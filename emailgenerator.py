import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import settings as stt
from pathlib import Path
import os
from datetime import date


def send_mail():
    try:
        # Main email setup
        message = MIMEMultipart()
        message["from"] = "Newsletter"
        message["to"] = stt.receiverEmail
        message["subject"] = "%s's Newsletter: %s" % (stt.twitterHandle, date.today())
        message.attach(MIMEText("Attached is your twitter newsletter."))
    except Exception as e:
        raise Exception(f"Error initializing email body: {e}")
    
    try:
        # Attaching document
        path = os.path.join(Path().resolve(), '%s_%s.docx' % (stt.twitterHandle, date.today()))
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename={}'.format(Path(path).name))
        message.attach(part)
    except Exception as e:
        raise Exception(f"Error attaching document to email: {e}")
    
    try:
        # Contacting email server and sending email
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(stt.senderEmail, stt.senderPassword)
            smtp.send_message(message)
            print('Email was sent successfully.')
    except Exception as e:
        raise Exception(f"Error contacting server/sending email: {e}")