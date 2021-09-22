import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587 # for starttls
sender_email = "test01fili@gmail.com"
receiver_email = "tslesc02@gmail.com"
password = input("Type you password and press enter: ")
#password = getpass.getpass(promtp='Password: ', stream=None)
message = """
Subject: Hi There

this is my first test of an email."""


#Creates a secure SSL context(find out what context is)
context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server,port)
    # server.ehlo()
    server.starttls(context=context)
    # server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

except Exception as e:
    print(e)
finally:
    server.quit()


#receiver_email = "tslesc02@gmail.com"



#message = """\
#    Subject: Hi there  

 #   This Message is the first text"""


#with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#    server.login("test01fili@gmail.com", password) #Send email
 #   server.sendmail(sender_email, receiver_email, message)

