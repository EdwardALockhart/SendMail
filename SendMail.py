def send_mail_attachments(user, app_pwd, recipient, subject, body, files, server, port):
    import smtplib
    from os.path import basename
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    
    msg = MIMEMultipart()
    msg["From"] = user
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body))

    for i in files or []:
        with open(i, "rb") as file:
            part = MIMEApplication(file.read(), Name = basename(i))
        part["Content-Disposition"] = 'attachment; filename = "%s"' % basename(i)
        msg.attach(part)

    with smtplib.SMTP(server, port, timeout = 15) as mail:
        mail.ehlo() # Identify ourselves
        mail.starttls() # Start encryption
        mail.ehlo() # Identify ourselves as encrypted
        mail.login(user, app_pwd)
        mail.sendmail(user, recipient, msg.as_string())
        mail.close() 
    print("Transmitted")

send_mail_attachments(user = "",
                      app_pwd = "",
                      recipient = "",
                      subject = "",
                      body = "",
                      files = ["/file1.txt", "/file2.txt"],
                      server = "",
                      port = 999)
