import smtplib
from credentials import *

def sendmail():

    try:
        sender = data_email['gmail']
        sender_password = data_email['password']
        r = 'dsubhadip114@gmail.com'
        # for r in recivers:
        #     content = 'Testing the SMTPLIB'
        #     server = smtplib.SMTP('smtp.gmail.com', 587)
        #     server.ehlo()
        #     server.starttls()
        #     server.login(sender, sender_password)
        #     server.sendmail(sender, r, content)
        #     server.close()
        
        for i in range(6):
            content = 'YOUR MOBILE GOT COMPROMISED'
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(sender, sender_password)
            server.sendmail(sender, r, content)
            server.close()


        # content = 'Testing the SMTPLIB'
        # server = smtplib.SMTP('smtp.gmail.com', 587)
        # server.ehlo()
        # server.starttls()
        # server.login(sender, sender_password)
        # server.sendmail(sender, r, content)
        # server.close()
    
    except Exception as e:
        print(e)

sendmail()