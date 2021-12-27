import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # similar to os.path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Pawel Bak'
email['to'] = 'pawelbak300589@gmail.com'
email['subject'] = 'Test Email Subject'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('username', 'password')
    smtp.send_message(email)
    print('Email sent!')
