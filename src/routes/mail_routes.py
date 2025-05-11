from flask import Blueprint, request
from flask_mail import Message

from src.extensions.extensions import mail, db
import os
import logging

from datetime import datetime
from src.model.email import Email

mail_blueprint = Blueprint("mail_blueprint", __name__, url_prefix="/api/v1/mail")

logger = logging.getLogger(__name__)

@mail_blueprint.route("/send", methods=['POST'])
def send_email():
    logger.info("received a request to send an email")
    logger.info(request.get_json())

    if request.headers.getlist("X-Forwarded-For"):
        client_ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        client_ip = request.remote_addr

    new_record = Email(request.get_json()['name'],
                       request.get_json()['mail'],
                       request.get_json()['message'],
                       client_ip)
    db.session.add(new_record)
    db.session.commit()

    msg = Message(request.get_json()['name'] , sender=os.environ.get('MAIL_USERNAME'), recipients=[os.environ.get('MAIL_USERNAME')])
    msg.html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body>
            <div style="border: 1px solid black; border-radius: 10px; padding: 20px 40px; display: flex; justify-content: center; align-items: center; flex-direction: column;">
                <div style="display: flex; justify-content: start; align-items: center; width: 100%;">
                    <p style="width: 100px;">Sender:</p>
                    <p>{request.get_json()['mail']}</p>
                </div>
                <div style="display: flex; justify-content: start; align-items: center; width: 100%;">
                    <p style="width: 100px;">Message:</p>
                    <p>{request.get_json()['message']}</p>
                </div>
            </div>
        </body>
        </html>
    """
    mail.send(msg)
    return "Sent", 200