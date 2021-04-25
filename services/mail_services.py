from threading import Thread
from flask_mail import Message
from app import app
from app import mail
import smtplib, ssl
import math,random




def sendtutsmail(app,msg,sender,recipients):            #sending mail in smtp server without using flask-mail
    try:
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com" 
        #localhost = "localhost"
        #port = 1025
        password = input("Type your password and press enter: ")
        #password = "GoldaUmarji@97"
        print(sender)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender,recipients,msg)
    except ConnectionRefusedError:
        raise InternalServerError("[MAIL SERVER] not working")

def send_async_email(app, msg,sender,recipients):                   #sending mail in flask-mail!! 
    with app.app_context():
        try:
            print("message will be printed")
            mail.send(msg)
        except ConnectionRefusedError:
            raise InternalServerError("[MAIL SERVER] not working")

 
def send_email(subject,recipients, text_body, html_body):
    sender = "saujanyapumarji@gmail.com"
    msg = Message(subject,recipients,sender)
    msg.body= text_body
    msg.html = html_body
    numaricpassword = generate_otp()
    print(numaricpassword)
    # msg = ('This is from tuts application!!'
    #         'we are sharing you the one time password of tuts application which will be used to login into our application.'
    #         'your otp is  ' +numaricpassword+
    #         '  please do not share the otp with anyone. thank you for joining our team' )
    Thread(target=send_async_email, args=(app, msg,sender,recipients )).start()


def generate_otp():
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

