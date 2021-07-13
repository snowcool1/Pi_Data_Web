
'''
import smtplib
from email.mime.text import MIMEText

username = 'april.may.mobile@gmail.com'
password = '!Datalogic1'
server = smtplib.SMTP('smtp.gmail.com', 587)


sender = 'april.may.mobile@gmail.com'
receivers = 'doan.nguyen@datalogic.com'


#port = 587
msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'april.may.mobile@gmail.com'
msg['To'] = 'doan.nguyen@datalogic.com'

#with smtplib.SMTP('smtp.gmail.com', 587) as server:
    
    # server.login('username', 'password')
server.sendmail(sender, receivers, msg.as_string())
#print("Successfully sent email")
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(sender, receivers, msg)
server.quit()
'''

#'
# 
# 
import smtplib
from email.mime.text import MIMEText

sender = 'april.may.mobile@gmail.com'
receivers = 'doan.nguyen@datalogic.com'
msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'

user = 'april.may.mobile@gmail.com'
password = '!Datalogic1'

with smtplib.SMTP("smtp.mailtrap.io", 1025) as server:

    server.login(user, password)
    server.sendmail(sender, receivers, msg.as_string())
    print("mail successfully sent")
    server.quit()
