import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Pawel Bak'
email['to'] = 'pawelbak300589@gmail.com'
email['subject'] = 'Test Email Subject'

email.set_content('Some content')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('username', 'password')
    smtp.send_message(email)
    print('Email sent!')
