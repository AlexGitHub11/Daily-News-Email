import smtplib, ssl
import os

def send(message):
    """ Send email """
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("EMAILUSERNAME")
    password = os.getenv("PASSWORD")
    receiver = os.getenv("EMAILUSERNAME")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

