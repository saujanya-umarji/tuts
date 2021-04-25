from app import app
from services.mail_services import generate_otp

def send_sms():
    sms_otp = generate_otp()
    print(sms_otp)
    return "sms sent!!"