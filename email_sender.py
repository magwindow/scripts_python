import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import EMAIL, PASSWORD

message = MIMEMultipart()
to_email = input('Кому отправить письмо: ')

message['Subject'] = input('Тема: ')
message['From'] = EMAIL

body = input('Сообщение: ')
message.attach(MIMEText(body, 'plain'))


server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(EMAIL, PASSWORD)
server.sendmail(EMAIL, to_email, message.as_string())

server.starttls()
server.quit()