import smtplib
from email.mime.text import MIMEText

msg = MIMEText("your message")
msg["subject"] = "Email ka title"
msg["From"] = "mansoorikaif365@gmail.com"
msg["To"] = "mansoorimohdkaif786@gmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("mansoorikaif365@gmail.com", "bzul uqzw nxkk lgvg")
    server.send_message(msg)