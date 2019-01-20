import smtplib


def login(email_address,password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_address, password)
    return server


def send_email(SERVER, FROM, TO, SUBJECT, TEXT):
    message = """Name: Gabriel's Server \nFrom: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, TO, SUBJECT, TEXT)
    SERVER.sendmail(FROM, TO, message.encode("utf-8"))


def logout(mail):
    mail.close()
    mail.logout()
