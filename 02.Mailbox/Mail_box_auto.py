import os
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.message import Message
from email.header import Header


from_address = 'april.may.mobile@gmail.com'
to_address = 'doan.nguyen@datalogic.com'
username = 'april.may.mobile@gmail.com'
password = '!Datalogic1'
server = smtplib.SMTP('smtp.gmail.com', 587)

msg = 'This is email test 5th'

#msg = Message()
#h = Header('Day la tieu de lan 4')
#msg['Subject'] = h
#msg.as_string('ddd')

server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(from_address, to_address, msg)
server.quit()
