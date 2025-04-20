import imaplib, email
from email.header import decode_header

def fetch_emails(server, user, password, folder="INBOX"):
    mail = imaplib.IMAP4_SSL(server)
    mail.login(user, password)
    mail.select(folder)
    _, data = mail.search(None, 'ALL')
    emails = []
    for num in data[0].split():
        _, msg_data = mail.fetch(num, '(RFC822)')
        raw_email = email.message_from_bytes(msg_data[0][1])
        subject = decode_header(raw_email["Subject"])[0][0]
        body = ""
        if raw_email.is_multipart():
            for part in raw_email.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    break
        else:
            body = raw_email.get_payload(decode=True).decode()
        emails.append({"subject": subject, "body": body, "from": raw_email["From"]})
    return emails
