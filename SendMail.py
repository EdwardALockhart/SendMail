def send_attachments(user, app_pwd, recipient, subject, body, files, server, port):
    import smtplib
    from os.path import basename
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body))

    for i in files or []:
        with open(i, 'rb') as file:
            part = MIMEApplication(file.read(), Name = basename(i))
        part['Content-Disposition'] = 'attachment; filename = "%s"' % basename(i)
        msg.attach(part)

    with smtplib.SMTP(server, port, timeout = 15) as mail:
        mail.ehlo() # Identify ourselves
        mail.starttls() # Start encryption
        mail.ehlo() # Identify ourselves as encrypted
        mail.login(user, app_pwd)
        mail.sendmail(user, recipient, msg.as_string())
        mail.close()

send_attachments(user = 'test@gmail.com',
                 app_pwd = '',
                 recipient = '',
                 subject = 'subject',
                 body = 'body',
                 files = ["/home/Documents/file1.csv", "/home/Documents/file2.csv"],
                 server = 'smtp.gmail.com',
                 port = 587,)
