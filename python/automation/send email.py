# Imports
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib as sp

# Content
message = MIMEMultipart()
message["From"] = "Someone"
message["To"] = "testuser@gmail.com"
message["Subject"] = "Hello World"
message.attach(MIMEText("Body"))

with sp.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("testuser@gmail.com", "todayisaniceday123")
    smtp.send_message(message)
    print("Sent!")
