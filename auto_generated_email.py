import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = '''Hello,
this is a test fo the auto_generated_email
'''

#The mail addressses and passwords
sender_address = 'test01fili@gmail.com'
sender_pass = '22n67qq2'
receiver_address = 'tslesc02@gmail.com'

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python.'

#adding an attachment
#message.attach(MIMEText(mail_content, 'plain'))

#Create SMTP session to send the mail
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('----------Mail Sent----------')



