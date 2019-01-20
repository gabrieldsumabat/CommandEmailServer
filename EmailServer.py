import datetime
import os
import Handle
import time
import schedule

from gmail import ReadEmail
from gmail import SendEmail

email_address = os.environ['EMAIL_ADDRESS']
password = os.environ['PASSWORD']


def delete_seen_email():
    ReadEmail.delete_emails(read_server, "(SEEN)")


def clean_log():
    log = open("emailserver.log", "w+")
    log.write("")
    log.close()


def check_inbox():
    log = open("emailserver.log", "a+")
    read_server.select('INBOX')
    messages = ReadEmail.get_email_content(read_server, "(UNSEEN)")
    if len(messages) == 0:
        print("No new emails @ %s \n" % datetime.datetime.now())
        log.write("No new emails @ %s \n" % datetime.datetime.now())
    for message in messages:
        print("NEW MESSAGE: \n%s \n" % message)
        log.write("NEW MESSAGE: \n%s \n" % message)
        subject, text = Handle.handle_commands(message)
        SendEmail.send_email(send_server, email_address, message.address, subject,
                             text)
    log.close()


if __name__ == "__main__":
    read_server = ReadEmail.login(email_address, password)
    send_server = SendEmail.login(email_address, password)

    schedule.every(1).minute.do(check_inbox)
    schedule.every(1).days.do(delete_seen_email)
    schedule.every(3).days.do(clean_log)

    while 1:
        schedule.run_pending()
        time.sleep(1)
