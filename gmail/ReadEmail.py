import email
import imaplib

from gmail import Message


def login(email_address, password):
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(email_address, password)
    mail.select("INBOX")
    return mail


def get_first_text_block(email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()


def get_email_content(mailbox, mail_filter):
    message_list = []
    result, data = mailbox.search(None, mail_filter)
    ids = data[0]
    email_id_list = ids.split()
    if len(email_id_list) != 0:
        for email_id in email_id_list:
            result, data = mailbox.fetch(email_id, "(RFC822)")
            email_message = email.message_from_bytes(data[0][1])  # Parsed Text
            from_information = email.utils.parseaddr(email_message['FROM'])
            name = from_information[0].strip()
            address = from_information[1].strip()
            subject = email_message['SUBJECT'].strip()
            content = get_first_text_block(email_message)
            message_list.append(Message.Message(name, address, subject, content))
    return message_list


def delete_emails(mailbox, mail_filter):
    message_list = []
    result, data = mailbox.search(None, mail_filter)
    ids = data[0]
    id_list = ids.split()
    if len(id_list) != 0:
        for i in id_list:
            mailbox.store(i, '+FLAGS', '\\Deleted')
        mailbox.expunge()
    return message_list


def logout(mail):
    mail.close()
    mail.logout()
