import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(email, name):
    fromaddr = "rowafean@gmail.com"
    password = "rowafean123"
    toaddr = email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Database test!"

    body = "Hello " + name + ". You are successfully registered"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr,password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
