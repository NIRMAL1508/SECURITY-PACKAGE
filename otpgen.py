import random
import smtplib
from email.message import EmailMessage

def otpgenerator(receiver_email):
    randomNumber = random.randint(100000,999999)

    sender_email ="adhugaming1342@gmail.com"
    sender_password = "sejeohczdffexusl"

    msg = EmailMessage()
    msg.set_content('''
    \n
    Hey User,
    Your OTP is {}
    \n
    '''.format(randomNumber))

    msg['Subject'] = 'One Time Password'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email,sender_password)
    server.send_message(msg)
    server.quit()

    return randomNumber