import smtplib
from email.mime.text import MIMEText

sender = 'april.may.mobile@gmail.com'
receivers = ['doan.nguyen@datalogic.com']


port = 1025
msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'april.may.mobile@gmail.com'
msg['To'] = 'doan.nguyen@datalogic.com'

with smtplib.SMTP('smtp.gmail.com', 1025) as server:
    
    # server.login('username', 'password')
    server.sendmail(sender, receivers, msg.as_string())
    print("Successfully sent email")