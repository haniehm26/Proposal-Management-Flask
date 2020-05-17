from threading import Thread
from flask_mail import Message

from app import mail
from app import app
from resources.errors import InternalServerError


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send_message(msg)
        except ConnectionRefusedError:
            raise InternalServerError("[MAIL SERVER] not working")


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(
        subject=subject,
        sender=sender,
        recipients=recipients,
        body=text_body,
        html=html_body
    )
    Thread(target=send_async_email, args=(app, msg)).start()
