from email.message import EmailMessage
from smtplib import SMTP_SSL
from szblony_mail import *
import os

mail = EmailMessage()
mail['From'] = senders_address()
mail['To'] = recipients_address()

title, content, typeof = title_email()
mail.set_content(content)
mail['Subject'] = title


print(mail)
connector = SMTP_SSL('smtp.gmail.com')
connector.login(os.environ.get('EMAIL_USERNAME'), os.environ.get('EMAIL_PASSWORD'))
connector.send_message(mail)