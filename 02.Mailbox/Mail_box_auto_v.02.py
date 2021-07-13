import os
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart

# Open the plain text file whose name is in textfile for reading.
with open('readme.txt') as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'Day la tieu de cua email v.02'
msg['From'] = 'april.may.mobile@gmail.com'
msg['To'] = 'doan.nguyen@datalogic.com'

# Send the message via our own SMTP server.
s = smtplib.SMTP('smtp.gmail.com', 587)
username = 'april.may.mobile@gmail.com'
password = '!Datalogic1'
s.send_message(msg)
s.quit()