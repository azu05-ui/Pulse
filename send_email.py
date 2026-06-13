import os
import smtplib
from email.mime.text import MIMEText

with open("daily_summary.txt", "r", encoding="utf-8") as f:
    content = f.read()

msg = MIMEText(content)
msg["Subject"] = "Pulse Daily Summary"
msg["From"] = os.environ["EMAIL_USER"]
msg["To"] = os.environ["EMAIL_TO"]

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(
    os.environ["EMAIL_USER"],
    os.environ["EMAIL_PASS"]
)

server.sendmail(
    os.environ["EMAIL_USER"],
    os.environ["EMAIL_TO"],
    msg.as_string()
)

server.quit()

print("Email sent successfully!")