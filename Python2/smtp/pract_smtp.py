import smtplib
from email.mime.text import MIMEText

'''
def send_email(subject,body):
    sender_email="mansoorikaif365@gmail.com"
    reciever_email="mansoorimohdkaif786@gmail.com"
    password="bzul uqzw nxkk lgvg"
    
    msg=MIMEText(body)
    msg["Subject"]=subject
    msg["From"]=sender_email
    msg["To"]=reciever_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(msg)
send_email("Backup Completed","Backup Created Successfully")
'''
'''
server = smtplib.SMTP("smtp.gmail.com", 587)
print(server)
'''
'''
serv = "smtp.gmail.com"
port = 587
print(f"SMTP Server: {serv}")
print(f"Port: {port}")
'''

'''
server = smtplib.SMTP("smtp.gmail.com", 587)
print("connection successfully")

server.quit()
print("Connection Closed")
'''

'''
server =smtplib.SMTP("smtp.gmail.com", 587)
print("Connected")
server.ehlo()
print("hello")
'''

'''
server = smtplib.SMTP("smtp.gmail.com")
server.starttls()
print("TLS started")
'''
'''
def send_email(subject,body):
    sender_email="amad123@gmail.com"
    reciever_email="kshi342@gmail.com"
    password="dkks wjie abh"

    msg=MIMEText(body)
    msg["Subject"]=subject
    msg["From"]=sender_email
    msg["To"]=reciever_email
'''

def send_email(subject,body):
    sender_email="amad123@gmail.com"
    reciever_email="kshi342@gmail.com"
    password="dkks wjie abh"

    msg=MIMEText(body)
    msg["Subject"]=subject
    msg["From"]=sender_email
    msg["To"]=reciever_email

    server = smtplib.SMTP("smtp.gmail.com")
    server.login(sender_email,password)
print("login successfully")