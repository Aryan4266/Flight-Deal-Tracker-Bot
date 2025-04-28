import smtplib
from email.message import EmailMessage
import requests

def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_username, smtp_password):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_username, smtp_password)
        server.send_message(msg)

def send_discord_alert(message, webhook_url):
    payload = {"content": message}
    requests.post(webhook_url, json=payload)
