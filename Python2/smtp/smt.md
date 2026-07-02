# 1) Imports (हमेशा ये लगते हैं):-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart   # अगर attachment ya HTML bhejna ho tab

# 2) Message बनाना:-
msg = MIMEText(body)          # simple text ke liye
# ya
msg = MIMEMultipart()         # attachment/HTML ke liye

msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email


#  3) Server connect + login (ये lines हर Gmail/Outlook script में same rehti hain):-

server = smtplib.SMTP("smtp.gmail.com", 587)   # Gmail ke liye fixed hai
server.starttls()                               # connection ko encrypt karta hai
server.login(sender_email, password)

# 4) Email भेजना:-
server.send_message(msg)
# ya purana style:
server.sendmail(sender_email, receiver_email, msg.as_string())

# 5) Connection बंद करना:-
server.quit()
(तुमने with smtplib.SMTP(...) as server: use किया है — ये better तरीका है, इसमें quit() की ज़रूरत नहीं, with block khatam hote hi connection close ho jata hai.)


# summary:-
याद रखने की trick
बस ये sequence yaad rakho, sabme same hota hai:
Connect → Encrypt (starttls) → Login → Message banao → Bhejo → Close
Har provider (Gmail, Outlook, Yahoo) ka sirf smtp.gmail.com वाला address aur port change hota hai, baaki syntax लगभग identical रहता है:

Gmail: smtp.gmail.com, port 587
Outlook: smtp.office365.com, port 587
Yahoo: smtp.mail.yahoo.com, port 587