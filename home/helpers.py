from django.core.mail import send_mail
from django.conf import settings
import smtplib
import ssl


def send_forget_pass_mail(fname, email, token):
    subject = 'Your Link to reset your Password'
    message = f'Hello {fname},\n\t thanks for choosing AkHospitals \n\tClick on the link to reset your password http://127.0.0.1:8000/change-password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from,
              recipient_list, fail_silently=False)

    # smtp_server = "smtp.gmail.com"
    # port = 465
    # sender_email = "2020ucp1821@mnit.ac.in"
    # password = 'akbasniwal'
    # receiver_email = email
    # context = ssl.create_default_context()
    # server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
    # server.login(sender_email, password)
    # server.sendmail(sender_email, receiver_email, message)
    return True
